from swodl_interpreter.inbuild_functions import functions
from swodl_interpreter.storage import Scope
from swodl_interpreter.asts.func_decl import add_empty_func


class DeclareWeb:
    def __init__(self, type_, method):
        self.type = type_
        self.method = method
        add_empty_func(self.method.proc_name, Scope.web_type,
                       self.method.actual_params)

    def visit(self, scope: Scope):
        name = self.method.proc_name
        if self.method.url:
            func_path = self.method.url.visit(scope)
            func = Scope.web_resolver.get(func_path, name)
            functions[name] = func
        scope.web_type[name] = self.type
