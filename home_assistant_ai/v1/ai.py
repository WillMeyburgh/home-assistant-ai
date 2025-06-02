import os
from typing import Any, Optional
from google.genai import Client, types, errors

from home_assistant_ai.v1.home_assistant import HomeAssistant

class AI:
    def __init__(self, home_assistant: HomeAssistant):
        self.client = Client(api_key=os.environ['GEMINI_API_KEY'])
        self.home_assistant = home_assistant
        tools = types.Tool(function_declarations=self.home_assistant.define_functions())
        self.config = types.GenerateContentConfig(tools=[tools])

    def ask(self, content: Any) -> Optional[str]:
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[content],
                config=self.config,
            )
        except errors.ServerError as e:
            if e.code == 503 or e.code == 401:
                return "Sorry I'm unavailable at the moment"
            raise e

        # Check for a function call
        if response.candidates[0].content.parts[0].function_call:
            function_call = response.candidates[0].content.parts[0].function_call
            self.home_assistant.call_function(function_call)
        else:
            return response.text