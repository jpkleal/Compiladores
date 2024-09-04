class Assign:
    def __init__(self):
        self.assign_id = None
        self.termo = None

    def to_py(self):
        code = f"{self.assign_id.name} = {self.termo.to_py()}"
        return code

    def to_c(self):
        code = f"{self.assign_id.name} = {self.termo.to_c()};"
        return code
