from antlr4 import *
from core import *

TARGETS = ['python', 'c']


def compiler(filename, path, target):

    lexer = IsiLanguageLexer(FileStream(f"{path}/{filename}"))
    token_stream = CommonTokenStream(lexer)
    parser = IsiLanguageParser(token_stream)

    tree = parser.prog()

    print(tree.toStringTree(recog=parser))
    parser.showIds()
    parser.verify_unused_variables()
    p = parser.program

    target_name = filename.split('.')[0]

    if target == 'c':
        target_name = f"{target_name}.c"
        with open(f"{path}/{target_name}", 'w') as f:
            f.write(p.gen_c_code())

    elif target == 'python':
        target_name = f"{target_name}.py"
        with open(f"{path}/{target_name}", 'w') as f:
            f.write(p.gen_python_code())

    else:
        raise Exception('Invalid target')

    return target_name
