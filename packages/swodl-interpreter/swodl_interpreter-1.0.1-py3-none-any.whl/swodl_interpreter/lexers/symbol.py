from swodl_interpreter.token import Token

SYMBOLS = ['(', ')', '[', ']', '{', '}', '@', ';', ':', '=', ',', '.', '!']


class Symbol(Token):
    def test(lexer):
        return lexer.current_char in SYMBOLS

    def process(lexer):
        token = Token(lexer.current_char, lexer.current_char, lexer.line)
        lexer.advance()
        return token
