from .token import Token
from swodl_interpreter.lexers import *


class Lexer:
    """
    Read script file as text and creates Tokens one by one.
    """

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line_pos = 0
        self.line = 1
        self.prev_line = 1
        self.current_char = self.text[self.pos] if self.text else None
        self.tokens = [
            Whitespace,
            DocComments,
            Comments,
            MultilineComments,
            Status,
            Operation,
            Label,
            Bool,
            Keywords,
            MethodCall,
            Id,
            String,
            Number,
            Symbol,
        ]

    def error(self, char):
        raise KeyError(f'Invalid character "{char}" on {self.line} line.')

    def advance(self, count=1):
        """Advance the `pos` pointer and set the `current_char` variable."""
        for _ in range(count):
            self.pos += 1
            if self.prev_line == self.line:
                self.line_pos += 1
            else:
                self.prev_line = self.line
                self.line_pos = 0
            if self.pos > len(self.text) - 1:
                self.current_char = None  # Indicates end of input
            else:
                self.current_char = self.text[self.pos]

    def get_tokens(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            for _token in self.tokens:
                if _token.test(self):
                    errors = []
                    token = _token.process(self)
                    if type(token) == tuple:
                        token, errors = token
                    for e in errors:
                        yield SwodlSyntaxError(e)
                    if token is not None:
                        token.line = self.line
                        yield token
                    break
            else:
                self.error(self.current_char)

        yield EOF(self.line)

class SwodlSyntaxError(Exception):
    ...

class EOF(Token):
    def __init__(self, line):
        self.line = line
        # TODO: Remove this lines
        self.type = EOF
        self.value = None
