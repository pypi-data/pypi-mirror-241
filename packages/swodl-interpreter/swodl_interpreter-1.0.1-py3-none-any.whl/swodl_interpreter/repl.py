import re

from swodl_interpreter.lexer import Lexer
from swodl_interpreter.parser import Parser
from swodl_interpreter.interpreter import Interpreter
from swodl_interpreter.storage import Scope


def repl():
    host = input('Set MAM host: ')
    scope = Scope()
    while (_in := input('>>>')) not in ('exit()', 'exit', 'exit;'):
        try:
            if re.match(r'^[\w_]*$', _in):
                print(scope.Global.get(_in, None))
                continue
            lexer = Lexer(_in)
            parser = Parser(lexer, scope)
            i = Interpreter(parser, scope, host)
            for _, v, _ in i.interpret():
                if type(v) == tuple:
                    v = v[1]
                if v is not None:
                    print(v)
        except Exception as e:
            print(f'\033[91m{e}\033[0m')
