from enum import Enum


OPERATIONS = (
    (),
    ('Neg', 'Comp', 'Ord', 'Add', 'Sub', 'Mul', 'Div', 'Log'),
    ('Comp', ),
    ('Neg', 'Comp', 'Log'),
)


class VarTypes(Enum):
    UNDEFINED = 0
    NUM = 1
    TEXT = 2
    BOOLEAN = 3

    def operations(self):
        return OPERATIONS[self.value]


INPUT_TYPES = {
    'NUM': VarTypes.NUM,
    'TEXTO': VarTypes.TEXT,
}
