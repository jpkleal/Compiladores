from vartypes import VarTypes


class Write:
    vartype_to_c = {
        VarTypes.NUM: "%f",
        VarTypes.TEXT: "%s",
        VarTypes.BOOL: "%d"
    }

    def __init__(self):
        self.termo = None

    def to_py(self):
        code = f"print({self.termo.to_py()})"
        return code

    def to_c(self):
        code = [f"printf(\"{self.vartype_to_c[self.termo.var_type]}\\n\", {self.termo.to_c()});"]
        return code
