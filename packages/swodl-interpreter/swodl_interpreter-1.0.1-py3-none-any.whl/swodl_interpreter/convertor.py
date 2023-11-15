import os
import pathlib
import json
from io import FileIO
from posixpath import join
from swodl_interpreter.lexer import Lexer
from swodl_interpreter.parser import Parser
from swodl_interpreter.asts import NoOp, error
from swodl_interpreter.storage import Scope

import sys, inspect


from swodl_interpreter.token import Token
from collections.abc import Iterable
from swodl_interpreter.asts import *
from swodl_interpreter.lexers import label
from swodl_interpreter.lexers.id import Id
from swodl_interpreter.lexers.bool import Bool
from swodl_interpreter.lexers.number import Number
from swodl_interpreter.lexers.keyword import In, Const


class Converter:
    def __init__(self, wf):
        if type(wf) == str:
            self.text = wf
        elif isinstance(wf, Iterable):
            self.text = ''.join(wf)
        self.parser = Parser(Lexer(self.text), Scope())

    def convert(self: FileIO, output: FileIO) -> None:
        t = list(self.parser.parse())
        tree = list(filter(lambda x: not isinstance(x, NoOp), t))
        path = pathlib.Path(output.name)
        #filename, file_extension = os.path.splitext(output.name)
        convertor = convertors[path.suffix]
        for cls in inspect.getmembers(sys.modules[__name__], inspect.isclass):
            if cls[1] not in (FileIO, Converter):
                cls[1].convert = convertor[cls[1]] if cls[1] in convertor else lambda *a, **k: ''
        if path.suffix == '.py':
            output.write('from swodl_interpreter.inbuild_functions import *\n')
            output.write('from swodl_interpreter.web_service_resolver import Resolver\n')
            output.write('\n')
            output.write('def workflow(host, mock):\n')
            output.write('    web_resolver = Resolver(host, mock)\n')
            for x in tree:
                output.write(f'{x.convert(4)}\n')
        elif path.suffix == '.go':
            output.write(f'package {path.stem}\n\nimport (\n\t"log"\n\t"time"\n\t"errors"\n\t"strconv"\n)\n\n')
            output.write('func main() {')
            #r = '\n'.join([x.convert() for x in tree])
            r = [f'{x.convert(4)}\n' for x in tree]
            #print(r)
            output.writelines(r)
            output.write('}')


def indent(i):
    return ' ' * (i + Scope.indent)

def return_py(self, i=0):
    if self.value is None:
        Scope.indent = Scope.indent - 4
        return ''#f'{indent(i+4)}return'
    else:
        return f'{indent(i)}return {self.value.convert(i)}'

def label_py(self, i=0):
    Scope.indent + 4
    return f'{indent(i-4)}# Sub\n' + f'{indent(i-4)}def sub_{self.name}():'

def label_go(self, i=0):
    Scope.indent + 4
    return f'{indent(i-4)}// Sub\nsub_{self.name}:'

def condition_py(self, i=0):
    s = (
        f'{indent(i)}if {self.conditions[0].convert(i)}:\n'
        + f'{self.blocks[0].convert(i+4)}\n'
    )
    for idx, c in enumerate(self.conditions[1:]):
        s += (
            f'{indent(i)}elif {c.convert(i)}:\n' +
            f'{self.blocks[idx+1].convert(i+4)}\n'
        )
    if self.else_block:
        s += f'{indent(i)}else:\n{self.else_block.convert(i+4)}'
    return s

def condition_go(self, i=0):
    s = (
        f'{indent(i)}if {self.conditions[0].convert(i)} {{\n'
        + f'{self.blocks[0].convert(i+4)}\n{indent(i)}}}\n'
    )
    for idx, c in enumerate(self.conditions[1:]):
        s += (
            f'{indent(i)}else if {c.convert(i)} {{\n' +
            f'{self.blocks[idx+1].convert(i+4)}\n{indent(i)}}}\n'
        )
    if self.else_block:
        s += f'{indent(i)}else {{\n{self.else_block.convert(i+4)}\n{indent(i)}}}'
    return s

