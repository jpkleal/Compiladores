from vartypes import VarTypes
from vartypes import Var
from commands import *


class Program:
    def __init__(self):
        self.symbol_table: list[Var] = []
        self.command = None

    def gen_c_code(self):
        vartype_to_c = {
            VarTypes.NUM: "float {name};",
            VarTypes.TEXT: "char {name}[32];"
        }

        code = "#include <stdio.h>\n\nint main() {\n"
        for symbol in self.symbol_table:
            code += f"\t{vartype_to_c[symbol.var_type].format(name=symbol.name)}\n"

        code += "\n".join(self.command.to_c())

        code += "\n\treturn 0;\n}"

        print(code)

    def gen_python_code(self):
        vartype_to_c = {
            VarTypes.NUM: "name:float",
            VarTypes.TEXT: "name:str"
        }

        code = ""
        # for symbol in self.symbol_table:
        #     code += f"{vartype_to_c[symbol.var_type].format(name=symbol.name)}\n"

        code += "\n".join(self.command.to_py())

        print(code)
