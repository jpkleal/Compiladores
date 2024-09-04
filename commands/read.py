from vartypes import VarTypes


class Read:
    vartype_to_c = {
        VarTypes.NUM: "%f",
        VarTypes.TEXT: "%s",
        VarTypes.BOOLEAN: "%d"
    }

    def __init__(self):
        self.assign_id = None

    def to_py(self):
        code = f"{self.assign_id.name} = input()"
        return code

    def to_c(self):
        code = f"scanf(\"{self.vartype_to_c[self.assign_id.var_type]}\", &{self.assign_id.name});"
        return code
