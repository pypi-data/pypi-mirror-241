import types

from swodl_interpreter.storage import Scope
from swodl_interpreter.asts.execution_exception import ExecutionException
from swodl_interpreter.asts.goto_sub import GoToCall, SubCall
from swodl_interpreter.asts.func_decl import FunctionDecl
from swodl_interpreter.asts._return import Return
from swodl_interpreter.asts.label import Label
from swodl_interpreter.asts.exit import Exit



class List(list):
    def visit(self, scope: Scope, from_line=0, to_line=float('inf')):
        i = 0
        try:
            for n in filter(lambda x: type(x) == FunctionDecl, self):
                n.visit(scope)
            if len(self) > 0 and self[i].line >= from_line:
                yield self[i].line, None, self[i].line
            while i < len(self):
                if to_line < self[i].line:
                    break
                v = None
                if self[i].line >= from_line:
                    v = self[i].visit(scope)
                    if isinstance(v, types.GeneratorType):
                        for _v, _, _n in v:
                            yield _v, _, _n
                    elif type(v) == Exit:
                        break
                    yield self[i].line, v, self.get_next_line(v, i)

                i = self.get_next_index(v, i)
        except NameError as e:
            scope.Global['_ExceptionMessage'] = str(e)
            raise ExecutionException(
                f'Missing {e} variable on {self[i].line} line.', e)
        except Exception as e:
            scope.Global['_ExceptionMessage'] = str(e)
            raise

    def get_next_index(self, v, i):
        if type(v) in (SubCall, GoToCall):
            return self.get_goto(v)[0]
        elif type(v) == Return and v.line > 0:
            i = self.get_return(v)[0]
        return i + 1

    def get_next_line(self, v, i):
        if isinstance(v, types.GeneratorType):
            return self[i + 1].line if i + \
                1 < len(self) else self[-1].line
        # elif type(v) == list:
        #     _next = v[0][0]
        elif type(v) in (SubCall, GoToCall):
            return self.get_goto(v)[1].line
        elif type(v) == Return and v.line > 0:
            return self.get_return(v)[1].line
        elif i + 1 < len(self):
            return self[i + 1].line
        return self[-1].line

    def get_goto(self, v):
        for i, x in enumerate(self):
            if type(x) == Label and x.name == v.name:
                return i, x

    def get_return(self, v):
        for i, x in enumerate(self):
            if type(x) == SubCall and x.line == v.line:
                return i, x
