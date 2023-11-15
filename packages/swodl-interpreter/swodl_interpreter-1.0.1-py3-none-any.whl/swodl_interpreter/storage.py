import json

class Scope:
    sub_calls = {}
    labels = {}
    web_type = {}
    web_resolver = None
    include_dir = None
    indent = 0

    def __init__(self) -> None:
        self.Global = {
            '_RetryDelay': 0.1,
            '_STATUS': None,
        }  # TODO: Add System Variables. Doc page 16
        self.functions = {}
        self.const = []

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return json.dumps(self.Global)
