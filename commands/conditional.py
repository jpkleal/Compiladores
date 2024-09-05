from base_structures import Bloc


class Conditional:
    def __init__(self):
        self.termo = None
        self.bloc_1 = Bloc()
        self.bloc_2 = Bloc()

    def to_c(self):
        code = [f"if({self.termo.to_c()}){'{'}"]

        for cmd in self.bloc_1.to_c():
            code.append(cmd)

        code.append("}")

        if self.bloc_2 is not None:
            code.append('else {')

        for cmd in self.bloc_2.to_c():
            code.append(cmd)

        code.append("}")

        return code

    def to_py(self):
        code = [f"if({self.termo.to_py()}):"]

        for cmd in self.bloc_1.to_py():
            code.append(cmd)

        if self.bloc_2 is not None:
            code.append('else:')

        for cmd in self.bloc_2.to_c():
            code.append(cmd)

        return code
