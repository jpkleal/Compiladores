from base_structures import Bloc


class AsLong:
    def __init__(self):
        self.termo = None
        self.bloc = Bloc()

    def to_c(self):
        code = [f"while({self.termo.to_c()}){'{'}"]

        for cmd in self.bloc.to_c():
            code.append(cmd)

        code.append('}')

        return code

    def to_py(self):
        code = [f"while({self.termo.to_py()}):"]

        for cmd in self.bloc.to_py():
            code.append(cmd)

        return code
