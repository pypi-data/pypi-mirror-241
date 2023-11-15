"""Base module for interacting with LLM APIs."""
import re
import os
import json
import time
import datetime
from typing import Any, AsyncGenerator, List, Dict, Optional, Union, Generator, Tuple
from attr import dataclass

import openai
from pydantic import BaseModel
from dotenv import load_dotenv
from litellm import completion, acompletion
from litellm import ModelResponse

from promptmodel.utils.types import LLMResponse, LLMStreamResponse
from promptmodel.utils import logger
from promptmodel.utils.enums import ParsingType, ParsingPattern, get_pattern_by_type
from promptmodel.utils.output_utils import convert_str_to_type, update_dict
from promptmodel.utils.prompt_util import (
    num_tokens_for_messages,
    num_tokens_from_function_call_output,
    num_tokens_from_functions_input,
)

load_dotenv()


class Role:
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    FUNCTION = "function"


class OpenAIMessage(BaseModel):
    role: Optional[str] = None
    content: Optional[str] = ""
    function_call: Optional[Dict[str, Any]] = None
    name: Optional[str] = None


DEFAULT_MODEL = "gpt-3.5-turbo"


@dataclass
class ParseResult:
    parsed_outputs: Dict[str, Any]
    error: bool
    error_log: Optional[str]


