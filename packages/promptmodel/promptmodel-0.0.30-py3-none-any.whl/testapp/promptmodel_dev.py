"""This single file is needed to build the Client development dashboard."""

from promptmodel import DevApp
from main import client as main_client

# Example imports
# from <dirname> import < objectname>

app = DevApp()

# Example usage
# This is needed to integrate your codebase with the prompt engineering dashboard

app.include_client(main_client)

app.register_sample(
    name="function_call_test/1",
    content={"user_message": "What is the weather like in Boston?"},
)

from main import get_current_weather, get_current_weather_desc

app.register_function(get_current_weather_desc, get_current_weather)
