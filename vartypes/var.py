from dataclasses import dataclass
from vartypes import VarTypes


@dataclass
class Var:
    var_type: VarTypes
    name: str
    initialized: bool = False
