class String: # TODO: move to default types
    def __init__(self, value, token):
        self.token = token
        self.value = value

    def visit(self, _=None):
        return self.value
