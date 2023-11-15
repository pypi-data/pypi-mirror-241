from swodl_interpreter.storage import *
from swodl_interpreter.asts._list import List
from swodl_interpreter.asts.execution_exception import ExecutionException
from swodl_interpreter.storage import Scope


class Include:
    def __init__(self, name):
        self.name = name

    def visit(self, scope: Scope):
        import os
        from swodl_interpreter.lexer import Lexer
        from swodl_interpreter.parser import Parser

        try:
            text = Scope.web_resolver.get_wf(self.name)
        except:
            try:
                with open(
                    os.path.join(Scope.include_dir, f'{self.name}.wfi'), 'r'
                ) as f:
                    text = f.read()
            except Exception as e:
                raise ExecutionException(f'Failed to include {self.name}.', e)
        _scope = Scope()
        lexer = Lexer(text)
        parser = Parser(lexer, _scope)
        tree = parser.parse()
        return List(tree).visit(scope)
