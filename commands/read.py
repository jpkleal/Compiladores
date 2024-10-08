from vartypes import VarTypes


class Read:
    vartype_to_c = {
        VarTypes.NUM: "%f",
        VarTypes.TEXT: "%s",
        VarTypes.BOOL: "%d"
    }
    vartype_to_py = {
        VarTypes.NUM: "float",
        VarTypes.TEXT: "str",
        VarTypes.BOOL: "bool"
    }

    def __init__(self):
        self.assign_id = None

    def to_py(self):
        code = f"{self.assign_id.name} = {self.vartype_to_py[self.assign_id.var_type]}(input())"
        return code

    def to_c(self):
        code = f"scanf(\"{self.vartype_to_c[self.assign_id.var_type]}\", &{self.assign_id.name});"
        return code
