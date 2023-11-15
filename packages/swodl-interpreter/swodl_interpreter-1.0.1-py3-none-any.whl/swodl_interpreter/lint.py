import re
import sys, inspect
from collections.abc import Iterable
from inflection import camelize, tableize
from swodl_interpreter.asts import *
from swodl_interpreter.lexers import label
from swodl_interpreter.lexers.id import Id
from swodl_interpreter.lexers.bool import Bool
from swodl_interpreter.lexers.number import Number
from swodl_interpreter.lexers.keyword import In, Const

in_sub = False
sub_name = None

def const(x):
    name = x.left[0].name
    if re.match('^[A-Z_0-9]+$', name) is None:
        return f"Line: {x.line}. Issue: Const name '{name}' should be in upper case. -> {tableize(name).upper()}"

def assign(x):
    if type(x.left[0]).__name__ == 'Id':
        r = '^[IN|OUT]?_?{name}_\w+$' if in_sub else '^_?[A-Za-z0-9]+$'
        name = x.left[0].name
        if re.match(r, name) is None or \
            camelize(name) != name and camelize(name, False) != name:
            if in_sub:
                return f"Line: {x.line}. Issue: '{name}' should be sub var name. -> [IN|OUT|INTERNAL]_{sub_name}_{camelize(name, False)}"
            else:
                return f"Line: {x.line}. Issue: Var name '{name}' should be in camel case. -> {camelize(name, False)}"

def add_result(r, v):
    if type(v) == str:
        r.append(v)
    elif isinstance(v, Iterable):
        r.extend(v)

def sub(x, l):
    r = []
    global in_sub, sub_name
    sub_name = x.name
    in_sub = True
    for token in l:
        if type(token) == Return:
            break
        try:
            add_result(r, token.lint())
        except:
            print(token)
    in_sub = False
    sub_name = None
    return r

def _if(x):
    r = []
    for i, b in enumerate(x.blocks):
        if x.conditions[i].line == b.line:
            r.append(f'Line: {x.line}. Issue: {{ should be on the next line.')
        for token in b.children:
            add_result(r, token.lint())
    if x.else_block:
        for token in x.else_block.children:
            add_result(r, token.lint())
    return r

def cycle(x):
    r = []
    for token in x.body.children:
        add_result(r, token.lint())
    return r

def try_catch(x):
    r = []
    for token in x.block.children + x.catch.children:
        add_result(r, token.lint())
    return r

rules = {
    Const: const,
    Assign: assign,
    Label: sub,
    Condition: _if,
    Cycle: cycle,
    DoCycle: cycle,
    Retry: cycle,
    TryCatch: try_catch
}

for cls in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    cls[1].lint = rules[cls[1]] if cls[1] in rules else lambda *a, **k: None
