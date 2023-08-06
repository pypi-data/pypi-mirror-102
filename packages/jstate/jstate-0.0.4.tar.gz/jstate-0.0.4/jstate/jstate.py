import os, json


class JState:
    def __init__(self, file: str, default=None):
        if default is None:
            default = {}
        self.file = file
        self.default = default

    def read(self) -> dict:
        if not os.path.exists(self.file):
            self.write(self.default)
            return self.default

        with open(self.file, 'r') as f:
            return json.loads(f.read())

    def write(self, state: dict):
        with open(self.file, 'w') as f:
            f.write(json.dumps(state))