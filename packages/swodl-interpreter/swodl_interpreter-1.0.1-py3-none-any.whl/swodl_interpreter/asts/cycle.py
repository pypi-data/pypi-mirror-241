import types

from swodl_interpreter.storage import Scope


class Cycle:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
        self._next = self.body.children[0].line

    def visit(self, scope: Scope):
        while self.condition.visit(scope):
            yield (self.line, None, self.body.children[0].line)
            v = self.body.visit(scope)
            if isinstance(v, types.GeneratorType):
                first_line = 0
                for i, vv in enumerate(v):
                    if first_line == 0:
                        first_line = vv[0]
                    # if self._next == -1:
                    #     self._next = first_line
                    if i == len(self.body.children) - 1:
                        self._next = self.line
                    yield vv
            else:
                yield v
            # self._next = -1
