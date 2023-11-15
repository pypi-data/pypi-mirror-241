import re
import json
import click

from dataclasses import dataclass
from swodl_interpreter.lexer import Lexer
from swodl_interpreter.parser import Parser
from swodl_interpreter.interpreter import Interpreter
from swodl_interpreter.lint import rules
from swodl_interpreter.storage import Scope
from swodl_interpreter.inbuild_functions import functions


@dataclass
class Args:
    host = None
    debug = False
    brake_point = []
    check_syntax = False
    show_code = False
    show_args = False
    mock = None
    include_folder = None

class Runner:
    def __init__(self, wf, args=Args()):
        if type(wf) == str:
            self.text = wf
            self.wflines = [f'{x}\n' for x in wf.split('\n')]
        elif type(wf) == list:
            self.text = ''.join(wf)
            self.wflines = wf
        self.scope = Scope()
        lexer = Lexer(self.text)
        self.parser = Parser(lexer, self.scope, args.check_syntax)
        self.args = args


    @staticmethod
    def from_file(f, args=Args()):
        return Runner(f.readlines(), args)

    @staticmethod
    def from_path(path, args=Args()):
        with open(path, 'r') as f:
            return Runner(f.readlines(), args)

    def lint(self):
        issues = []
        l = self.parser.parse()
        for token in l:
            if type(token).__name__ == 'Label' and \
                token.name in self.parser.scope.sub_calls:
                issues.extend(token.lint(l))
            else:
                r = token.lint()
                if type(r) == str:
                    issues.append(r)
                elif type(r) == list:
                    issues.extend(r)
        for i in issues:
            click.echo(i)
        if issues:
            click.secho('Lint failed', err=True, fg='red')

    def validate(self):
        from swodl_interpreter.parser import FuncNotDeclared
        from swodl_interpreter.asts.comment import Doc
        from swodl_interpreter.asts.status import Status
        for _ in self.parser.parse():
            pass
        for e in self.parser.errors:
            if type(e) == FuncNotDeclared and e.fn_name in functions:
                self.parser.errors.remove(e)
        return [e for e in self.parser.errors if not (type(e) == FuncNotDeclared and e.fn_name in functions)]

    def get_exec_lines(self):
        from swodl_interpreter.asts.label import Label
        from swodl_interpreter.asts.func_decl import FunctionDecl
        d = {}
        for statement in self.parser.parse():
            if type(statement) in (FunctionDecl, Label):
                d[statement.name] = statement.line
        return d

    def run(self, dict_={}, from_line=0, to_line=float('inf'), **kwarg):
        self.interpreter = Interpreter(
            self.parser,
            self.scope,
            self.args.host,
            self.args.include_folder,
            self.args.mock,
        )
        self.scope.Global.update({**kwarg, **dict_})
        _input = ''
        for c, v, _next in self.interpreter.interpret(from_line, to_line):
            _input = self.try_input(_input)
            if _input == 'stop':
                break
            _input = self.try_debug(_input, _next)
        return self.scope

    def try_input(self, _input):
        while re.search(r'(\w*_*)*=(\w*_*)*', _input) or re.search(
            r'set_brake_points\((\d+\,?\s?)+\)', _input
        ):
            # print(_input)
            if not re.search(r'set_brake_points\((\d+\,?\s?)+\)', _input):
                n, v = _input.split('=')
                self.scope.Global[n.strip()] = v
            if re.search(r'set_brake_points\((\d+\,?\s?)+\)', _input):
                self.args.brake_point = [int(x)
                                         for x in re.findall(r'\d+', _input)]
            # print("---", self.args.brake_point)
            _input = input(
                "Press 'Enter' to continue or write 'stop' to stop debug: ")
        return _input

    def try_show_args(self):
        if self.args.show_args:
            print(json.dumps({'Global': self.scope.Global,
                              'Functions': {k:str(v) for k, v in self.scope.functions.items()}
                            }, indent=4))

    def try_show_code(self, line):
        if self.args.show_code:
            n_line = '\n'
            print()
            print(
                f"{line-1:>5}   | {self.wflines[line-2].replace(n_line, '')}")
            print(f"{line:>5} ->| {self.wflines[line-1].replace(n_line, '')}")
            print(f"{line+1:>5}   | {self.wflines[line].replace(n_line, '')}")
            print()

    def try_debug(self, _input, _next):
        if (
            self.args.debug and
            (_input == 'step'
            or _next in (self.args.brake_point or []))
        ):
            print(f'Line: {_next}')

            self.try_show_code(_next)
            self.try_show_args()

            _input = input(
                "Press 'Enter' to continue or write 'stop' to stop debug: ")
        return _input

# with open('./tests/test.wf', 'r') as f:
#     r = Runner.from_file(f)
#     r.args.debug = True
#     r.args.brake_point = [1, 8]
#     r.run()
