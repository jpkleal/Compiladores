import fileinput
import sys
from antlr4 import *
from core.IsiLanguageLexer import IsiLanguageLexer
from core.IsiLanguageParser import IsiLanguageParser

# input_text = input("> ")
lexer = IsiLanguageLexer(FileStream('input.isi'))
token_stream = CommonTokenStream(lexer)
parser = IsiLanguageParser(token_stream)

tree = parser.prog()

print(tree.toStringTree(recog=parser))
parser.showIds()
parser.verify_unused_variables()
