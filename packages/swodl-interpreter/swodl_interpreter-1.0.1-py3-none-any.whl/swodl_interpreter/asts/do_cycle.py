import types

from swodl_interpreter.asts.cycle import Cycle
from swodl_interpreter.storage import Scope


class DoCycle(Cycle):
    def visit(self, scope: Scope):
        r = []
        while True:
            self._next = self.body.children[0].line
            yield (self.line, None, self.body.children[0].line)
            v = self.body.visit(scope)
            if isinstance(v, types.GeneratorType):
                first_line = 0
                for i, vv in enumerate(v):
                    if first_line == 0:
                        first_line = vv[0]
                    if self._next == -1:
                        self._next = first_line
                    # if i == len(self.body.children) - 1:
                    #     AST._next = self.end_line
                    yield vv
            else:
                yield v
            if not self.condition.visit(scope):
                break
