from __future__ import annotations
import asyncio

from dataclasses import dataclass
from typing import (
    Any,
    AsyncGenerator,
    Callable,
    Dict,
    Generator,
    List,
    Optional,
    Tuple,
    Union,
)
from uuid import uuid4

import promptmodel.utils.logger as logger
from promptmodel.llms.llm_proxy import LLMProxy
from promptmodel.utils.prompt_util import (
    fetch_prompts,
    run_async_in_sync,
    fetch_chat_model,
    fetch_chat_model_conversation,
)
from promptmodel.utils.types import LLMStreamResponse, LLMResponse
from promptmodel import DevClient


class RegisteringMeta(type):
    def __call__(cls, *args, **kwargs):
        instance: ChatModel = super().__call__(*args, **kwargs)
        # Find the global client instance in the current context
        client = cls.find_client_instance()
        if client is not None:
            client.register_chat_model(instance.name)
        return instance

    @staticmethod
    def find_client_instance():
        import sys

        # Get the current frame
        frame = sys._getframe(2)
        # Get global variables in the current frame
        global_vars = frame.f_globals
        # Find an instance of DevClient among global variables
        for var_name, var_val in global_vars.items():
            if isinstance(var_val, DevClient):
                return var_val
        return None


class ChatModel(metaclass=RegisteringMeta):
    def __init__(self, name: str, chat_uuid: Optional[str] = None):
        self.name = name
        if chat_uuid is None:
            chat_uuid = str(uuid4())
        self.llm_proxy = LLMProxy(name, None)

    def get_prompts(self) -> List[Dict[str, str]]:
        """Get prompt for the promptmodel.

        Returns:
            List[Dict[str, str]]: list of prompts. Each prompt is a dict with 'role' and 'content'. In the case of ChatModel, only one prompt(system prompt) is returned.
        """
        # add name to the list of prompt_models

        instruction, detail = run_async_in_sync(fetch_chat_model(self.name))
        return instruction

    def get_conv_log(self, chat_uuid: str) -> List[Dict[str, Any]]:
        """Get conversation log for the chat_uuid.

        Returns:
            List[Dict[str, Any]]: list of messages.
        """

        conversation = run_async_in_sync(fetch_chat_model_conversation(chat_uuid))
        return conversation

    def chat(
        self,
        chat_uuid: Optional[str] = None,
        inputs: Dict[str, Any] = {},
        new_messages: List[Dict[str, str]] = [],
        function_list: Optional[List[Dict[str, Any]]] = None,
        use_conv_log: bool = True,
    ) -> LLMResponse:
        """Run PromptModel. It does not raise error.

        Args:
            chat_uuid : chat_uuid for the conversation. If chat_uuid is None, new chat_uuid is generated.
            inputs (Dict[str, Any], optional): input to the instruction (system_prompt). Defaults to {}.
            new_messages (List[Dict[str, str]], optional): new messages from the user, function or else. Defaults to [].
            function_list (Optional[List[Dict[str, Any]]], optional): list of functions.
            use_conv_log (bool): If True, call LLM with conversation log. Else call LLM only with [system_prompt] + new_messages. Defaults to True.

        Returns:
            LLMResponse: response from the promptmodel. you can find raw output in response.raw_output or response.api_response['choices'][0]['message']['content'].

        Error:
            It does not raise error. If error occurs, you can check error in response.error and error_log in response.error_log.
        """
        return self.llm_proxy.chat(
            chat_uuid, inputs, new_messages, function_list, use_conv_log
        )

    async def achat(
        self,
        chat_uuid: Optional[str] = None,
        inputs: Dict[str, Any] = {},
        new_messages: List[Dict[str, str]] = [],
        function_list: Optional[List[Dict[str, Any]]] = None,
        use_conv_log: bool = True,
    ) -> LLMResponse:
        """Run PromptModel. It does not raise error.

        Args:
            chat_uuid : chat_uuid for the conversation. If chat_uuid is None, new chat_uuid is generated.
            inputs (Dict[str, Any], optional): input to the instruction (system_prompt). Defaults to {}.
            new_messages (List[Dict[str, str]], optional): new messages from the user, function or else. Defaults to [].
            function_list (Optional[List[Dict[str, Any]]], optional): list of functions.
            use_conv_log (bool): If True, call LLM with conversation log. Else call LLM only with [system_prompt] + new_messages. Defaults to True.

        Returns:
            LLMResponse: response from the promptmodel. you can find raw output in response.raw_output or response.api_response['choices'][0]['message']['content'].

        Error:
            It does not raise error. If error occurs, you can check error in response.error and error_log in response.error_log.
        """
        return await self.llm_proxy.achat(
            chat_uuid, inputs, new_messages, function_list, use_conv_log
        )
