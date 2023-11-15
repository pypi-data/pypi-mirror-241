from swodl_interpreter.token import Token


class String(Token):
    def __init__(self, type: str, value: str, line: int = -1) -> None:
        super().__init__(type, value, line)

    def test(lexer):
        return Token._if(lexer, '"')

    def process(lexer):
        result = ''
        lexer.advance()
        special_chars = {
            '\\': '\\',
            '"': '\"',
            'n': '\n',
            'r': '\r',
            'a': '\a',
            'b': '\b',
            'f': '\f',
            't': '\t',
            'v': '\v',
        }
        errors = []
        while lexer.current_char is not None and lexer.current_char != '"':
            if lexer.current_char == '\\':
                lexer.advance()
                if lexer.current_char in special_chars:
                    result += special_chars[lexer.current_char]
                    lexer.advance()
                else:
                    errors.append(UnrecognizedEscapeException(f'Unrecognized escape sequence {lexer.current_char} on {lexer.line}.'))
            else:
                if lexer.current_char == '\n':
                    lexer.line += 1
                result += lexer.current_char
                lexer.advance()
        if lexer.current_char != '"':
            raise Exception('String never closed.')
        lexer.advance()
        return String('STRING', result, lexer.line), errors

class UnrecognizedEscapeException(Exception):
    ...
