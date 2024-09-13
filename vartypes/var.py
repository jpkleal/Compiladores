from dataclasses import dataclass
from vartypes import VarTypes


@dataclass
class Var:
    var_type: VarTypes
    name: str
    initialized: bool = False

    def evaluate(self):
        return [self.name]

    def to_py(self):
        return self.name

    def to_c(self):
        return self.name
