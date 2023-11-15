import json
import inspect

from swodl_interpreter.asts import *
from swodl_interpreter.asts import Error as AstError
from swodl_interpreter.inbuild_functions import functions
from swodl_interpreter.web_service_resolver import mapping as web_mapping
from swodl_interpreter.lexers.operation import OPERATION, EQUALS

# from swodl_interpreter.lexers.number import Number as NumberToken
from swodl_interpreter.lexers.string import String as StringToken
from swodl_interpreter.lexers import Operation
from swodl_interpreter.asts.struct import ArrayType
from swodl_interpreter.lexer import EOF, SwodlSyntaxError
from swodl_interpreter.storage import Scope

# from swodl_interpreter.storage import web_func_type

class Error:
    def __init__(self, line: int, msg: str):
        self.line = line
        self.msg = msg

    def json(self):
        return json.dumps({
            'line': self.line,
            'msg': self.msg
        })

class FuncNotDeclared(Error):
    def __init__(self, line: int, msg: str, name: str):
        super().__init__(line, msg)
        self.fn_name = name

class Parser(object):
    def __init__(self, lexer, scope: Scope, collect_errors=False):
        # self.lexer = lexer
        self.scope = scope
        self.line = -1
        self.lines = []
        self.errors = []
        self.collect_errors = collect_errors
        # set current token to the first token taken from the input
        self.tokens = lexer.get_tokens()
        self.current_token = next(self.tokens)

        self.statements = {
            'BEGIN': self.compound_statement,
            'EXIT': self._statement(Exit),
            'METHODCALL': self.proccall_statement,
            'ERROR': self._statement(AstError, True),
            'DELAY': self._statement(Delay, True),
            'GOSUB': self.go_call_statement(SubCall),
            'GOTO': self.go_call_statement(GoToCall),
            'DECLARE': self.declare,
            'ID': self.assignment_statement,
            'LABEL': self.label,
            'THROW': self._statement(Throw, True),
            'IF': self.condition,
            'WHILE': self.while_statement,
            'FUNCTION': self.function,
            'INCLUDE': self.include,
            'VAR': self.var,
            'CONST': self.const,
            'IN': self._in,
            '[': self.assignment_statement,
            'TRY': self._try,
            'DO': self.do_retry,
            'RETRY': self.do_retry,
            'STATUS': self.status,
            'RETURN': self._return,
            'COMMENT': self.comment,  # lambda: self.empty(),
            'DOC': self.doc,
        }

    def doc(self):
        return Doc(self.next())

    def comment(self):
        return Comment(self.next())

    def next(self, *tokens):
        for token in tokens or [None]:
            temp = self.current_token
            if token is None or self._istype(token):
                self.line = self.current_token.line
                self.lines.append(self.line)
                t = None
                while t is None:
                    t = next(self.tokens)
                    if type(t) == SwodlSyntaxError:
                        self.error_text(str(t))
                        t = None
                self.current_token = t
            else:
                self.error(token)
        return temp

    def next_if(self, token):
        if self._istype(token):
            return self.next()

    def add_error(self, err):
        if self.collect_errors:
            self.errors.append(err)
        else:
            raise Exception(err.msg)

    def error_text(self, msg, line=None):
        line = line if line is not None else self.line
        self.add_error(Error(line, msg))

    def error(self, token):
        self.error_text(f'{token} missing on {self.line} line.')

    def eat(self, token_type):
        if token_type.lower() == 'all' or self._istype(token_type):
            self.line = self.current_token.line
            self.lines.append(self.line)
            self.current_token = next(self.tokens)
        else:
            self.error(token_type)

    def compound_statement(self):
        statement_list = []
        begin_token_line = self.current_token.line
        if self.current_token.type == '{':
            self.eat('{')
            while not self._istype('}', EOF):
                statement_list.append(self.statement())
            if type(self.current_token) == EOF:
                self.error_text(
                    f"'{{' on {begin_token_line} line not closed", begin_token_line
                )
            else:
                self.eat('}')
        else:
            statement_list = [self.statement()]
        return Compound(statement_list, begin_token_line)

    def statement(self):
        templ = self.current_token.line
        node = self.statements.get(self.current_token.type, self.empty)
        if node == self.empty and self.current_token.type not in (
            'SUSPEND',
            ':',
            ';',
            '@',
        ):
            try:
                node = self.expr()
            except:
                node = node()
        else:
            node = node()
        if node:
            node.line = templ
        return node

    def _istype(self, *args):
        return self.current_token.type in args

    def _return(self):
        try:
            self.eat('RETURN')
            return Return() if self._istype(';') else Return(self.expr())
        finally:
            self.eat(';')

    def status(self):
        text = self.current_token.value
        self.eat('STATUS')
        return Status(text)

    def do_retry(self):
        def get_block():
            block = self.compound_statement()
            self.eat('WHILE')
            condition = self.expr()
            self.eat(';')
            return condition, block

        if self.next().type == 'DO':
            return DoCycle(*get_block())
        else:
            return Retry(self.expr(), *get_block())
        # c.end_line = self.line
        # return c

    def _try(self):
        self.eat('TRY')
        try_body = self.compound_statement()
        self.eat('CATCH')
        catch = self.compound_statement()
        t = TryCatch(try_body, catch)
        t.end_line = self.line
        return t

    def var(self):
        self.eat(self.current_token.type)
        return self.assignment_statement(True)

    def _in(self):
        temp = self.current_token
        self.eat('IN')
        temp.set_name(self.current_token.name)
        self.next('ID', ';')
        return temp

    # CONST
    def const_assign(self):
        if not self._istype('='):
            self.error_text('Constant must be initialized with a value')
        self.eat('=')

    def should_not_method(self):
        if self._istype('METHODCALL'):
            self.error_text('Expressions are not allowed as values of const.')

    def _assign(self, node, func=None):
        node.add(self.scope, self.current_token)
        self.eat('ID')
        self.const_assign()
        if func != None:
            func()
        node.right.append(self.expr())

    def const(self):
        node = self.current_token
        self.eat('CONST')
        self._assign(node)
        while self._istype(','):
            self.eat(',')
            self._assign(node, self.should_not_method)
        self.eat(';')
        return node

    # ----------------

    def assignment_statement(self, is_var=False):
        self.next_if('[')
        left = [self.variable()]
        right = []
        temp = Operation(value='=')
        while self._istype('=', ','):
            temp = self.next()
            if temp.type == ',' and self._istype('ID'):
                left.append(self.variable())
            # self.proccall_statement(close=False)
            # elif self._istype('METHODCALL'):
            #     tempcall = self.proccall_statement(close=False)
            #     tempcall.line = self.current_token.line
            #     right.append(tempcall)
            else:
                right.append(self.expr())
            self.next_if(']')
        self.next(';')
        return Assign(left, temp, right, is_var)

    def condition(self):
        self.eat('IF')
        conditions = [self.expr()]
        blocks = [self.compound_statement()]
        else_block = None
        while self._istype('ELSE'):
            self.eat('ELSE')
            if self._istype('IF'):
                self.eat('IF')
                conditions.append(self.expr())
                blocks.append(self.compound_statement())
            else:
                else_block = self.compound_statement()
                break
        c = Condition(conditions, blocks, else_block)
        c.end_line = self.line
        return c

    def declare(self):
        try:
            self.next('DECLARE')
            self.next_if('CONST')
            self.next_if('CONST')
            type_ = self.next_if('ID')
            if self._istype('['):
                self.eat('[')
                type_ = []
                if not self._istype(']'):
                    type_.append(self.expr().value)
                while self._istype(','):
                    self.eat(',')
                    type_.append(self.expr().value)
                self.eat(']')
            if not self._istype('METHODCALL'):
                raise ExecutionException('No method declaration found.')
            method = self.proccall_statement(declare=True)
            method.line = self.current_token.line
            return DeclareWeb(type_, method)
        except Exception as e:
            if self.collect_errors:
                temp_line = self.line
                self.errors.append(
                    Error(
                        self.line,
                        f'Invalid web method declaration on {self.line}. {e}'
                    )
                )
                while self.line == temp_line:
                    self.eat('All')
            else:
                raise ExecutionException(
                    f'Invalid web method declaration on {self.line}. {e}'
                )

    def while_statement(self):
        self.eat('WHILE')
        return Cycle(self.expr(), self.compound_statement())

    def function(self):
        self.eat('FUNCTION')
        name = self.current_token.value
        self.eat('METHODCALL')
        self.eat('(')
        actual_params = []
        do = not self._istype(')')
        while do:
            if self._istype(','):
                self.eat(',')
            node = self.expr()
            actual_params.append(node)
            do = self._istype(',')

        self.eat(')')
        return FunctionDecl(name, actual_params, self.compound_statement())

    def include(self):
        self.eat('INCLUDE')
        node = Include(self.current_token.value)
        self.eat('STRING')
        self.eat(';')
        return node

    def _statement(self, cls, expr=False):
        def func():
            self.eat(cls.__name__.upper())
            if expr:
                value = self.expr()
            self.eat(';')
            if cls == Error:
                return cls(self.line, value)
            return cls(value) if expr else cls()

        return func

    def label(self):
        name = self.current_token.value
        self.eat('LABEL')
        self.eat(':')
        return Label(name)

    def go_call_statement(self, cls):
        def func():
            self.eat(self.current_token.type)
            name = self.current_token.value
            goto_calls.append((self.line, name))
            self.eat('ID')
            self.eat(';')
            return cls(name)

        return func

    def proccall_statement(self, main=True, close=True, declare=False):
        """proccall_statement : ID LPAREN (expr (',' expr)*)? RPAREN"""
        token = self.current_token

        proc_name = self.current_token.value
        self.eat('METHODCALL')
        self.eat('(')
        actual_params = []
        do = self.current_token.type != ')'
        while do:
            if self.current_token.type == ',':
                self.eat(',')
            if (
                declare
                and self.current_token.type == 'ID'
                and self.current_token.value
                in ('string', 'int', 'float', '_json', '_auto', '_array')
            ):
                self.eat('ID')
            if self.current_token.type == 'METHODCALL':
                node = self.proccall_statement(False)
            elif self.current_token.type == '[':
                self.eat('[')
                temp_v = []
                while self.current_token.type != ']':
                    temp_v.append(self.expr())
                    if self.current_token.type == ',':
                        self.eat(',')
                node = ArrayType(temp_v)
                self.eat(']')
            else:
                node = self.expr()
                if declare:
                    if self.current_token.type == '{':
                        self.eat('{')
                        self.eat('}')
                    if type(node) == Array:
                        node = node.left
            node.line = self.current_token.line
            actual_params.append(node)
            do = self.current_token.type == ','

        self.eat(')')
        url = None
        if main and self.current_token.type == 'AS':
            self.eat(self.current_token.type)
            new_name = self.expr().value
            web_mapping[new_name] = proc_name
            proc_name = new_name
        if self.current_token.type == '@':
            self.eat(self.current_token.type)
            if self.current_token.type == '@':
                self.eat(self.current_token.type)
            url = self.expr()
        if main and close:
            self.eat(';')

        if self.collect_errors:
            try:
                default_params = {
                    k: v.default
                    for k, v in inspect.signature(
                        functions[proc_name]
                    ).parameters.items()
                    if v.default is not inspect.Parameter.empty
                }
                params = inspect.getfullargspec(functions[proc_name]).args
            except:
                default_params = {}
                try:
                    # self.error_text(web_func_type[proc_name].args)
                    params = Scope.web_type[proc_name].args
                except:
                    params = None
            if not declare:
                if proc_name not in functions and proc_name not in Scope.web_type:
                    self.add_error(FuncNotDeclared(
                        self.current_token.line,
                        f'{proc_name} not declared',
                        proc_name))
                elif params != None and (
                    len(params) - len(default_params) > len(actual_params)
                    or len(actual_params) > len(params)
                ):
                    self.error_text(
                        f'{proc_name} has wrong number of parameters. Expected {len(params)} but {len(actual_params)} was given'
                    )

        node = ProcedureCall(
            proc_name=proc_name, actual_params=actual_params, token=token, url=url
        )
        return node

    def variable(self):
        node = self.current_token
        self.eat('ID')
        while self.current_token.type in ('.', '['):
            if self.current_token.type == '[':
                self.eat('[')
                node = Array(node, self.current_token)
                if self.current_token.type != ']':
                    self.eat('all')
                self.eat(']')
            if self.current_token.type in ('.'):
                self.eat(self.current_token.type)
                node = Struct(left=node, right=Attr(self.current_token))
                self.eat('ID')
        return node

    def empty(self):
        self.eat('All')
        return NoOp()

    def expr(self):
        node = self.term() or NoOp()
        while self.current_token.value in OPERATION + EQUALS:
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token.value, right=self.term())
        node.line = self.line
        return node

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()
        while self._istype('*', '/'):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token.value, right=self.factor())

        return node

    def factor(self):
        token = self.current_token
        if token.type == 'ID':
            return self.variable()
        node = self.statements.get(self.current_token.type, self.empty)
        if self.empty != node:
            if node == self.proccall_statement:
                return node(main=False)
            return node()
        self.eat(token.type)
        if token.type in ('!', '+', '-'):
            return UnaryOp(token.type, self.factor())
        elif token.type == '(':
            node = self.expr()
            self.eat(')')
            if hasattr(node, 'name') and node.name in (
                'int',
                'float',
                'string',
                'bool',
            ):
                node = UnaryOp(node.name, self.factor())
            return node
        elif type(token) == StringToken:
            return String(token.value, token)
        return token

    def parse(self):
        while type(self.current_token) != EOF:
            try:
                yield self.statement()
            except StopIteration:
                pass
        if self.collect_errors:
            for line, name in goto_calls:
                if name not in Scope.labels:
                    self.error_text(f'{name} label not declared', line)


goto_calls = []