def do_cycle_py(self, i=0):
    b = self.body.convert(i + 4)
    c = self.condition.convert(i)
    return (
        f'{indent(i)}while True:\n{b}'
        + f'\n{indent(i+4)}if {c}:\n{indent(i*3)}break\n'
    )

def do_cycle_go(self, i=0):
    b = self.body.convert(i + 4)
    c = self.condition.convert(i)
    return (
        f'{indent(i)}for ok := true; ok; ok = {c} {{{b}\n{indent(i)}}}'
    )

def error_py(self, i=0):
    s = self.node.value
    s = s if self.node.token.type == 'ID' else f'"{s}"'
    return f'raise Exception({s})'

def error_go(self, i=0):
    s = self.node.value
    s = s if self.node.token.type == 'ID' else f'"{s}"'
    return f'log.Fatal(errors.New({s}))'

def retry_py(self, i=0):
    b = self.body.convert(i * 3)
    c = self.condition.convert(i)
    return (
        f'{indent(i)}# Retry\n'
        + f'{indent(i)}tries = 0\n'
        + f'{indent(i)}while tries <= {self.tries.value} and \\\n'
        + f'{indent(i*3)}{c}:\n{indent(i+4)}try:\n{indent(i*3)}tries += 1\n{b}'
        + f'\n{indent(i+4)}except:\n{indent(i*3)}pass'
    )

def retry_go(self, i=0):
    b = self.body.convert(i * 2)
    c = self.condition.convert(i)
    return (
        f'{indent(i)}for tries := 0; tries <= {self.tries.value} && {c}'
        + f'; tries = tries + 1 {{\n{b}\n{indent(i)}}}'
    )

def struct_py(self, i=0):
    def _get_py(elem):
        return f'[{elem.right.value}]' if type(elem) == Array else f'["{elem.right.value}"]'
    indexes = _get_py(self)
    node = self.left
    while type(node) in (Array, Struct):
        indexes += _get_py(node)
        node = node.left
    return f'{node.value}{indexes}'



def declare_web_py(self, i=0):
    n = self.method.proc_name
    p = [x.value for x in self.method.actual_params]
    url = (
        f'{indent(i+4)}{n}.url = {self.method.url.convert(i)}\n'
        if self.method.url
        else ''
    )
    return (
        f'{indent(i)}def {n}('
        + f"{', '.join(p)}):\n{url}"
        + f'{indent(i+4)}return web_resolver.get({n}.url, "{n}")({", ".join(p)})\n'
    )

def procedure_call_py(self, i=0):
    from swodl_interpreter.inbuild_functions import functions
    n = self.proc_name
    if n in functions:
        func = functions[n]
        n = func.__name__
    s = f'{indent(i)}{n}.url = {self.url.convert(i)}\n' if self.url else ''
    return f"{s}{indent(i)}{n}({', '.join([str(x.convert(i)) for x in self.actual_params])})"

