from swodl_interpreter.storage import Scope


class Label:
    def __init__(self, name):
        self.name = name
        Scope.labels.update({name: None})

    def visit(self, _=None):
        pass
