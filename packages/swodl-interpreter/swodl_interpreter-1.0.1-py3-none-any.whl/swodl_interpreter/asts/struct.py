import xmltodict

from swodl_interpreter.storage import Scope


class Attr:
    def __init__(self, token) -> None:
        self.line = token.line
        self.name = token.name
        self.value = token.value

    def visit(self, _):
        return self.name


class Struct:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _try_parse_xml(self, s):
        try:
            return list(dict(xmltodict.parse(s)).items())[0][1]
        except:
            return s

    def _get_indexes(self, scope: Scope):
        indexes = []
        node = self
        while type(node) in (Array, Struct):
            indexes.insert(0, node.right.visit(scope))
            node = node.left
        indexes.insert(0, node.value)
        return indexes

    def visit(self, scope: Scope, value=''):
        val = scope.Global
        indexes = self._get_indexes(scope)
        for index in indexes:
            val = self._try_parse_xml(val)
            if val is None or (not isinstance(val, dict) and not isinstance(val, list)):
                root[prev_index] = StructType() if type(
                    index) == str else ArrayType()
                val = root[prev_index]
            root, prev_index = val, index
            if isinstance(val, dict) and type(index) == int:
                val = list(val.values())[0]
                val = val[index] if index < len(val) else ''
            else:
                val = val.get(index, None)
        if val is None:
            root[prev_index] = value
        return val or value


class Array(Struct):
    pass


class StructType(dict):
    def __getitem__(self, key):
        if key not in self:
            return None
        return dict(self)[key]

    def get(self, key, default=None):
        if default is not None:
            return super().get(key)
        return super().get(key, default)

    def __str__(self):
        str = ''.join([f'<{k}>{v}</{k}>' for k, v in self.items()])
        return f'<struct>{str}</struct>'


class ArrayType(list):
    def __init__(self, iter=None):
        if iter is not None:
            super().__init__(iter)
        else:
            super().__init__()
        self.values = {i: v for i, v in enumerate(iter or [])}

    def get(self, index, _=None):
        return self[index]

    def __getitem__(self, index):
        if int(index) not in self.values:
            self.values[int(index)] = None
        return self.values[int(index)]

    def __setitem__(self, index, value):
        self.values[index] = value
        super().__init__(self.values.values())

    def __str__(self):
        str = ''.join(
            [f'<item index="{i}">{v or ""}</item>' for i,
                v in self.values.items()]
        )
        return f'<itemsOfArray>{str}</itemsOfArray>'


class ThrowException(Exception):
    pass

class SwodlError(Exception):
    pass
