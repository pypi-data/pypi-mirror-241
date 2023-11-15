from swodl_interpreter.token import Token


class Number(Token):
    def __init__(self, type: str, value: str, line: int = -1) -> None:
        super().__init__(type, value, line)

    def test(lexer) -> bool:
        return lexer.current_char.isdigit()

    def process(lexer):
        result = ''
        while lexer.current_char is not None and Token._if(
            lexer, r'[0-9\.]', is_re=True
        ):
            result += lexer.current_char
            lexer.advance()
        if '.' in result:
            return Number('FLOAT', float(result))
        return Number('INTEGER', int(result))

    def visit(self, _=None):
        return self.value
