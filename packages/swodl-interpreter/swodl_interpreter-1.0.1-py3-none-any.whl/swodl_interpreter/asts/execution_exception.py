class ExecutionException(Exception):
    def __str__(self):
        return self.args[0]
