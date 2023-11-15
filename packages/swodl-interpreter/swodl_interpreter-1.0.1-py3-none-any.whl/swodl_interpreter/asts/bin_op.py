from swodl_interpreter.storage import Scope
from swodl_interpreter.lexers.bool import Bool


def _is(value, type):
    try:
        if type == float and '.' not in str(value):
            return False
        type(value)
        return True
    except ValueError:
        return False


def cast(left, right, op_type, scope: Scope):
    left_type = type(left)
    right_type = type(right)
    left = left.visit(scope)
    right = right.visit(scope)
    if left is None:
        pass
    elif type(left) == str and type(right) == str and op_type == '+':
        pass
    elif Bool in (left_type, right_type):
        left = bool(left)
        right = bool(right)
    elif (_is(left, float) and (_is(right, int) or _is(right, int))) or (
        _is(right, float) and (_is(left, int) or _is(left, int))
    ):
        left = float(left)
        right = float(right)
    elif _is(left, int) and _is(right, int):
        left = int(left)
        right = int(right)
    else:
        left = str(left)
        right = str(right)
    return left, right


class BinOp:
    ops = {
        '+': lambda l, r: l + r,
        '-': lambda l, r: l - r,
        '*': lambda l, r: l * r,
        '/': lambda l, r: l / r,
        '%': lambda l, r: l % r,
        '<': lambda l, r: l < r,
        '>': lambda l, r: l > r,
        '<=': lambda l, r: l <= r,
        '>=': lambda l, r: l >= r,
        '==': lambda l, r: l == r,
        '!=': lambda l, r: l != r,
        '>>': lambda l, r: l >> r,
        '<<': lambda l, r: l << r,
        '^': lambda l, r: l ^ r,
        '&': lambda l, r: l & r,
        '&&': lambda l, r: l and r,
        '|': lambda l, r: l | r,
        '||': lambda l, r: l or r,
    }

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def visit(self, scope: Scope):
        left, right = cast(self.left, self.right, self.op, scope)
        if type(left) == int and self.op == '/':
            def result(l, r): return l // r
        elif self.op in BinOp.ops:
            result = BinOp.ops[self.op]
        else:
            raise NotImplementedError(f'{self.op}({self.op}) not supported')
        if left is None and right is None:
            return result
        elif left is None:
            return lambda l: result(l, right)
        elif right is None:
            return lambda r: result(left, r)
        return result(left, right)
