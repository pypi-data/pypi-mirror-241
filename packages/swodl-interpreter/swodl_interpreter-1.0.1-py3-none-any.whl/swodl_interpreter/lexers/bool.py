from swodl_interpreter.token import Token


class Bool(Token):
    def __init__(self, value: bool, line: int) -> None:
        super().__init__(value=value, line=line)

    def __str__(self):
        return str(self.value)

    def visit(self, _=None):
        return self.value

    def test(lexer):
        return Token._if(lexer, r'(true|false)[ );,\n]+', is_re=True)

    def process(lexer):
        """Handle identifiers and reserved keywords"""
        result = ''
        while lexer.current_char is not None and lexer.current_char.isalnum():
            result += lexer.current_char
            lexer.advance()
        return Bool(result == 'true', lexer.line)
