from commands import *


class Bloc:
    def __init__(self, first=False):
        self.commands = []
        self.first = first

    def append(self, cmd):
        if isinstance(cmd, Bloc):
            self.commands.append(cmd)
            return

        self.commands.append(STR_TO_COMMAND[cmd]())

    def to_c(self):
        code = []
        for i in self.commands:
            sub_commands = i.to_c()
            if isinstance(sub_commands, str):
                code.append("\t"+sub_commands)
            else:
                for j in sub_commands:
                    code.append("\t"+j)

        return code

    def to_py(self):
        code = []
        for i in self.commands:
            sub_commands = i.to_py()
            if isinstance(sub_commands, str):
                if self.first:
                    code.append(sub_commands)
                else:
                    code.append("\t"+sub_commands)
            else:
                for j in sub_commands:
                    if self.first:
                        code.append(j)
                    else:
                        code.append("\t"+j)

        return code

    @property
    def command(self):
        return self.commands[-1]
