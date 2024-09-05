from commands.assign import Assign
from commands.read import Read
from commands.write import Write
from commands.conditional import Conditional
from commands.dowhile import DoWhile
from commands.aslong import AsLong

STR_TO_COMMAND = {
    'assign': Assign,
    'read': Read,
    'write': Write,
    'if': Conditional,
    'dowhile': DoWhile,
    'while': AsLong
}

__all__ = ['Assign', 'Read', 'Write', 'Conditional', 'DoWhile', 'AsLong', 'STR_TO_COMMAND']
