from lxml import etree

from swodl_interpreter.storage import Scope
from swodl_interpreter.asts.struct import Struct, Array
from swodl_interpreter.asts.procedure_call import ProcedureCall


class Assign:
    def __init__(self, left, op, right, is_var):
        self.left = left
        self.op = op
        self.right = right
        self.is_var = is_var

    def visit(self, scope: Scope):
        for i, _ in enumerate(self.left):
            if type(self.left[i]) in (Array, Struct):
                self.left[i].visit(scope, self.right[i].visit(scope))
            else:
                var_name = self.left[i].name
                if (
                    len(self.left) > 1
                    and len(self.right) == 1
                    and type(self.right[0]) == ProcedureCall
                ):
                    method = self.right[0]
                    params = scope.web_type[method.proc_name]
                    r = method.visit(scope)
                    if r is not None:
                        r = (
                            etree.fromstring(r)
                            .xpath(f"//*[local-name()='{params[i]}']")[0]
                            .text
                        )
                    scope.Global[var_name] = r or ''
                elif i < len(self.right):
                    if self.op.value == '=':
                        scope.Global[var_name] = self.right[i].visit(scope)
                    else:
                        from swodl_interpreter.asts.bin_op import BinOp
                        scope.Global[var_name] = BinOp(
                            self.left[i], self.op.value, self.right[i]
                        ).visit(scope)
        return self.line, None
