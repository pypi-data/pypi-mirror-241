import types

from swodl_interpreter.storage import Scope
from swodl_interpreter.asts.comment import Comment
from swodl_interpreter.asts.execution_exception import ExecutionException


class NoOp:
    def visit(self, _):
        pass  # TODO: Check lines propagation


class Compound:
    def __init__(self, children, line):
        self.children = [x for x in children if type(x) != Comment]
        self.line = line
        self._next = self.children[0].line if len(self.children) > 0 else line

    def visit(self, scope: Scope):
        try:
            for i, child in enumerate(self.children):
                self._next = self.children[i+1].line if i + \
                    1 < len(self.children) else self.line
                value = child.visit(scope)
                if isinstance(value, types.GeneratorType):
                    for list_value in value:
                        yield list_value
                elif isinstance(value, tuple):
                    yield *value, self._next
                else:
                    yield child.line, value, self._next
        except Exception as e:
            err = ExecutionException(f'Error on {child.line} line. {e}', e)
            scope.Global['_ExceptionMessage'] = str(err)
            raise err
