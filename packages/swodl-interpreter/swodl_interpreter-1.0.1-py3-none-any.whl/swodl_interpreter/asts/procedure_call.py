from swodl_interpreter.inbuild_functions import functions
from swodl_interpreter.storage import Scope
from swodl_interpreter.asts.struct import ArrayType


class ProcedureCall:
    def __init__(self, proc_name, actual_params, token, url):
        self.proc_name = proc_name
        self.actual_params = actual_params
        self.token = token
        self.url = url
        # self.proc_symbol = None

    def visit(self, scope: Scope):
        if self.proc_name in functions:
            func = functions[self.proc_name]
        elif self.url != None:
            func = Scope.web_resolver.get(
                self.url.visit(scope), self.proc_name)
        args = []
        for x in self.actual_params:
            # TODO: refactor! remove this if. Should be normal array
            if type(x) == ArrayType:
                args.append([y.visit(scope) for y in x])
            else:
                args.append(x.visit(scope))
        try:
            return func(*args)
        except Exception as e:
            raise e
