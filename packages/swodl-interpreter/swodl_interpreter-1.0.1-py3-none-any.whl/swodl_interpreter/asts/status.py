from swodl_interpreter.storage import Scope


class Status:
    def __init__(self, text):
        self.text = text

    def visit(self, scope: Scope):
        scope.Global['_STATUS'] = self.text
