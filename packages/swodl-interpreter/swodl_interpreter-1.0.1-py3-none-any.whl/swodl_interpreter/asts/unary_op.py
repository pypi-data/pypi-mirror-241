from swodl_interpreter.storage import Scope


def try_to_num(value):
    try:
        return float(value)
    except ValueError:
        try:
            return int(value)
        except ValueError:
            return value


class UnaryOp:
    ops = {
        '+': lambda value: value,
        '-': lambda value: -try_to_num(value),
        'string': lambda value: str(value),
        'int': lambda value: int(value),
        'float': lambda value: float(value),
        'bool': lambda value: bool(False if value in ('0', 0) else value),
        '!': lambda value: not value,
    }

    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def visit(self, scope: Scope):
        op = self.op
        value = self.expr.visit(scope)
        if value is None:
            return None
        if op in UnaryOp.ops:
            return UnaryOp.ops[op](value)
        else:
            raise NotImplementedError(f'{op} not supported')
