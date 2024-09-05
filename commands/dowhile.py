from base_structures import Bloc


class DoWhile:
    def __init__(self):
        self.termo = None
        self.bloc = Bloc(first=True)

    def to_c(self):
        code = ["do {"]

        for cmd in self.bloc.to_c():
            code.append(cmd)

        code.append(f"{'}'} while({self.termo.to_c()});")

        return code

    def to_py(self):
        code = []
        for cmd in self.bloc.to_py():
            code.append(cmd)

        code.append(f"while({self.termo.to_py()}):")
        self.bloc.first = False

        for cmd in self.bloc.to_py():
            code.append(cmd)

        return code
