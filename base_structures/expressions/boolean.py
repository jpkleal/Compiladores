to_c = {
    'Falso': '0',
    'Verdadeiro': '1'
}

to_py = {
    'Falso': 'False',
    'Verdadeiro': 'True'
}


class Boolean:
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self

    def to_c(self):
        return to_c[self.val]

    def to_py(self):
        return to_py[self.val]

    def __repr__(self):
        return str(self.val)