from swodl_interpreter.storage import Scope


class TryCatch:
    def __init__(self, block, catch):
        self.block = block
        self.catch = catch

    def _visit_child(self, block, scope):
        v = block.visit(scope)
        self._next = block.children[0].line if block.children else self.end_line
        yield (self.line, None, self._next)
        # if isinstance(v, types.GeneratorType):
        for i, vv in enumerate(v):
            if i == len(block.children) - 1:
                self._next = self.end_line
            yield vv
        # else:
        #     yield v

    def visit(self, scope: Scope):
        try:
            for children in self._visit_child(self.block, scope):
                yield children
        except Exception as e:
            scope.Global['_ExceptionMessage'] = str(e)
            for children in self._visit_child(self.catch, scope):
                yield children
