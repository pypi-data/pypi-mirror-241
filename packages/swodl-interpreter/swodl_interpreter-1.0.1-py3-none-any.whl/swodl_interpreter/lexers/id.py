from swodl_interpreter.token import Token
from swodl_interpreter.storage import Scope


class Id(Token):
    def __init__(self, name: str, line: int) -> None:
        super().__init__(value=name, line=line)
        self.name = name

    def test(lexer):
        return lexer.current_char.isalpha() or lexer.current_char == '_'

    def process(lexer):
        result = ''
        while lexer.current_char is not None and (
            lexer.current_char.isalnum() or lexer.current_char == '_'
        ):
            result += lexer.current_char
            lexer.advance()
        return Id(result, lexer.line)

    def visit(self, scope: Scope):
        if self.name not in scope.Global:
            if self.name in ('_a', '_b', '_value'):
                return None
            # return self.name  # TODO: Check why
            # raise NameError(repr(self.name))
            return None
        else:
            v = scope.Global[self.name] if scope.Global[self.name] != None else ''
            if type(v) in (int, float, bool):
                return str(v)
            return v
