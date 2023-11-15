from swodl_interpreter.storage import Scope


class Condition:
    def __init__(self, conditions, blocks, else_block):
        self.conditions = conditions
        self.blocks = blocks
        self.else_block = else_block

    def visit(self, scope: Scope):
        for i, condition in enumerate(self.conditions):
            if condition.visit(scope):
                self._next = self.blocks[i].children[0].line
                yield condition.line, None, self._next
                for j, v in enumerate(self.blocks[i].visit(scope)):
                    if j == len(self.blocks[i].children) - 1:
                        self._next = self.end_line
                    yield v
                break
            else:
                self._next = (
                    self.conditions[i + 1].line
                    if i + 1 < len(self.conditions)
                    else self.end_line
                )
                yield (condition.line, None, self._next)
        else:
            if self.else_block:
                yield (self.else_block.line, None, self.else_block.children[0].line)
                for v in self.else_block.visit(scope):
                    yield v
