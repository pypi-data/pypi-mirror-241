from swodl_interpreter.storage import Scope
from swodl_interpreter.asts.struct import ThrowException, SwodlError


class Error:
    def __init__(self, node):
        self.node = node

    def visit(self, scope: Scope):
        e = self.node.visit(scope)
        scope.Global['_ExceptionMessage'] = str(e)
        raise SwodlError(e)


class Throw(Error):
    def visit(self, scope: Scope):
        e = self.node.visit(scope)
        scope.Global['_ExceptionMessage'] = str(e)
        raise ThrowException(e)
