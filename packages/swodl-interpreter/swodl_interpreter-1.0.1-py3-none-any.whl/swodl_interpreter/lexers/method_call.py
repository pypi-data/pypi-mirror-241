from swodl_interpreter.token import Token


class MethodCall(Token):
    def __init__(self, name: str, line: int) -> None:
        super().__init__(value=name, line=line)

    def test(lexer):
        return Token._if(lexer, r'[\w_]+\(', is_re=True)

    def process(lexer):
        result = ''
        while lexer.current_char != '(':
            result += lexer.current_char
            lexer.advance()
        return MethodCall(result, lexer.line)
