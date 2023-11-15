from swodl_interpreter.storage import Scope


class GoToCall:
    def __init__(self, name):
        self.name = name

    def visit(self, scope: Scope):
        scope.Global['_System_GoSubLine'] = -1
        return self


class SubCall:
    def __init__(self, name):
        self.name = name
        Scope.sub_calls.update({name: None})

    def visit(self, scope: Scope):
        scope.Global['_System_GoSubLine'] = self.line
        return self
