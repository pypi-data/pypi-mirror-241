from swodl_interpreter.token import Token


class Status(Token):
    def test(lexer):
        return Token._if(lexer, '[[')

    def process(lexer):
        lexer.advance(2)
        result = ''
        while not Token._if(lexer, ']]'):
            result += lexer.current_char
            lexer.advance()
        lexer.advance(2)
        token = Status('STATUS', result, lexer.line)
        return token
