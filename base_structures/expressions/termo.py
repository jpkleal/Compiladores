from vartypes import VarTypes, Var
from base_structures.expressions.operator import OP

class Termo:
    def __init__(self, root=True):
        self.ops = []
        self._stack = []
        self.var_type = VarTypes.UNDEFINED
        self.root = root
        self.evaluated = False
        self.val = None
        self.closed = False

    def append(self, text):
        # First item in the operation
        if len(self._stack) == 0:
            if isinstance(text, OP) and text.op == 'ap':
                self._stack.append(Termo(False))
                return
            self._stack.append(text)
            return

        # Dealing with parenthesis
        if isinstance(text, OP) and text.op == 'ap':
            self._stack.append(Termo(False))
            return

        li = self._stack.pop()

        if isinstance(text, OP) and text.op == 'fp':
            li.closed = True
            self._stack.append(li)
            return

        if isinstance(li, Termo) and not li.closed:
            li.append(text)
            self._stack.append(li)
            return

        # Adding an OP
        if isinstance(text, OP):

            # OP in Stack
            if isinstance(li, OP):

                # Stack OP has higher precedence (ex. op(8+8) * )
                if li.precedence < text.precedence:
                    text.left = li.right
                    li.right = text
                    self._stack.append(li)
                    return

                # Stack OP has lower or equal precedence (ex. op(8-8) + )
                else:
                    text.left = li
                    self._stack.append(text)
                    return

            # Stack has a Value or Var
            text.left = li
            self._stack.append(text)
            return

        # Value or Var (not an op)
        li.right = text
        self._stack.append(li)

    def evaluate(self):
        if self.evaluated:
            return self.val

        head = self._stack.pop()
        new_val = head.evaluate()
        if isinstance(new_val, list):
            out = [] if self.root else [OP('ap')]
            out.extend(new_val)
            if not self.root:
                out.append(OP('fp'))
            self.val = out
            self.evaluated = True
            return out

        self.val = new_val
        self.evaluated = True
        return new_val

    def to_c(self):
        ops = self.evaluate()
        code = ""
        if isinstance(ops, list):
            for op in ops:
                if isinstance(op, str):
                    code += op
                else:
                    code += op.to_c()
            return code
        else:
            return ops.to_c()

    def to_py(self):
        ops = self.evaluate()
        code = ""
        if isinstance(ops, list):
            for op in ops:
                if isinstance(op, str):
                    code += op
                else:
                    code += op.to_py()
            return code
        else:
            return ops.to_py()