convertors = {
    '.py': {
        Bool: lambda x, _: repr(x.value),
        Id: lambda x, _: x.value,
        In: lambda x, _: x.name,
        Number: lambda x, _: x.value,
        Assign : lambda x, i:
            f"{indent(i)}{', '.join([x.convert(0) for x in x.left])} = {', '.join([str(x.convert(0)) for x in x.right])}" \
                if isinstance(x.op, Token) \
                else f"{indent(i)}{', '.join([x.name for x in x.left])}",
        Return: return_py,
        BinOp: lambda x, i: f'{x.left.convert(i)} {x.op} {x.right.convert(i)}',
        Label: label_py,
        Comment: lambda x, i: f"{indent(i)}'''{x.text}'''" if '\n' in str(x.text) else f'{indent(i)}# {x.text}',
        Compound: lambda self, i: f'\n'.join([x.convert(i) for x in filter(lambda x: type(x) != NoOp, self.children)]),
        Condition: condition_py,
        Cycle: lambda x, i: (
                f'{indent(i)}while {x.condition.convert(i)}:\n' +
                f'{x.body.convert(i+4)}'
            ),
        DoCycle: do_cycle_py,
        Delay: lambda x, i: f'{indent(i)}time.sleep({x.var.value})',
        Error: error_py,
        Throw: error_py,
        Exit: lambda x, i: f'{indent(i)}return',
        FunctionDecl: lambda x,i: f'{indent(i)}def {x.name}(' + f"{', '.join([x.value for x in x.params])}):\n{x.body.convert(i+4)}",
        SubCall: lambda x, i: f'{indent(i)}# GoSub\n' + f'{indent(i)}sub_{x.name}()\n',
        GoToCall: lambda x, i: f'{indent(i)}# GoTo !!! Please rewrite this !!!\n{indent(i)}sub_{x.name}!!!\n',
        Include: lambda x, i: f'from {x.name} import *',
        Status: lambda x, i: f'\n{indent(i)}status("{x.text}")\n',
        String: lambda x, i: repr(x.value),
        UnaryOp: lambda x, i: f'{x.op}({x.expr.convert(i)})' \
            if x.op in ('int', 'float', 'string', 'bool') \
            else f'not {x.expr.convert(i)}' \
                if x.op == '!' else f'{x.op}{x.expr.convert(i)}',
        Retry: retry_py,
        TryCatch: lambda x, i: (
            f'{indent(i)}try:\n{x.block.convert(i+4)}\n'
            + f"{indent(i)}except:\n{x.catch.convert(i+4) if len(x.catch.children) > 0 else indent(i+4)+'pass'}\n"
        ),
        Array: struct_py,
        Struct: struct_py,
        DeclareWeb: declare_web_py,
        ProcedureCall: procedure_call_py
    },
    '.go': {
        Bool: lambda x, _: str(x.value).lower(),
        Id: lambda x, _: x.value,
        In: lambda x, _: x.name,
        Number: lambda x, _: str(x.value),
        String: lambda x, _: f'"{x.value}"',
        Const: lambda x, i: f"const {', '.join([x.name for x in x.left])} = {', '.join([x.convert(0) for x in x.right])}",
        GoToCall: lambda x, _: f'goto {x.name}',
        Label: label_go,
        Assign : lambda x, i:
            f"{indent(i)}{', '.join([x.convert(0) for x in x.left])} {':=' if x.is_var else '='} {', '.join([x.convert(0) for x in x.right])}" \
                if isinstance(x.op, Token) \
                else f"{indent(i)}{'var ' if x.is_var else ''}{', '.join([x.name for x in x.left])}",
        Return: return_py,
        BinOp: lambda x, i: f'{x.left.convert(i)} {x.op} {x.right.convert(i)}',
        Comment: lambda x, i: f'{indent(i)}/*{str(x.text)}*/' if '\n' in str(x.text) else f'{indent(i)}{str(x.text)}',
        Compound: lambda self, i: f'\n'.join([x.convert(i) for x in filter(lambda x: type(x) != NoOp, self.children)]),
        Condition: condition_go,
        Cycle: lambda x, i: (
                f'{indent(i)}for {x.condition.convert(i)} {{\n' +
                f'{x.body.convert(i+4)}\n{indent(i)}}}'
            ),
        DoCycle: do_cycle_go,
        Delay: lambda x, i: f'{indent(i)}time.Sleep({x.var.value} * time.Second)',
        Error: error_go,
        Throw: error_go,
        Exit: lambda x, i: f'{indent(i)}return',
        FunctionDecl: lambda x, i: f'{indent(i)}func {x.name}(' + f"{', '.join([x.value for x in x.params])}) {{\n{x.body.convert(i+4)}\n}}",
        SubCall: lambda x, i: f'{indent(i)}goto sub_{x.name}\n{indent(i)}back_sub_{x.name}:',
        GoToCall: lambda x, i: f'{indent(i)}goto sub_{x.name}\n',
        Include: lambda x, i: f'->->->from {x.name} import *',
        Status: lambda x, i: f'\n{indent(i)}status("{x.text}")\n',
        String: lambda x, i: json.dumps(x.value),
        UnaryOp: lambda x, i: f'{x.op}({x.expr.convert(i)})' if x.op in ('strconv.ParseInt', 'strconv.ParseFloat', 'string', 'strconv.ParseBool') else f'{x.op}{x.expr.convert(i)}',
        Retry: retry_go
    }
}


# with open("tests/test.wf", "r") as f:
#     c = Converter(f.readlines())
#     #c.convert("tests/converted/test.py")
#     with open("tests/converted/test.py", "w") as fw:
#         c.convert(fw)
