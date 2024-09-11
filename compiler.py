import fileinput
import sys
from antlr4 import *
from core import *

# input_text = input("> ")
lexer = IsiLanguageLexer(FileStream('input.isi'))
token_stream = CommonTokenStream(lexer)
parser = IsiLanguageParser(token_stream)

tree = parser.prog()

print(tree.toStringTree(recog=parser))
parser.showIds()
parser.verify_unused_variables()
p = parser.program
print("----------")
print("C: \n")
p.gen_c_code()

print("\n")
print("---------")
print("Python: \n")
p.gen_python_code()
