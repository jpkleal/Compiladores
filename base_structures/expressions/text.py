class Text:
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self

    def to_c(self):
        return self.val

    def to_py(self):
        return self.val

    def __repr__(self):
        return str(self.val)
