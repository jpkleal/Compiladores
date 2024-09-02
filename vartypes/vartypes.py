from enum import Enum


ORDINAL = {
    0: False,
    1: True,
    2: False,
    3: False
}

DENIABLE = {
    0: False,
    1: True,
    2: False,
    3: True
}


class VarTypes(Enum):
    UNDEFINED = 0
    NUM = 1
    TEXT = 2
    BOOLEAN = 3

    def orderable(self):
        return ORDINAL[self.value]

    def deniable(self):
        return DENIABLE[self.value]