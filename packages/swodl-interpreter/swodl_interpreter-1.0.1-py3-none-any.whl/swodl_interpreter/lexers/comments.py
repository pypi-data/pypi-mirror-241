from swodl_interpreter.token import Token

class DocComments(Token):
    def test(lexer):
        return Token._if(lexer, '///[\s\n]', is_re=True)

    def process(lexer):
        doc = ''
        for _ in range(3):
            lexer.advance()
        while lexer.current_char != '\n':
            doc += lexer.current_char
            lexer.advance()
        return DocComments('DOC', doc, lexer.line)

    def __str__(self) -> str:
        return self.value

class Comments(Token):
    def test(lexer):
        return Token._if(lexer, '//')

    def process(lexer):
        comment = ''
        while lexer.current_char != '\n':
            comment += lexer.current_char
            lexer.advance()
        return Comments('COMMENT', comment, lexer.line)

    def __str__(self) -> str:
        return self.value


class MultilineComments(Token):
    def test(lexer):
        return Token._if(lexer, '/*')

    def process(lexer):
        comment = ''
        lexer.advance(2)
        while Token.not_end(lexer, '*/') and not Token._if(lexer, '*/'):
            if lexer.current_char == '\n':
                lexer.line += 1
            comment += lexer.current_char
            lexer.advance()
        lexer.advance(2)
        return MultilineComments('COMMENT', comment, lexer.line)

    def __str__(self) -> str:
        return self.value
