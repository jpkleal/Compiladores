from vartypes import Var
from base_structures.expressions.num import Num
from base_structures.expressions.boolean import Boolean

precedence = {
    '+': 5,
    '-': 5,
    '*': 6,
    '/': 6,
    '>': 4,
    '<': 4,
    '>=': 4,
    '<=': 4,
    'OU': 1,
    'E': 2,
    'NAO': 3,
    '==': 4,
    '!=': 4
}

post_operation_type = {
    '+': Num,
    '-': Num,
    '*': Num,
    '/': Num,
    '>': Boolean,
    '<': Boolean,
    '>=': Boolean,
    '<=': Boolean,
    'OU': Boolean,
    'E': Boolean,
    'NAO': Boolean,
    '==': Boolean,
    '!=': Boolean
}

to_c = {
    '+': "+",
    '-': "-",
    '*': '*',
    '/': '/',
    '>': '>',
    '<': '<',
    '>=': '>=',
    '<=': '<=',
    'OU': '||',
    'E': '&&',
    'NAO': '!',
    '==': '==',
    '!=': '!=',
    'ap': '(',
    'fp': ')'
}

to_py = {
    '+': "+",
    '-': "-",
    '*': '*',
    '/': '/',
    '>': '>',
    '<': '<',
    '>=': '>=',
    '<=': '<=',
    'OU': 'or',
    'E': 'and',
    'NAO': 'not',
    '==': '==',
    '!=': '!=',
    'ap': '(',
    'fp': ')'
}

class OP:
    def __init__(self, op):
        self.op = op
        self.left = None
        self._right = None

    def __repr__(self):
        return "(" + repr(self.left) + self.op + repr(self.right) + ")"

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        if isinstance(self._right, OP):
            self._right.right = value
        else:
            self._right = value

    def evaluate(self):
        if self.left is None:
            return self.unary_evaluate()

        l = self.left.evaluate()
        r = self.right.evaluate()

        if not isinstance(l, list) and not isinstance(r, list):
            new_val = eval(f"{l.to_py()} {self.to_py()} {r.to_py()}")
            return self.operate(new_val)

        else:
            l = [l] if not isinstance(l, list) else l
            r = [r] if not isinstance(r, list) else r

            out = []
            out.extend(l)
            out.append(self)
            out.extend(r)
            return out

    def unary_evaluate(self):
        r = self.right.evaluate()

        if not isinstance(r, list):
            new_val = eval(f"{self.to_py()} {r.to_py()}")
            return self.operate(new_val)

        else:
            r = [r] if not isinstance(r, list) else r

            out = [self]
            out.extend(r)
            return out

    def operate(self, val):
        nt = post_operation_type[self.op]
        if nt == Boolean:
            val = 'Verdadeiro' if val else 'Falso'
        return nt(val)

    def to_c(self):
        return to_c[self.op]

    def to_py(self):
        return to_py[self.op]

    @property
    def precedence(self):
        return precedence[self.op]
