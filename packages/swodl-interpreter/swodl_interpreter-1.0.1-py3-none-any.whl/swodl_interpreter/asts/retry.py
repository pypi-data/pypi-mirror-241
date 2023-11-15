import time

from swodl_interpreter.storage import Scope
from swodl_interpreter.asts.execution_exception import ExecutionException


class Retry:
    def __init__(self, tries, condition, body):
        self.condition = condition
        self.body = body
        self.tries = tries

    def visit(self, scope: Scope):
        tries = 0
        while True:
            tries += 1
            try:
                for v in self.body.visit(scope):
                    yield v
                    if isinstance(v, ExecutionException):
                        time.sleep(scope.Global['_RetryDelay'])
            except Exception as e:
                scope.Global['_ExceptionMessage'] = str(e)
                time.sleep(scope.Global['_RetryDelay'])
            if not self.condition.visit(scope):
                break
            if tries >= self.tries.value:
                break
