from swodl_interpreter.asts.assign import Assign
from swodl_interpreter.token import Token

OPERATION = ['+', '-', '*', '/', '%', '&&', '||', '&', '|', '^', '<<', '>>']
EQUALS = ['==', '<=', '>=', '!=', '<', '>']
ASSIGN = [f'{op}=' for op in OPERATION]
x = OPERATION + EQUALS + ASSIGN


class Operation(Token):
    def get_op(lexer):
        n = lexer.pos
        for op in ASSIGN + OPERATION + EQUALS:
            if op == lexer.text[n: n + len(op)]:
                return op

    def test(lexer):
        return Operation.get_op(lexer) != None

    def process(lexer):
        op = Operation.get_op(lexer)
        lexer.advance(len(op))
        if op in ASSIGN:
            return Operation('=', OPERATION[ASSIGN.index(op)], lexer.line)
        return Operation(op, op, lexer.line)