class LLM:
    def __init__(self, rate_limit_manager=None):
        self._rate_limit_manager = rate_limit_manager

    @classmethod
    def __parse_output_pattern__(
        cls,
        raw_output: Optional[str] = None,
        parsing_type: Optional[ParsingType] = None,
    ) -> ParseResult:
        if parsing_type is None:
            return ParseResult(parsed_outputs={}, error=False, error_log=None)
        if raw_output is None:
            return ParseResult(parsed_outputs={}, error=True, error_log="No content")
        parsing_pattern = get_pattern_by_type(parsing_type)
        whole_pattern = parsing_pattern["whole"]
        parsed_results = re.findall(whole_pattern, raw_output, flags=re.DOTALL)
        parsed_outputs = {}
        error: bool = False
        error_log: str = None

        try:
            for parsed_result in parsed_results:
                key = parsed_result[0]
                type_str = parsed_result[1]
                value = convert_str_to_type(parsed_result[2], type_str)
                parsed_outputs[key] = value
        except Exception as e:
            error = True
            error_log = str(e)

        return ParseResult(
            parsed_outputs=parsed_outputs,
            error=error,
            error_log=error_log,
        )

    def __validate_openai_messages(
        self, messages: List[Dict[str, str]]
    ) -> List[OpenAIMessage]:
        """Validate and convert list of dictionaries to list of OpenAIMessage."""
        res = []
        for message in messages:
            res.append(OpenAIMessage(**message))
        return res

    def run(
        self,
        messages: List[Dict[str, str]],
        functions: List[Any] = [],
        model: Optional[str] = DEFAULT_MODEL,
        *args,
        **kwargs,
    ) -> LLMResponse:
        """Return the response from openai chat completion."""
        response = None
        try:
            response = completion(
                model=model,
                messages=[
                    message.model_dump(exclude_none=True)
                    for message in self.__validate_openai_messages(messages)
                ],
                functions=functions,
            )

            content = (
                response.choices[0]["message"]["content"]
                if "content" in response.choices[0]["message"]
                else None
            )
            call_func = (
                response.choices[0]["message"]["function_call"]
                if "function_call" in response.choices[0]["message"]
                else None
            )
            return LLMResponse(
                api_response=response, raw_output=content, function_call=call_func
            )
        except Exception as e:
            if response is not None:
                return LLMResponse(api_response=response, error=True, error_log=str(e))
            else:
                return LLMResponse(api_response=None, error=True, error_log=str(e))

    async def arun(
        self,
        messages: List[Dict[str, str]],
        functions: List[Any] = [],
        model: Optional[str] = DEFAULT_MODEL,
        *args,
        **kwargs,
    ) -> LLMResponse:
        """Return the response from openai chat completion."""
        response = None
        try:
            response = await acompletion(
                model=model,
                messages=[
                    message.model_dump(exclude_none=True)
                    for message in self.__validate_openai_messages(messages)
                ],
                functions=functions,
            )
            content = (
                response.choices[0]["message"]["content"]
                if "content" in response.choices[0]["message"]
                else None
            )
            call_func = (
                response.choices[0]["message"]["function_call"]
                if "function_call" in response.choices[0]["message"]
                else None
            )
            return LLMResponse(
                api_response=response, raw_output=content, function_call=call_func
            )
        except Exception as e:
            if response is not None:
                return LLMResponse(api_response=response, error=True, error_log=str(e))
            else:
                return LLMResponse(api_response=None, error=True, error_log=str(e))

    def stream(
        self,
        messages: List[Dict[str, str]],  # input
        functions: List[Any] = [],
        model: Optional[str] = DEFAULT_MODEL,
        *args,
        **kwargs,
    ) -> Generator[LLMStreamResponse, None, None]:
        """Stream openai chat completion."""
        response = None
        try:
            # load_prompt()
            start_time = datetime.datetime.now()
            response = completion(
                model=model,
                messages=[
                    message.model_dump(exclude_none=True)
                    for message in self.__validate_openai_messages(messages)
                ],
                stream=True,
                functions=functions,
            )

            for chunk in self.__llm_stream_response_generator__(
                messages, response, start_time, functions
            ):
                yield chunk
        except Exception as e:
            yield LLMStreamResponse(error=True, error_log=str(e))

    async def astream(
        self,
        messages: List[Dict[str, str]],
        functions: List[Any] = [],
        model: Optional[str] = DEFAULT_MODEL,
        *args,
        **kwargs,
    ) -> AsyncGenerator[LLMStreamResponse, None]:
        """Parse & stream output from openai chat completion."""
        response = None
        try:
            start_time = datetime.datetime.now()
            response = await acompletion(
                model=model,
                messages=[
                    message.model_dump(exclude_none=True)
                    for message in self.__validate_openai_messages(messages)
                ],
                stream=True,
                functions=functions,
            )

            async for chunk in self.__llm_stream_response_agenerator__(
                messages, response, start_time, functions
            ):
                yield chunk
        except Exception as e:
            yield LLMStreamResponse(error=True, error_log=str(e))

    def run_and_parse(
        self,
        messages: List[Dict[str, str]],
        parsing_type: Optional[ParsingType] = None,
        functions: List[Any] = [],
        output_keys: Optional[List[str]] = None,
        model: Optional[str] = DEFAULT_MODEL,
    ) -> LLMResponse:
        """Parse and return output from openai chat completion."""
        response = None
        parsed_success = True
        parse_result = None
        error_log = None
        try:
            response = completion(
                model=model,
                messages=[
                    message.model_dump(exclude_none=True)
                    for message in self.__validate_openai_messages(messages)
                ],
                functions=functions,
            )
            raw_output = response.choices[0]["message"]["content"]

            call_func = (
                response.choices[0]["message"]["function_call"]
                if "function_call" in response.choices[0]["message"]
                else None
            )
            if not call_func:
                # function call does not appear in output

                parse_result: ParseResult = self.__parse_output_pattern__(
                    raw_output, parsing_type
                )

                # if output_keys exist & parsed_outputs does not match with output_keys -> error
                # if parse_result.error -> error
                if (
                    output_keys is not None
                    and set(parse_result.parsed_outputs.keys()) != set(output_keys)
                ) or parse_result.error:
                    parsed_success = False
                    error_log = (
                        "Output keys do not match with parsed output keys"
                        if not parse_result.error_log
                        else parse_result.error_log
                    )

            return LLMResponse(
                api_response=response,
                raw_output=raw_output,
                parsed_outputs=parse_result.parsed_outputs if parse_result else None,
                function_call=call_func,
                error=not parsed_success,
                error_log=error_log,
            )
        except Exception as e:
            if response is not None:
                return LLMResponse(api_response=response, error=True, error_log=str(e))
            else:
                return LLMResponse(api_response=None, error=True, error_log=str(e))

    async def arun_and_parse(
        self,
        messages: List[Dict[str, str]],
        parsing_type: Optional[ParsingType] = None,
        functions: List[Any] = [],
        output_keys: Optional[List[str]] = None,
        model: Optional[str] = DEFAULT_MODEL,
    ) -> LLMResponse:
        """Generate openai chat completion asynchronously, and parse the output.
        Example prompt is as follows:
        -----
        Given a topic, you are required to generate a story.
        You must follow the provided output format.

        Topic:
        {topic}

        Output format:
        [Story]
        ...
        [/Story]

        Now generate the output:
        """
        response = None
        parsed_success = True
        parse_result = None
        error_log = None
        try:
            response = await acompletion(
                model=model,
                messages=[
                    message.model_dump(exclude_none=True)
                    for message in self.__validate_openai_messages(messages)
                ],
                functions=functions,
            )
            raw_output = response.choices[0]["message"]["content"]
            call_func = (
                response.choices[0]["message"]["function_call"]
                if "function_call" in response.choices[0]["message"]
                else None
            )

            if not call_func:
                # function call does not appear in output

                parse_result: ParseResult = self.__parse_output_pattern__(
                    raw_output, parsing_type
                )

                # if output_keys exist & parsed_outputs does not match with output_keys -> error
                # if parse_result.error -> error
                if (
                    output_keys is not None
                    and set(parse_result.parsed_outputs.keys()) != set(output_keys)
                ) or parse_result.error:
                    parsed_success = False
                    error_log = (
                        "Output keys do not match with parsed output keys"
                        if not parse_result.error_log
                        else parse_result.error_log
                    )

            return LLMResponse(
                api_response=response,
                raw_output=raw_output,
                parsed_outputs=parse_result.parsed_outputs if parse_result else None,
                function_call=call_func,
                error=not parsed_success,
                error_log=error_log,
            )
        except Exception as e:
            if response is not None:
                return LLMResponse(api_response=response, error=True, error_log=str(e))
            else:
                return LLMResponse(api_response=None, error=True, error_log=str(e))

    def stream_and_parse(
        self,
        messages: List[Dict[str, str]],
        parsing_type: Optional[ParsingType] = None,
        functions: List[Any] = [],
        output_keys: Optional[List[str]] = None,
        model: Optional[str] = DEFAULT_MODEL,
        **kwargs,
    ) -> Generator[LLMStreamResponse, None, None]:
        """Parse & stream output from openai chat completion."""
        response = None
        try:
            if parsing_type == ParsingType.COLON.value:
                # cannot stream colon type
                yield LLMStreamResponse(
                    error=True, error_log="Cannot stream colon type"
                )
                return
            start_time = datetime.datetime.now()
            response = completion(
                model=model,
                messages=[
                    message.model_dump(exclude_none=True)
                    for message in self.__validate_openai_messages(messages)
                ],
                stream=True,
                functions=functions,
            )

            parsed_outputs = {}
            error_occurs = False
            error_log = None

            if len(functions) > 0:
                # if function exists, cannot parsing in stream time
                # just stream raw output and parse after stream
                streamed_outputs = {
                    "content": "",
                    "function_call": None,
                    "api_response": None,
                }
                response_with_api_res = None
                for chunk in self.__llm_stream_response_generator__(
                    messages, response, start_time, functions
                ):
                    if chunk.raw_output:
                        streamed_outputs["content"] += chunk.raw_output
                    if chunk.function_call:
                        streamed_outputs["function_call"] = chunk.function_call
                    if (
                        chunk.api_response
                        and "delta" not in chunk.api_response["choices"][0]
                    ):  # only get the last api_response, not delta response
                        streamed_outputs["api_response"] = chunk.api_response
                        response_with_api_res = chunk
                    else:
                        yield chunk

                    if chunk.error and not error_occurs:
                        error_occurs = True
                        error_log = chunk.error_log

                if not streamed_outputs["function_call"]:
                    # if function call does not exist in output
                    # able to parse
                    parse_result: ParseResult = self.__parse_output_pattern__(
                        streamed_outputs["content"], parsing_type
                    )

                    error_occurs = parse_result.error or error_occurs
                    error_log = parse_result.error_log if not error_log else error_log

                    if (
                        output_keys is not None
                        and set(parse_result.parsed_outputs.keys()) != set(output_keys)
                    ) or error_occurs:
                        error_occurs = True
                        error_log = (
                            "Output keys do not match with parsed output keys"
                            if not error_log
                            else error_log
                        )
                        yield LLMStreamResponse(
                            api_response=streamed_outputs["api_response"],
                            error=True,
                            error_log=error_log,
                        )
                    else:
                        response_with_api_res.parsed_outputs = (
                            parse_result.parsed_outputs
                        )
                        yield response_with_api_res
                else:
                    yield response_with_api_res
            else:
                if parsing_type is None:
                    for chunk in self.__llm_stream_response_generator__(
                        messages, response, start_time, functions
                    ):
                        yield chunk

                        if chunk.error and not error_occurs:
                            error_occurs = True
                            error_log = chunk.error_log

                elif parsing_type == ParsingType.DOUBLE_SQUARE_BRACKET.value:
                    for chunk in self.__double_type_sp_generator__(
                        messages, response, parsing_type, start_time, functions
                    ):
                        yield chunk
                        if chunk.parsed_outputs:
                            parsed_outputs = update_dict(
                                parsed_outputs, chunk.parsed_outputs
                            )
                        if chunk.error and not error_occurs:
                            error_occurs = True
                            error_log = chunk.error_log
                else:
                    for chunk in self.__single_type_sp_generator__(
                        messages, response, parsing_type, start_time
                    ):
                        yield chunk
                        if chunk.parsed_outputs:
                            parsed_outputs = update_dict(
                                parsed_outputs, chunk.parsed_outputs
                            )
                        if chunk.error and not error_occurs:
                            error_occurs = True
                            error_log = chunk.error_log

                if (
                    output_keys is not None
                    and set(parsed_outputs.keys()) != set(output_keys)
                ) and not error_occurs:
                    error_occurs = True
                    error_log = "Output keys do not match with parsed output keys"
                    yield LLMStreamResponse(error=True, error_log=error_log)

        except Exception as e:
            yield LLMStreamResponse(error=True, error_log=str(e))

    async def astream_and_parse(
        self,
        messages: List[Dict[str, str]],
        parsing_type: Optional[ParsingType] = None,
        functions: List[Any] = [],
        output_keys: Optional[List[str]] = None,
        model: Optional[str] = DEFAULT_MODEL,
    ) -> AsyncGenerator[LLMStreamResponse, None]:
        """Parse & stream output from openai chat completion."""
        response = None
        try:
            if parsing_type == ParsingType.COLON.value:
                # cannot stream colon type
                yield LLMStreamResponse(
                    error=True, error_log="Cannot stream colon type"
                )
                return
            start_time = datetime.datetime.now()
            response = await acompletion(
                model=model,
                messages=[
                    message.model_dump(exclude_none=True)
                    for message in self.__validate_openai_messages(messages)
                ],
                stream=True,
                functions=functions,
            )

            parsed_outputs = {}
            error_occurs = False  # error in stream time
            error_log = None
            if len(functions) > 0:
                # if function exists, cannot parsing in stream time
                # just stream raw output and parse after stream
                streamed_outputs = {
                    "content": "",
                    "function_call": None,
                    "api_response": None,
                }
                response_with_api_res = None
                async for chunk in self.__llm_stream_response_agenerator__(
                    messages, response, start_time, functions
                ):
                    if chunk.raw_output:
                        streamed_outputs["content"] += chunk.raw_output
                    if chunk.function_call:
                        streamed_outputs["function_call"] = chunk.function_call
                    if (
                        chunk.api_response
                        and "delta" not in chunk.api_response["choices"][0]
                    ):
                        streamed_outputs["api_response"] = chunk.api_response
                        response_with_api_res = chunk
                    else:
                        yield chunk

                    if chunk.error and not error_occurs:
                        error_occurs = True
                        error_log = chunk.error_log

                if not streamed_outputs["function_call"]:
                    # if function call does not exist in output
                    # able to parse
                    parse_result: ParseResult = self.__parse_output_pattern__(
                        streamed_outputs["content"], parsing_type
                    )

                    error_occurs = parse_result.error or error_occurs
                    error_log = parse_result.error_log if not error_log else error_log
                    if (
                        output_keys is not None
                        and set(parse_result.parsed_outputs.keys()) != set(output_keys)
                    ) or error_occurs:
                        error_occurs = True
                        error_log = (
                            "Output keys do not match with parsed output keys"
                            if not error_log
                            else error_log
                        )
                        yield LLMStreamResponse(
                            api_response=streamed_outputs["api_response"],
                            error=True,
                            error_log=error_log,
                        )
                    else:
                        response_with_api_res.parsed_outputs = (
                            parse_result.parsed_outputs
                        )
                        yield response_with_api_res
                else:
                    yield response_with_api_res
            else:
                if parsing_type is None:
                    async for chunk in self.__llm_stream_response_agenerator__(
                        messages, response, start_time, functions
                    ):
                        yield chunk

                        if chunk.error and not error_occurs:
                            error_occurs = True
                            error_log = chunk.error_log

                elif parsing_type == ParsingType.DOUBLE_SQUARE_BRACKET.value:
                    async for chunk in self.__double_type_sp_agenerator__(
                        messages, response, parsing_type, start_time, functions
                    ):
                        yield chunk
                        if chunk.parsed_outputs:
                            parsed_outputs = update_dict(
                                parsed_outputs, chunk.parsed_outputs
                            )
                        if chunk.error and not error_occurs:
                            error_occurs = True
                else:
                    async for chunk in self.__single_type_sp_agenerator__(
                        messages, response, parsing_type, start_time, functions
                    ):
                        yield chunk
                        if chunk.parsed_outputs:
                            parsed_outputs = update_dict(
                                parsed_outputs, chunk.parsed_outputs
                            )
                        if chunk.error and not error_occurs:
                            error_occurs = True

                if (
                    output_keys is not None
                    and set(parsed_outputs.keys()) != set(output_keys)
                ) and not error_occurs:
                    error_occurs = True
                    error_log = "Output keys do not match with parsed output keys"
                    yield LLMStreamResponse(error=True, error_log=error_log)

        except Exception as e:
            yield LLMStreamResponse(error=True, error_log=str(e))

    def make_model_response(
        self,
        chunk: dict,
        response_ms,
        messages: List[Dict[str, str]],
        raw_output: str,
        function_list: List[Any] = [],
        function_call: Optional[dict] = None,
    ) -> ModelResponse:
        count_start_time = datetime.datetime.now()
        prompt_token: int = num_tokens_for_messages(
            messages=messages, model=chunk["model"]
        )
        completion_token: int = num_tokens_for_messages(
            model=chunk["model"],
            messages=[{"role": "assistant", "content": raw_output}],
        )

        if len(function_list) > 0:
            function_list_token = num_tokens_from_functions_input(
                functions=function_list, model=chunk["model"]
            )
            prompt_token += function_list_token

        if function_call:
            function_call_token = num_tokens_from_function_call_output(
                function_call_output=function_call, model=chunk["model"]
            )
            completion_token += function_call_token

        count_end_time = datetime.datetime.now()
        logger.debug(
            f"counting token time : {(count_end_time - count_start_time).total_seconds() * 1000} ms"
        )

        usage = {
            "prompt_tokens": prompt_token,
            "completion_tokens": completion_token,
            "total_tokens": prompt_token + completion_token,
        }
        res = ModelResponse(
            id=chunk["id"],
            created=chunk["created"],
            model=chunk["model"],
            usage=usage,
            response_ms=response_ms,
        )
        res["choices"][0]["finish_reason"] = chunk["choices"][0]["finish_reason"]
        res["choices"][0]["message"]["content"] = (
            raw_output if raw_output != "" else None
        )
        res["response_ms"] = response_ms
        if function_call:
            res.choices[0]["message"]["function_call"] = function_call
        return res

    def __llm_stream_response_generator__(
        self,
        messages: List[Dict[str, str]],
        response: Generator,
        start_time: datetime.datetime,
        functions: List[Any] = [],
    ) -> Generator[LLMStreamResponse, None, None]:
        raw_output = ""
        function_call = {"name": "", "arguments": ""}
        try:
            yield_api_response_with_fc = False
            for chunk in response:
                yield_api_response_with_fc = False
                if (
                    "function_call" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["function_call"] is not None
                ):
                    for key, value in chunk["choices"][0]["delta"][
                        "function_call"
                    ].items():
                        function_call[key] += value

                    yield LLMStreamResponse(
                        api_response=chunk,
                        function_call=chunk["choices"][0]["delta"]["function_call"],
                    )
                    yield_api_response_with_fc = True

                if (
                    "content" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["content"] is not None
                ):
                    raw_output += chunk["choices"][0]["delta"]["content"]
                    yield LLMStreamResponse(
                        api_response=chunk if not yield_api_response_with_fc else None,
                        raw_output=chunk["choices"][0]["delta"]["content"],
                    )

                if chunk["choices"][0]["finish_reason"] != None:
                    end_time = datetime.datetime.now()
                    response_ms = (end_time - start_time).total_seconds() * 1000
                    yield LLMStreamResponse(
                        api_response=self.make_model_response(
                            chunk,
                            response_ms,
                            messages,
                            raw_output,
                            function_list=functions,
                            function_call=function_call
                            if chunk["choices"][0]["finish_reason"] == "function_call"
                            else None,
                        )
                    )
        except Exception as e:
            logger.error(e)
            yield LLMStreamResponse(error=True, error_log=str(e))

    def __single_type_sp_generator__(
        self,
        messages: List[Dict[str, str]],
        response: Generator,
        parsing_type: ParsingType,
        start_time: datetime.datetime,
        functions: List[Any] = [],
    ) -> Generator[LLMStreamResponse, None, None]:
        try:
            parsing_pattern = get_pattern_by_type(parsing_type)
            start_tag = parsing_pattern["start"]
            start_fstring = parsing_pattern["start_fstring"]
            end_fstring = parsing_pattern["end_fstring"]
            start_token = parsing_pattern["start_token"]
            end_token = parsing_pattern["end_token"]

            buffer = ""
            raw_output = ""
            active_key = None
            stream_pause = False
            end_tag = None
            function_call = {"name": "", "arguments": ""}
            yield_api_response_with_fc = False
            for chunk in response:
                yield_api_response_with_fc = False
                if (
                    "function_call" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["function_call"] is not None
                ):
                    for key, value in chunk["choices"][0]["delta"][
                        "function_call"
                    ].items():
                        function_call[key] += value

                    yield LLMStreamResponse(
                        api_response=chunk,
                        function_call=chunk["choices"][0]["delta"]["function_call"],
                    )
                    yield_api_response_with_fc = True

                if (
                    "content" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["content"] is not None
                ):
                    stream_value: str = chunk["choices"][0]["delta"]["content"]
                    raw_output += stream_value
                    yield LLMStreamResponse(
                        api_response=chunk if not yield_api_response_with_fc else None,
                        raw_output=stream_value,
                    )

                    buffer += stream_value
                    while True:
                        if active_key is None:
                            keys = re.findall(start_tag, buffer, flags=re.DOTALL)
                            if len(keys) == 0:
                                break  # no key
                            active_key, active_type = keys[
                                0
                            ]  # Updated to unpack both key and type
                            end_tag = end_fstring.format(key=active_key)
                            # delete start tag from buffer
                            start_pattern = start_fstring.format(
                                key=active_key, type=active_type
                            )
                            buffer = buffer.split(start_pattern)[-1]
                        else:
                            if (
                                stream_value.find(start_token) != -1
                            ):  # start token appers in chunk -> pause
                                stream_pause = True
                                break
                            elif stream_pause:
                                if (
                                    buffer.find(end_tag) != -1
                                ):  # if end tag appears in buffer
                                    yield LLMStreamResponse(
                                        parsed_outputs={
                                            active_key: buffer.split(end_tag)[
                                                0
                                            ].replace(end_tag, "")
                                        }
                                    )
                                    buffer = buffer.split(end_tag)[-1]
                                    active_key = None
                                    stream_pause = False
                                elif (
                                    stream_value.find(end_token) != -1
                                ):  # if pattern ends  = ("[blah]" != end_pattern) appeared in buffer
                                    if (
                                        active_type == "List"
                                        or active_type == "Dict"
                                        and end_token.find("]") != -1
                                    ):
                                        try:
                                            buffer_dict = json.loads(buffer)
                                            stream_pause = False
                                            continue
                                        except Exception as exception:
                                            logger.error(exception)
                                            yield LLMStreamResponse(
                                                error=True,
                                                error_log="Parsing error : Invalid end tag detected",
                                                parsed_outputs={
                                                    active_key: buffer.split(
                                                        start_token
                                                    )[0]
                                                },
                                            )
                                            stream_pause = False
                                            buffer = ""
                                    yield LLMStreamResponse(
                                        error=True,
                                        error_log="Parsing error : Invalid end tag detected",
                                        parsed_outputs={active_key: buffer},
                                    )
                                    stream_pause = False
                                    buffer = ""
                                break
                            else:
                                # no start token, no stream_pause (not inside of tag)
                                if buffer:
                                    yield LLMStreamResponse(
                                        parsed_outputs={active_key: buffer}
                                    )
                                    buffer = ""
                                break

                if chunk["choices"][0]["finish_reason"] != None:
                    end_time = datetime.datetime.now()
                    response_ms = (end_time - start_time).total_seconds() * 1000
                    yield LLMStreamResponse(
                        api_response=self.make_model_response(
                            chunk,
                            response_ms,
                            messages,
                            raw_output,
                            function_list=functions,
                            function_call=function_call
                            if chunk["choices"][0]["finish_reason"] == "function_call"
                            else None,
                        )
                    )
        except Exception as e:
            logger.error(e)
            yield LLMStreamResponse(error=True, error_log=str(e))

    def __double_type_sp_generator__(
        self,
        messages: List[Dict[str, str]],
        response: Generator,
        parsing_type: ParsingType,
        start_time: datetime.datetime,
        functions: List[Any] = [],
    ) -> Generator[LLMStreamResponse, None, None]:
        try:
            parsing_pattern = get_pattern_by_type(parsing_type)
            start_tag = parsing_pattern["start"]
            start_fstring = parsing_pattern["start_fstring"]
            end_fstring = parsing_pattern["end_fstring"]
            start_token = parsing_pattern["start_token"]
            end_token = parsing_pattern["end_token"]

            buffer = ""
            raw_output = ""
            active_key = None
            stream_pause = False
            end_tag = None
            function_call = {"name": "", "arguments": ""}
            yield_api_response_with_fc = False
            for chunk in response:
                yield_api_response_with_fc = False
                if (
                    "function_call" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["function_call"] is not None
                ):
                    for key, value in chunk["choices"][0]["delta"][
                        "function_call"
                    ].items():
                        function_call[key] += value

                    yield LLMStreamResponse(
                        api_response=chunk,
                        function_call=chunk["choices"][0]["delta"]["function_call"],
                    )
                    yield_api_response_with_fc = True

                if (
                    "content" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["content"] is not None
                ):
                    stream_value: str = chunk["choices"][0]["delta"]["content"]
                    raw_output += stream_value
                    yield LLMStreamResponse(
                        api_response=chunk if not yield_api_response_with_fc else None,
                        raw_output=stream_value,
                    )

                    buffer += stream_value

                    while True:
                        if active_key is None:
                            keys = re.findall(start_tag, buffer, flags=re.DOTALL)
                            if len(keys) == 0:
                                break  # no key
                            active_key, active_type = keys[0]
                            end_tag = end_fstring.format(key=active_key)
                            # delete start tag from buffer
                            start_pattern = start_fstring.format(
                                key=active_key, type=active_type
                            )
                            buffer = buffer.split(start_pattern)[-1]

                        else:
                            if (
                                stream_value.find(start_token) != -1
                            ):  # start token appers in chunk -> pause
                                stream_pause = True
                                break
                            elif stream_pause:
                                if (
                                    buffer.find(end_tag) != -1
                                ):  # if end tag appears in buffer
                                    yield LLMStreamResponse(
                                        parsed_outputs={
                                            active_key: buffer.split(end_tag)[0]
                                        }
                                    )
                                    buffer = buffer.split(end_tag)[-1]
                                    active_key = None
                                    stream_pause = False
                                elif (
                                    stream_value.find(end_token) != -1
                                ):  # if ("[blah]" != end_pattern) appeared in buffer
                                    if (
                                        buffer.find(end_token + end_token) != -1
                                    ):  # if ]] in buffer -> error
                                        yield LLMStreamResponse(
                                            error=True,
                                            error_log="Parsing error : Invalid end tag detected",
                                            parsed_outputs={
                                                active_key: buffer.split(start_token)[0]
                                            },
                                        )
                                        buffer = buffer.split(end_token + end_token)[-1]
                                        stream_pause = False
                                        break
                                    else:
                                        if (
                                            buffer.find(start_token + start_token) != -1
                                        ):  # if [[ in buffer -> pause
                                            break
                                        else:
                                            # if [ in buffer (== [blah]) -> stream
                                            yield LLMStreamResponse(
                                                parsed_outputs={active_key: buffer}
                                            )
                                            buffer = ""
                                            stream_pause = False
                                            break
                                break
                            else:
                                # no start token, no stream_pause (not inside of tag)
                                if buffer:
                                    yield LLMStreamResponse(
                                        parsed_outputs={active_key: buffer}
                                    )
                                    buffer = ""
                                break

                if chunk["choices"][0]["finish_reason"] != None:
                    end_time = datetime.datetime.now()
                    response_ms = (end_time - start_time).total_seconds() * 1000
                    yield LLMStreamResponse(
                        api_response=self.make_model_response(
                            chunk,
                            response_ms,
                            messages,
                            raw_output,
                            function_list=functions,
                            function_call=function_call
                            if chunk["choices"][0]["finish_reason"] == "function_call"
                            else None,
                        )
                    )
        except Exception as e:
            logger.error(e)
            yield LLMStreamResponse(error=True, error_log=str(e))

    async def __llm_stream_response_agenerator__(
        self,
        messages: List[Dict[str, str]],
        response: AsyncGenerator,
        start_time: datetime.datetime,
        functions: List[Any] = [],
    ) -> AsyncGenerator[LLMStreamResponse, None]:
        raw_output = ""
        function_call = {"name": "", "arguments": ""}
        try:
            yield_api_response_with_fc = False
            async for chunk in response:
                yield_api_response_with_fc = False
                if (
                    "function_call" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["function_call"] is not None
                ):
                    for key, value in chunk["choices"][0]["delta"][
                        "function_call"
                    ].items():
                        function_call[key] += value

                    yield LLMStreamResponse(
                        api_response=chunk,
                        function_call=chunk["choices"][0]["delta"]["function_call"],
                    )
                    yield_api_response_with_fc = True

                if (
                    "content" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["content"] is not None
                ):
                    stream_value: str = chunk["choices"][0]["delta"]["content"]
                    raw_output += stream_value
                    yield LLMStreamResponse(
                        api_response=chunk if not yield_api_response_with_fc else None,
                        raw_output=stream_value,
                    )

                if chunk["choices"][0]["finish_reason"] != None:
                    end_time = datetime.datetime.now()
                    response_ms = (end_time - start_time).total_seconds() * 1000
                    yield LLMStreamResponse(
                        api_response=self.make_model_response(
                            chunk,
                            response_ms,
                            messages,
                            raw_output,
                            function_list=functions,
                            function_call=function_call
                            if chunk["choices"][0]["finish_reason"] == "function_call"
                            else None,
                        )
                    )
        except Exception as e:
            logger.error(e)
            yield LLMStreamResponse(error=True, error_log=str(e))

    async def __single_type_sp_agenerator__(
        self,
        messages: List[Dict[str, str]],
        response: AsyncGenerator,
        parsing_type: ParsingType,
        start_time: datetime.datetime,
        functions: List[Any] = [],
    ) -> AsyncGenerator[LLMStreamResponse, None]:
        try:
            parsing_pattern = get_pattern_by_type(parsing_type)
            start_tag = parsing_pattern["start"]
            start_fstring = parsing_pattern["start_fstring"]
            end_fstring = parsing_pattern["end_fstring"]
            start_token = parsing_pattern["start_token"]
            end_token = parsing_pattern["end_token"]

            buffer = ""
            raw_output = ""
            active_key = None
            stream_pause = False
            end_tag = None
            function_call = {"name": "", "arguments": ""}
            yield_api_response_with_fc = False
            async for chunk in response:
                yield_api_response_with_fc = False
                if (
                    "function_call" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["function_call"] is not None
                ):
                    for key, value in chunk["choices"][0]["delta"][
                        "function_call"
                    ].items():
                        function_call[key] += value

                    yield LLMStreamResponse(
                        api_response=chunk,
                        function_call=chunk["choices"][0]["delta"]["function_call"],
                    )
                    yield_api_response_with_fc = True

                if (
                    "content" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["content"] is not None
                ):
                    stream_value: str = chunk["choices"][0]["delta"]["content"]
                    raw_output += stream_value
                    yield LLMStreamResponse(
                        api_response=chunk if not yield_api_response_with_fc else None,
                        raw_output=stream_value,
                    )

                    buffer += stream_value

                    while True:
                        if active_key is None:
                            keys = re.findall(start_tag, buffer, flags=re.DOTALL)
                            if len(keys) == 0:
                                break  # no key

                            active_key, active_type = keys[
                                0
                            ]  # Updated to unpack both key and type
                            end_tag = end_fstring.format(key=active_key)
                            # delete start tag from buffer
                            start_pattern = start_fstring.format(
                                key=active_key, type=active_type
                            )
                            buffer = buffer.split(start_pattern)[-1]

                        else:
                            if (
                                stream_value.find(start_token) != -1
                            ):  # start token appers in chunk -> pause
                                stream_pause = True
                                break
                            elif stream_pause:
                                if (
                                    buffer.find(end_tag) != -1
                                ):  # if end tag appears in buffer
                                    yield LLMStreamResponse(
                                        parsed_outputs={
                                            active_key: buffer.split(end_tag)[
                                                0
                                            ].replace(end_tag, "")
                                        }
                                    )
                                    buffer = buffer.split(end_tag)[-1]
                                    active_key = None
                                    stream_pause = False
                                elif (
                                    stream_value.find(end_token) != -1
                                ):  # if pattern ends  = ("[blah]" != end_pattern) appeared in buffer
                                    if (
                                        active_type == "List"
                                        or active_type == "Dict"
                                        and end_token.find("]") != -1
                                    ):
                                        try:
                                            buffer_dict = json.loads(buffer)
                                            stream_pause = False
                                            continue
                                        except Exception as exception:
                                            logger.error(exception)
                                            yield LLMStreamResponse(
                                                error=True,
                                                error_log="Parsing error : Invalid end tag detected",
                                                parsed_outputs={
                                                    active_key: buffer.split(
                                                        start_token
                                                    )[0]
                                                },
                                            )
                                            stream_pause = False
                                            buffer = ""
                                    yield LLMStreamResponse(
                                        error=True,
                                        error_log="Parsing error : Invalid end tag detected",
                                        parsed_outputs={active_key: buffer},
                                    )
                                    stream_pause = False
                                    buffer = ""
                                break
                            else:
                                # no start token, no stream_pause (not inside of tag)
                                if buffer:
                                    yield LLMStreamResponse(
                                        parsed_outputs={active_key: buffer}
                                    )
                                    buffer = ""
                                break

                if chunk["choices"][0]["finish_reason"] != None:
                    end_time = datetime.datetime.now()
                    response_ms = (end_time - start_time).total_seconds() * 1000
                    yield LLMStreamResponse(
                        api_response=self.make_model_response(
                            chunk,
                            response_ms,
                            messages,
                            raw_output,
                            function_list=functions,
                            function_call=function_call
                            if chunk["choices"][0]["finish_reason"] == "function_call"
                            else None,
                        )
                    )
        except Exception as e:
            logger.error(e)
            yield LLMStreamResponse(error=True, error_log=str(e))

    async def __double_type_sp_agenerator__(
        self,
        messages: List[Dict[str, str]],
        response: AsyncGenerator,
        parsing_type: ParsingType,
        start_time: datetime.datetime,
        functions: List[Any] = [],
    ) -> AsyncGenerator[LLMStreamResponse, None]:
        try:
            parsing_pattern = get_pattern_by_type(parsing_type)
            start_tag = parsing_pattern["start"]
            start_fstring = parsing_pattern["start_fstring"]
            end_fstring = parsing_pattern["end_fstring"]
            start_token = parsing_pattern["start_token"]
            end_token = parsing_pattern["end_token"]

            buffer = ""
            raw_output = ""
            active_key = None
            stream_pause = False
            end_tag = None
            function_call = {"name": "", "arguments": ""}
            yield_api_response_with_fc = False
            async for chunk in response:
                yield_api_response_with_fc = False
                if (
                    "function_call" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["function_call"] is not None
                ):
                    for key, value in chunk["choices"][0]["delta"][
                        "function_call"
                    ].items():
                        function_call[key] += value

                    yield LLMStreamResponse(
                        api_response=chunk,
                        function_call=chunk["choices"][0]["delta"]["function_call"],
                    )
                    yield_api_response_with_fc = True

                if (
                    "content" in chunk["choices"][0]["delta"]
                    and chunk["choices"][0]["delta"]["content"] is not None
                ):
                    stream_value: str = chunk["choices"][0]["delta"]["content"]
                    raw_output += stream_value
                    yield LLMStreamResponse(
                        api_response=chunk if not yield_api_response_with_fc else None,
                        raw_output=stream_value,
                    )

                    buffer += stream_value

                    while True:
                        if active_key is None:
                            keys = re.findall(start_tag, buffer, flags=re.DOTALL)
                            # if len(keys) > 1:
                            #     yield LLMStreamResponse(
                            #         error=True,
                            #         error_log="Parsing error : Nested key detected",
                            #     )
                            #     break
                            if len(keys) == 0:
                                break  # no key
                            active_key, active_type = keys[0]
                            end_tag = end_fstring.format(key=active_key)
                            # delete start tag from buffer
                            start_pattern = start_fstring.format(
                                key=active_key, type=active_type
                            )
                            buffer = buffer.split(start_pattern)[-1]

                        else:
                            if (
                                stream_value.find(start_token) != -1
                            ):  # start token appers in chunk -> pause
                                stream_pause = True
                                break
                            elif stream_pause:
                                if (
                                    buffer.find(end_tag) != -1
                                ):  # if end tag appears in buffer
                                    yield LLMStreamResponse(
                                        parsed_outputs={
                                            active_key: buffer.split(end_tag)[0]
                                        }
                                    )
                                    buffer = buffer.split(end_tag)[-1]
                                    active_key = None
                                    stream_pause = False
                                    # break
                                elif (
                                    stream_value.find(end_token) != -1
                                ):  # if ("[blah]" != end_pattern) appeared in buffer
                                    if (
                                        buffer.find(end_token + end_token) != -1
                                    ):  # if ]] in buffer -> error
                                        yield LLMStreamResponse(
                                            error=True,
                                            error_log="Parsing error : Invalid end tag detected",
                                            parsed_outputs={
                                                active_key: buffer.split(start_token)[0]
                                            },
                                        )
                                        buffer = buffer.split(end_token + end_token)[-1]
                                        stream_pause = False
                                        break
                                    else:
                                        if (
                                            buffer.find(start_token + start_token) != -1
                                        ):  # if [[ in buffer -> pause
                                            break
                                        else:
                                            # if [ in buffer (== [blah]) -> stream
                                            yield LLMStreamResponse(
                                                parsed_outputs={active_key: buffer}
                                            )
                                            buffer = ""
                                            stream_pause = False
                                            break
                                break
                            else:
                                # no start token, no stream_pause (not inside of tag)
                                if buffer:
                                    yield LLMStreamResponse(
                                        parsed_outputs={active_key: buffer}
                                    )
                                    buffer = ""
                                break

                if chunk["choices"][0]["finish_reason"] != None:
                    end_time = datetime.datetime.now()
                    response_ms = (end_time - start_time).total_seconds() * 1000
                    yield LLMStreamResponse(
                        api_response=self.make_model_response(
                            chunk,
                            response_ms,
                            messages,
                            raw_output,
                            function_list=functions,
                            function_call=function_call
                            if chunk["choices"][0]["finish_reason"] == "function_call"
                            else None,
                        )
                    )
        except Exception as e:
            logger.error(e)
            yield LLMStreamResponse(error=True, error_log=str(e))
