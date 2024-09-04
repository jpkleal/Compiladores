from vartypes import VarTypes


class Termo:
    def __init__(self):
        self.ops = []
        self.var_type = VarTypes.UNDEFINED

    def append(self, text):
        self.ops.append(text)

    def to_c(self):
        code = ""
        for op in self.ops:
            if isinstance(op, str):
                code += op
            else:
                code += op.to_c()
        return code

    def to_py(self):
        code = ""
        for op in self.ops:
            if isinstance(op, str):
                code += op
            else:
                code += op.to_py()
        return code


class OP:
    op_to_c = {
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

    op_to_py = {
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

    def __init__(self, op):
        self.op = op

    def to_c(self):
        return self.op_to_c[self.op]

    def to_py(self):
        return self.op_to_py[self.op]
