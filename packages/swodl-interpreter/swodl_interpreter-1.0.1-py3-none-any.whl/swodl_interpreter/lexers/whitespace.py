from swodl_interpreter.token import Token


class Whitespace(Token):
    def test(lexer):
        return lexer.current_char.isspace()

    def process(lexer):
        while lexer.current_char is not None and lexer.current_char.isspace():
            if lexer.current_char == '\n':
                lexer.line += 1
            lexer.advance()
