# Generated from IsiLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from vartypes import *
from exceptions import SemanticException
from core import Program, Bloc, Termo, OP


def serializedATN():
    return [
        4,0,29,239,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,150,8,14,1,15,1,15,1,15,
        3,15,155,8,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,3,17,165,8,
        17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,177,8,
        19,1,20,3,20,180,8,20,1,20,5,20,183,8,20,10,20,12,20,186,9,20,1,
        21,1,21,5,21,190,8,21,10,21,12,21,193,9,21,1,21,1,21,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,
        22,212,8,22,1,23,4,23,215,8,23,11,23,12,23,216,1,23,1,23,4,23,221,
        8,23,11,23,12,23,222,3,23,225,8,23,1,24,1,24,1,24,1,25,1,25,1,26,
        1,26,1,27,1,27,1,28,1,28,1,28,1,28,0,0,29,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,
        35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,
        57,29,1,0,7,2,0,60,60,62,62,3,0,42,43,45,45,47,47,2,0,65,90,97,122,
        3,0,48,57,65,90,97,122,5,0,32,32,44,46,48,57,65,90,97,122,1,0,48,
        57,3,0,9,10,13,13,32,32,249,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,
        27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,
        37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,
        47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,
        57,1,0,0,0,1,59,1,0,0,0,3,61,1,0,0,0,5,63,1,0,0,0,7,72,1,0,0,0,9,
        80,1,0,0,0,11,88,1,0,0,0,13,93,1,0,0,0,15,101,1,0,0,0,17,104,1,0,
        0,0,19,110,1,0,0,0,21,116,1,0,0,0,23,122,1,0,0,0,25,131,1,0,0,0,
        27,136,1,0,0,0,29,149,1,0,0,0,31,154,1,0,0,0,33,156,1,0,0,0,35,164,
        1,0,0,0,37,166,1,0,0,0,39,176,1,0,0,0,41,179,1,0,0,0,43,187,1,0,
        0,0,45,211,1,0,0,0,47,214,1,0,0,0,49,226,1,0,0,0,51,229,1,0,0,0,
        53,231,1,0,0,0,55,233,1,0,0,0,57,235,1,0,0,0,59,60,5,44,0,0,60,2,
        1,0,0,0,61,62,5,58,0,0,62,4,1,0,0,0,63,64,5,112,0,0,64,65,5,114,
        0,0,65,66,5,111,0,0,66,67,5,103,0,0,67,68,5,114,0,0,68,69,5,97,0,
        0,69,70,5,109,0,0,70,71,5,97,0,0,71,6,1,0,0,0,72,73,5,102,0,0,73,
        74,5,105,0,0,74,75,5,109,0,0,75,76,5,112,0,0,76,77,5,114,0,0,77,
        78,5,111,0,0,78,79,5,103,0,0,79,8,1,0,0,0,80,81,5,100,0,0,81,82,
        5,101,0,0,82,83,5,99,0,0,83,84,5,108,0,0,84,85,5,97,0,0,85,86,5,
        114,0,0,86,87,5,101,0,0,87,10,1,0,0,0,88,89,5,108,0,0,89,90,5,101,
        0,0,90,91,5,105,0,0,91,92,5,97,0,0,92,12,1,0,0,0,93,94,5,101,0,0,
        94,95,5,115,0,0,95,96,5,99,0,0,96,97,5,114,0,0,97,98,5,101,0,0,98,
        99,5,118,0,0,99,100,5,97,0,0,100,14,1,0,0,0,101,102,5,115,0,0,102,
        103,5,101,0,0,103,16,1,0,0,0,104,105,5,101,0,0,105,106,5,110,0,0,
        106,107,5,116,0,0,107,108,5,97,0,0,108,109,5,111,0,0,109,18,1,0,
        0,0,110,111,5,115,0,0,111,112,5,101,0,0,112,113,5,110,0,0,113,114,
        5,97,0,0,114,115,5,111,0,0,115,20,1,0,0,0,116,117,5,102,0,0,117,
        118,5,105,0,0,118,119,5,109,0,0,119,120,5,115,0,0,120,121,5,101,
        0,0,121,22,1,0,0,0,122,123,5,101,0,0,123,124,5,110,0,0,124,125,5,
        113,0,0,125,126,5,117,0,0,126,127,5,97,0,0,127,128,5,110,0,0,128,
        129,5,116,0,0,129,130,5,111,0,0,130,24,1,0,0,0,131,132,5,102,0,0,
        132,133,5,97,0,0,133,134,5,99,0,0,134,135,5,97,0,0,135,26,1,0,0,
        0,136,137,5,102,0,0,137,138,5,105,0,0,138,139,5,109,0,0,139,140,
        5,102,0,0,140,141,5,97,0,0,141,142,5,99,0,0,142,143,5,97,0,0,143,
        28,1,0,0,0,144,150,7,0,0,0,145,146,5,60,0,0,146,150,5,61,0,0,147,
        148,5,62,0,0,148,150,5,61,0,0,149,144,1,0,0,0,149,145,1,0,0,0,149,
        147,1,0,0,0,150,30,1,0,0,0,151,152,5,79,0,0,152,155,5,85,0,0,153,
        155,5,69,0,0,154,151,1,0,0,0,154,153,1,0,0,0,155,32,1,0,0,0,156,
        157,5,78,0,0,157,158,5,65,0,0,158,159,5,79,0,0,159,34,1,0,0,0,160,
        161,5,33,0,0,161,165,5,61,0,0,162,163,5,61,0,0,163,165,5,61,0,0,
        164,160,1,0,0,0,164,162,1,0,0,0,165,36,1,0,0,0,166,167,7,1,0,0,167,
        38,1,0,0,0,168,169,5,78,0,0,169,170,5,85,0,0,170,177,5,77,0,0,171,
        172,5,84,0,0,172,173,5,69,0,0,173,174,5,88,0,0,174,175,5,84,0,0,
        175,177,5,79,0,0,176,168,1,0,0,0,176,171,1,0,0,0,177,40,1,0,0,0,
        178,180,7,2,0,0,179,178,1,0,0,0,180,184,1,0,0,0,181,183,7,3,0,0,
        182,181,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,
        185,42,1,0,0,0,186,184,1,0,0,0,187,191,5,34,0,0,188,190,7,4,0,0,
        189,188,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,
        192,194,1,0,0,0,193,191,1,0,0,0,194,195,5,34,0,0,195,44,1,0,0,0,
        196,197,5,86,0,0,197,198,5,101,0,0,198,199,5,114,0,0,199,200,5,100,
        0,0,200,201,5,97,0,0,201,202,5,100,0,0,202,203,5,101,0,0,203,204,
        5,105,0,0,204,205,5,114,0,0,205,212,5,111,0,0,206,207,5,70,0,0,207,
        208,5,97,0,0,208,209,5,108,0,0,209,210,5,115,0,0,210,212,5,111,0,
        0,211,196,1,0,0,0,211,206,1,0,0,0,212,46,1,0,0,0,213,215,7,5,0,0,
        214,213,1,0,0,0,215,216,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,
        217,224,1,0,0,0,218,220,5,46,0,0,219,221,7,5,0,0,220,219,1,0,0,0,
        221,222,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,225,1,0,0,0,
        224,218,1,0,0,0,224,225,1,0,0,0,225,48,1,0,0,0,226,227,5,58,0,0,
        227,228,5,61,0,0,228,50,1,0,0,0,229,230,5,40,0,0,230,52,1,0,0,0,
        231,232,5,41,0,0,232,54,1,0,0,0,233,234,5,46,0,0,234,56,1,0,0,0,
        235,236,7,6,0,0,236,237,1,0,0,0,237,238,6,28,0,0,238,58,1,0,0,0,
        14,0,149,154,164,176,179,182,184,189,191,211,216,222,224,1,6,0,0
    ]

class IsiLanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BEGIN = 3
    END = 4
    DECLARE = 5
    INPUT = 6
    OUTPUT = 7
    IF = 8
    THEN = 9
    ELSE = 10
    ENDIF = 11
    WHILE = 12
    DO = 13
    ENDDO = 14
    OP_ORD = 15
    OP_LOG_B = 16
    OP_LOG_U = 17
    OP_REL = 18
    OP_NUM = 19
    TYPE = 20
    ID = 21
    TEXTO = 22
    BOOL = 23
    NUM = 24
    ASSIGN = 25
    AP = 26
    FP = 27
    ENDCMD = 28
    WS = 29

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'programa'", "'fimprog'", "'declare'", "'leia'", 
            "'escreva'", "'se'", "'entao'", "'senao'", "'fimse'", "'enquanto'", 
            "'faca'", "'fimfaca'", "'NAO'", "':='", "'('", "')'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BEGIN", "END", "DECLARE", "INPUT", "OUTPUT", "IF", "THEN", 
            "ELSE", "ENDIF", "WHILE", "DO", "ENDDO", "OP_ORD", "OP_LOG_B", 
            "OP_LOG_U", "OP_REL", "OP_NUM", "TYPE", "ID", "TEXTO", "BOOL", 
            "NUM", "ASSIGN", "AP", "FP", "ENDCMD", "WS" ]

    ruleNames = [ "T__0", "T__1", "BEGIN", "END", "DECLARE", "INPUT", "OUTPUT", 
                  "IF", "THEN", "ELSE", "ENDIF", "WHILE", "DO", "ENDDO", 
                  "OP_ORD", "OP_LOG_B", "OP_LOG_U", "OP_REL", "OP_NUM", 
                  "TYPE", "ID", "TEXTO", "BOOL", "NUM", "ASSIGN", "AP", 
                  "FP", "ENDCMD", "WS" ]

    grammarFileName = "IsiLanguage.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


        self._symbol_table = {}
        self._bloc_stack = []
        self._last_assignment = None
        self._last_termo_type = VarTypes.UNDEFINED
        self._input_set_type = VarTypes.UNDEFINED
        self._first_p_type = VarTypes.UNDEFINED
        self._last_termo = None
        self.program = Program()

    def showIds(self):
        for key, vals in self._symbol_table.items():
            print(key, vals)

    def declare_var(self, var):
        self._check_duplicated_var(var)
        self._symbol_table[var]=Var(name=var, var_type=VarTypes.UNDEFINED)

    def assign_var(self, var):
        self._check_existing_var(var)
        self._symbol_table[var].initialized = True
        self._last_assignment = self._symbol_table[var]

    def acces_var(self, var):
        self._check_existing_var(var)
        self._check_initialized_var(var)

        self._last_termo_type = self._symbol_table[var].var_type

    def input_assignment_type(self):
        if self._last_assignment.var_type == VarTypes.UNDEFINED and self._input_set_type == VarTypes.UNDEFINED:
            raise SemanticException(f"Could Not Resolve Type For Input: {self._last_assignment.name}")

        if self._input_set_type != VarTypes.UNDEFINED:
            self._last_assignment.var_type = self._input_set_type

    def check_op(self, type, op):
        if op not in type.operations():
            raise SemanticException(f"Type Doesn't Support Operation: {type}, {op}")

    def check_2p_op(self, op):
        if self._last_termo_type != self._first_p_type:
            raise SemanticException(f"Can Not Operate On Diferent Types: {self._last_termo_type} {op} {self._first_p_type}")
        self.check_op(self._last_termo_type, op)

    def _check_existing_var(self, var):
        if var not in self._symbol_table:
            raise SemanticException(f"Undeclared Variable: {var}")

    def _check_duplicated_var(self, var):
        if var in self._symbol_table:
            raise SemanticException(f"Alredy Declared Variable: {var}")

    def _check_initialized_var(self, var):
        if var not in self._symbol_table or not self._symbol_table[var].initialized:
            raise SemanticException(f"Uninitialized Variable: {var}")

    def initialize(self, var):
        self._symbol_table[var].initialized = True
        return self._symbol_table[var]

    def verify_unused_variables(self):
        for key, vals in self._symbol_table.items():
            if not vals.initialized:
                raise SemanticException(f"Variable created and not used: {key}")

    def end_bloc(self):
        if len(self._bloc_stack) > 1:
            self._bloc_stack[-2].append(self._bloc_stack.pop(-1))

    @property
    def bloc(self):
        return self._bloc_stack[-1]

    def begin_termo(self):
        self._last_termo = Termo()

    def append_to_termo(self, text):
        self._last_termo.append(text)


