from swodl_interpreter.storage import Scope
from swodl_interpreter.inbuild_functions import functions


def add_empty_func(name, functions=functions, args=None):
    def func(): return ''
    func.args = [x.value for x in args] if args else []
    func.__name__ = name
    functions.update({name: func})


class FunctionDecl:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params  # a list of Param nodes
        self.body = body
        add_empty_func(self.name, functions, self.params)

    def visit(self, scope: Scope):
        name = self.name
        if name not in scope.functions:
            scope.functions[name] = []

        def func(*args):
            func_scope = Scope()
            for n, v in zip([x.value for x in self.params], args):
                func_scope.Global[n] = v
            scope.functions[name].append(func_scope)
            for _ in self.body.visit(func_scope):
                pass
            return func_scope.Global['__return_func']

        func.__name__ = name
        functions[name] = func
