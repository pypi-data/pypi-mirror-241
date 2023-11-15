import re


class Token:
    def __init__(self, _type: str = '', value: str = '', line: int = -1) -> None:
        self.type = _type.upper() or type(self).__name__.upper()
        self.value = value
        self.line = line

    def __str__(self) -> str:
        return f'{type(self).__name__}({self.type}, {repr(self.value)})'

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.type}, {repr(self.value)}, {self.line})'

    def not_end(lexer, text: str) -> bool:
        return lexer.pos + len(text) < len(lexer.text)

    def _if(lexer, text: str, shift: int = 0, is_re: bool = False) -> bool:
        n = lexer.pos + shift
        text = text if is_re else re.escape(text)
        return re.match(text, lexer.text[n:]) is not None
