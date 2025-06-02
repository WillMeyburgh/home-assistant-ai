import os
from typing import List
from homeassistant_api import Client

class HomeAssistant:
    def __init__(self):
        self.client = Client(
            os.environ['HOME_ASSISTANT_URL'],
            os.environ['HOME_ASSISTANT_TOKEN'],
        )

        self.__lights = None

    def get_lights(self):
        if self.__lights is None:
            self.__lights = {}

            states = self.client.get_states()
            for state in states:
                if 'light' in state.entity_id and 'sensor' not in state.entity_id:
                    self.__lights[state.attributes['friendly_name']] = state.entity_id
        return self.__lights
    
    def switch(self, name: str, switch: bool):
        id = self.get_lights()[name]
        self.client.trigger_service(
            id[:id.rfind('.')], 
            'turn_on' if switch else 'turn_off', 
            entity_id=id
        )

    def call_function(self, call):
        if call.name == 'switch_light':
            self.switch(**call.args)

    def define_functions(self) -> List:
        return [
            {
                "name": "switch_light",
                "description": "Turn a light on or off with it's id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "enum": list(self.get_lights().keys()),
                            "description": "The light name",
                        },
                        "switch": {
                            "type": "boolean",
                            "description": "If the light needs to be switched on or off"
                        }
                    },
                    "required": ["name", "switch"],
                },
            }
        ]