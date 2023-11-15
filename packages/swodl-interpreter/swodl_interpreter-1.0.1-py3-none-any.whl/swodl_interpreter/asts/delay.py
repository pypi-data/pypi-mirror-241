import time


class Delay:
    def __init__(self, var):
        self.var = var

    def visit(self, _):
        time.sleep(self.var.value)
