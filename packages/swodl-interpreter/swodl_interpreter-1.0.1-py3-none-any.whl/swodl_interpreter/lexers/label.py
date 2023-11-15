from swodl_interpreter.token import Token


class Label(Token):
    def __init__(self, name: str, line: int) -> None:
        super().__init__('LABEL', name, line)

    def test(lexer):
        return Label._if(lexer, r'[\w_]+\:', is_re=True)

    def process(lexer):
        result = ''
        while lexer.current_char != ':':
            result += lexer.current_char
            lexer.advance()
        return Label(result, lexer.line)
