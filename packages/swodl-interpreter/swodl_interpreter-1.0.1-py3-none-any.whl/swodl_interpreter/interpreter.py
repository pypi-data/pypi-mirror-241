from collections.abc import Iterable

from .inbuild_functions import *
from swodl_interpreter.storage import Scope
from .web_service_resolver import Resolver
from swodl_interpreter.asts import List, NoOp, Comment


class Interpreter:
    def __init__(self, parser, scope: Scope, host=None, include_dir=None, mock=None):
        self.parser = parser
        Scope.include_dir = include_dir
        Scope.web_resolver = Resolver(host, mock)
        self.scope = scope
        functions['config_get'] = Scope.web_resolver.get_config
        t = list(self.parser.parse())
        self.tree = List(filter(lambda x: type(x) not in (NoOp, Comment), t))

    def lines(self):
        return list(set(self.parser.lines))

    def interpret(self, from_line=0, to_line=float('inf')):
        if not isinstance(self.tree, Iterable):
            raise Exception(f'No visit method in {type(self.tree).__name__}')
        return self.tree.visit(self.scope, from_line, to_line)
