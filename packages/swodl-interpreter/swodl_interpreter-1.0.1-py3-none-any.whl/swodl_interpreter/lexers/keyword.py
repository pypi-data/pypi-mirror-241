from swodl_interpreter.token import Token
from swodl_interpreter.storage import Scope


class In(Token):
    def set_name(self, name):
        self.name = name

    def visit(self, _):
        pass


class Const(Token):
    def __init__(self) -> None:
        super().__init__()
        self.left, self.right = [], []

    def add(self, scope, left):
        self.left.append(left)
        scope.const.append(left.name)

    def visit(self, scope: Scope):
        for i, l in enumerate(self.left):
            scope.Global[l.name] = self.right[i].visit(scope)


class Soap(Token):
    def __init__(self) -> None:
        self.token = self
        super().__init__('CONST')  # TODO: FIX!


RESERVED_KEYWORDS = [
    'try',
    'catch',
    'throw',
    'if',
    'else',
    'while',
    'do',
    'retry',
    'in',
    'var',
    'const',
    'soap',
    'goto',
    'gosub',
    'return',
    'exit',
    'error',
    'delay',
    'suspend',
    'declare',
    'as',
    'include',
    'function',
]


class Keywords(Token):
    def __init__(self, type, line) -> None:
        super().__init__(type, line=line)

    def test(lexer):
        keywords = f"({'|'.join(RESERVED_KEYWORDS)})"
        return Token._if(lexer, keywords + r'[ ():;,{\n]+', is_re=True)

    def process(lexer):
        """Handle identifiers and reserved keywords"""
        result = ''
        while lexer.current_char is not None and (
            lexer.current_char.isalnum() or lexer.current_char == '_'
        ):
            result += lexer.current_char
            lexer.advance()
        if result == 'in':
            return In()
        if result == 'soap':
            return Soap()
        if result == 'const':
            return Const()
        return Keywords(result, lexer.line)
