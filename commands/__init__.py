from commands.assign import Assign
from commands.read import Read
from commands.write import Write

STR_TO_COMMAND = {
    'assign': Assign,
    'read': Read,
    'write': Write
}

__all__ = ['Assign', 'Read', 'Write', 'STR_TO_COMMAND']
