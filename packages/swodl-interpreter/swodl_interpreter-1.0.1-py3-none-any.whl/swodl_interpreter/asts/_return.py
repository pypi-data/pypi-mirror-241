from swodl_interpreter.storage import Scope


class Return:
    def __init__(self, value=None, line=-1):
        self.value = value
        self.line = line

    def visit(self, scope: Scope):
        if self.value is not None:
            scope.Global['__return_func'] = self.value.visit(scope)
        else:
            try:
                if '_System_GoSubLine' in scope.Global:
                    return Return(line=scope.Global['_System_GoSubLine'])
                return Return(line=self.line+1)
            finally:
                scope.Global['_System_GoSubLine'] = -1
