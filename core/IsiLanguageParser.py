# Generated from IsiLanguage.g4 by ANTLR 4.13.2
# encoding: utf-8
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
        4,1,29,214,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,4,3,60,8,3,11,3,12,3,61,1,3,1,3,1,4,1,4,1,4,3,4,69,8,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,81,8,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,9,1,9,1,9,3,9,107,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,3,10,117,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,164,8,14,1,
        14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,174,8,15,10,15,12,15,
        177,9,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,185,8,15,10,15,12,15,
        188,9,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,196,8,15,10,15,12,15,
        199,9,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,207,8,15,10,15,12,15,
        210,9,15,3,15,212,8,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,0,0,218,0,32,1,0,0,0,2,40,1,0,0,0,4,51,1,0,0,0,6,54,
        1,0,0,0,8,68,1,0,0,0,10,70,1,0,0,0,12,85,1,0,0,0,14,92,1,0,0,0,16,
        100,1,0,0,0,18,106,1,0,0,0,20,108,1,0,0,0,22,120,1,0,0,0,24,128,
        1,0,0,0,26,136,1,0,0,0,28,163,1,0,0,0,30,211,1,0,0,0,32,33,5,3,0,
        0,33,34,3,2,1,0,34,35,3,6,3,0,35,36,5,4,0,0,36,37,5,28,0,0,37,38,
        6,0,-1,0,38,39,6,0,-1,0,39,1,1,0,0,0,40,41,5,5,0,0,41,46,3,4,2,0,
        42,43,5,1,0,0,43,45,3,4,2,0,44,42,1,0,0,0,45,48,1,0,0,0,46,44,1,
        0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,28,0,0,50,
        3,1,0,0,0,51,52,5,21,0,0,52,53,6,2,-1,0,53,5,1,0,0,0,54,59,6,3,-1,
        0,55,56,3,8,4,0,56,57,5,28,0,0,57,60,1,0,0,0,58,60,3,18,9,0,59,55,
        1,0,0,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,
        62,63,1,0,0,0,63,64,6,3,-1,0,64,7,1,0,0,0,65,69,3,10,5,0,66,69,3,
        12,6,0,67,69,3,14,7,0,68,65,1,0,0,0,68,66,1,0,0,0,68,67,1,0,0,0,
        69,9,1,0,0,0,70,71,5,6,0,0,71,72,6,5,-1,0,72,73,6,5,-1,0,73,74,5,
        26,0,0,74,75,3,16,8,0,75,76,6,5,-1,0,76,80,6,5,-1,0,77,78,5,2,0,
        0,78,79,5,20,0,0,79,81,6,5,-1,0,80,77,1,0,0,0,80,81,1,0,0,0,81,82,
        1,0,0,0,82,83,6,5,-1,0,83,84,5,27,0,0,84,11,1,0,0,0,85,86,5,7,0,
        0,86,87,6,6,-1,0,87,88,5,26,0,0,88,89,3,26,13,0,89,90,6,6,-1,0,90,
        91,5,27,0,0,91,13,1,0,0,0,92,93,3,16,8,0,93,94,5,25,0,0,94,95,6,
        7,-1,0,95,96,6,7,-1,0,96,97,3,26,13,0,97,98,6,7,-1,0,98,99,6,7,-1,
        0,99,15,1,0,0,0,100,101,5,21,0,0,101,102,6,8,-1,0,102,17,1,0,0,0,
        103,107,3,20,10,0,104,107,3,22,11,0,105,107,3,24,12,0,106,103,1,
        0,0,0,106,104,1,0,0,0,106,105,1,0,0,0,107,19,1,0,0,0,108,109,5,8,
        0,0,109,110,5,26,0,0,110,111,3,26,13,0,111,112,5,27,0,0,112,113,
        5,9,0,0,113,116,3,6,3,0,114,115,5,10,0,0,115,117,3,6,3,0,116,114,
        1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,11,0,0,119,21,
        1,0,0,0,120,121,5,12,0,0,121,122,5,26,0,0,122,123,3,26,13,0,123,
        124,5,27,0,0,124,125,5,13,0,0,125,126,3,6,3,0,126,127,5,14,0,0,127,
        23,1,0,0,0,128,129,5,13,0,0,129,130,3,6,3,0,130,131,5,14,0,0,131,
        132,5,12,0,0,132,133,5,26,0,0,133,134,3,28,14,0,134,135,5,27,0,0,
        135,25,1,0,0,0,136,137,6,13,-1,0,137,138,3,28,14,0,138,139,6,13,
        -1,0,139,27,1,0,0,0,140,141,5,21,0,0,141,142,6,14,-1,0,142,164,6,
        14,-1,0,143,144,5,24,0,0,144,145,6,14,-1,0,145,164,6,14,-1,0,146,
        147,5,22,0,0,147,148,6,14,-1,0,148,164,6,14,-1,0,149,150,5,23,0,
        0,150,151,6,14,-1,0,151,164,6,14,-1,0,152,153,5,26,0,0,153,154,6,
        14,-1,0,154,155,3,28,14,0,155,156,5,27,0,0,156,157,6,14,-1,0,157,
        164,1,0,0,0,158,159,5,17,0,0,159,160,6,14,-1,0,160,161,3,28,14,0,
        161,162,6,14,-1,0,162,164,1,0,0,0,163,140,1,0,0,0,163,143,1,0,0,
        0,163,146,1,0,0,0,163,149,1,0,0,0,163,152,1,0,0,0,163,158,1,0,0,
        0,164,165,1,0,0,0,165,166,3,30,15,0,166,29,1,0,0,0,167,168,6,15,
        -1,0,168,169,5,19,0,0,169,170,6,15,-1,0,170,171,3,28,14,0,171,172,
        6,15,-1,0,172,174,1,0,0,0,173,167,1,0,0,0,174,177,1,0,0,0,175,173,
        1,0,0,0,175,176,1,0,0,0,176,212,1,0,0,0,177,175,1,0,0,0,178,179,
        6,15,-1,0,179,180,5,16,0,0,180,181,6,15,-1,0,181,182,3,28,14,0,182,
        183,6,15,-1,0,183,185,1,0,0,0,184,178,1,0,0,0,185,188,1,0,0,0,186,
        184,1,0,0,0,186,187,1,0,0,0,187,212,1,0,0,0,188,186,1,0,0,0,189,
        190,6,15,-1,0,190,191,5,15,0,0,191,192,6,15,-1,0,192,193,3,28,14,
        0,193,194,6,15,-1,0,194,196,1,0,0,0,195,189,1,0,0,0,196,199,1,0,
        0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,212,1,0,0,0,199,197,1,0,
        0,0,200,201,6,15,-1,0,201,202,5,18,0,0,202,203,6,15,-1,0,203,204,
        3,28,14,0,204,205,6,15,-1,0,205,207,1,0,0,0,206,200,1,0,0,0,207,
        210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,212,1,0,0,0,210,
        208,1,0,0,0,211,175,1,0,0,0,211,186,1,0,0,0,211,197,1,0,0,0,211,
        208,1,0,0,0,212,31,1,0,0,0,13,46,59,61,68,80,106,116,163,175,186,
        197,208,211
    ]

class IsiLanguageParser ( Parser ):

    grammarFileName = "IsiLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'programa'", "'fimprog'", 
                     "'declare'", "'leia'", "'escreva'", "'se'", "'entao'", 
                     "'senao'", "'fimse'", "'enquanto'", "'faca'", "'fimfaca'", 
                     "<INVALID>", "<INVALID>", "'NAO'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "':='", "'('", "')'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "BEGIN", "END", 
                      "DECLARE", "INPUT", "OUTPUT", "IF", "THEN", "ELSE", 
                      "ENDIF", "WHILE", "DO", "ENDDO", "OP_ORD", "OP_LOG_B", 
                      "OP_LOG_U", "OP_REL", "OP_NUM", "TYPE", "ID", "TEXTO", 
                      "BOOL", "NUM", "ASSIGN", "AP", "FP", "ENDCMD", "WS" ]

    RULE_prog = 0
    RULE_declara = 1
    RULE_declaral = 2
    RULE_bloco = 3
    RULE_cmd = 4
    RULE_cmdLeitura = 5
    RULE_cmdEscrita = 6
    RULE_cmdAssign = 7
    RULE_assignId = 8
    RULE_ctrlFluxo = 9
    RULE_ctrlIF = 10
    RULE_ctrlWhile = 11
    RULE_ctrlDoWhile = 12
    RULE_new_termo = 13
    RULE_termo = 14
    RULE_termol = 15

    ruleNames =  [ "prog", "declara", "declaral", "bloco", "cmd", "cmdLeitura", 
                   "cmdEscrita", "cmdAssign", "assignId", "ctrlFluxo", "ctrlIF", 
                   "ctrlWhile", "ctrlDoWhile", "new_termo", "termo", "termol" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    BEGIN=3
    END=4
    DECLARE=5
    INPUT=6
    OUTPUT=7
    IF=8
    THEN=9
    ELSE=10
    ENDIF=11
    WHILE=12
    DO=13
    ENDDO=14
    OP_ORD=15
    OP_LOG_B=16
    OP_LOG_U=17
    OP_REL=18
    OP_NUM=19
    TYPE=20
    ID=21
    TEXTO=22
    BOOL=23
    NUM=24
    ASSIGN=25
    AP=26
    FP=27
    ENDCMD=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
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



    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(IsiLanguageParser.BEGIN, 0)

        def declara(self):
            return self.getTypedRuleContext(IsiLanguageParser.DeclaraContext,0)


        def bloco(self):
            return self.getTypedRuleContext(IsiLanguageParser.BlocoContext,0)


        def END(self):
            return self.getToken(IsiLanguageParser.END, 0)

        def ENDCMD(self):
            return self.getToken(IsiLanguageParser.ENDCMD, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = IsiLanguageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(IsiLanguageParser.BEGIN)
            self.state = 33
            self.declara()
            self.state = 34
            self.bloco()
            self.state = 35
            self.match(IsiLanguageParser.END)
            self.state = 36
            self.match(IsiLanguageParser.ENDCMD)
            self.program.symbol_table=self._symbol_table.values()
            self.program.set_command(self._bloc_stack[0])
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(IsiLanguageParser.DECLARE, 0)

        def declaral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.DeclaralContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.DeclaralContext,i)


        def ENDCMD(self):
            return self.getToken(IsiLanguageParser.ENDCMD, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_declara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclara" ):
                listener.enterDeclara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclara" ):
                listener.exitDeclara(self)




    def declara(self):

        localctx = IsiLanguageParser.DeclaraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declara)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(IsiLanguageParser.DECLARE)
            self.state = 41
            self.declaral()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 42
                self.match(IsiLanguageParser.T__0)
                self.state = 43
                self.declaral()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(IsiLanguageParser.ENDCMD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_declaral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaral" ):
                listener.enterDeclaral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaral" ):
                listener.exitDeclaral(self)




    def declaral(self):

        localctx = IsiLanguageParser.DeclaralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(IsiLanguageParser.ID)
            self.declare_var(self._input.LT(-1).text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ctrlFluxo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.CtrlFluxoContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.CtrlFluxoContext,i)


        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.CmdContext,i)


        def ENDCMD(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.ENDCMD)
            else:
                return self.getToken(IsiLanguageParser.ENDCMD, i)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)




    def bloco(self):

        localctx = IsiLanguageParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self._bloc_stack.append(Bloc())
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 7, 21]:
                    self.state = 55
                    self.cmd()
                    self.state = 56
                    self.match(IsiLanguageParser.ENDCMD)
                    pass
                elif token in [8, 12, 13]:
                    self.state = 58
                    self.ctrlFluxo()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2109888) != 0)):
                    break

            self.end_bloc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdLeitura(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdLeituraContext,0)


        def cmdEscrita(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdEscritaContext,0)


        def cmdAssign(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdAssignContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = IsiLanguageParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cmd)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.cmdLeitura()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.cmdEscrita()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.cmdAssign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdLeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(IsiLanguageParser.INPUT, 0)

        def AP(self):
            return self.getToken(IsiLanguageParser.AP, 0)

        def assignId(self):
            return self.getTypedRuleContext(IsiLanguageParser.AssignIdContext,0)


        def FP(self):
            return self.getToken(IsiLanguageParser.FP, 0)

        def TYPE(self):
            return self.getToken(IsiLanguageParser.TYPE, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdLeitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdLeitura" ):
                listener.enterCmdLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdLeitura" ):
                listener.exitCmdLeitura(self)




    def cmdLeitura(self):

        localctx = IsiLanguageParser.CmdLeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cmdLeitura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(IsiLanguageParser.INPUT)
            self.bloc.append("read")
            self._input_set_type=VarTypes.UNDEFINED
            self.state = 73
            self.match(IsiLanguageParser.AP)
            self.state = 74
            self.assignId()
            self.initialize(self._input.LT(-1).text)
            self.bloc.command.assign_id=self._last_assignment
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 77
                self.match(IsiLanguageParser.T__1)
                self.state = 78
                self.match(IsiLanguageParser.TYPE)
                self._input_set_type=INPUT_TYPES[self._input.LT(-1).text]


            self.input_assignment_type()
            self.state = 83
            self.match(IsiLanguageParser.FP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdEscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(IsiLanguageParser.OUTPUT, 0)

        def AP(self):
            return self.getToken(IsiLanguageParser.AP, 0)

        def new_termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.New_termoContext,0)


        def FP(self):
            return self.getToken(IsiLanguageParser.FP, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdEscrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdEscrita" ):
                listener.enterCmdEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdEscrita" ):
                listener.exitCmdEscrita(self)




    def cmdEscrita(self):

        localctx = IsiLanguageParser.CmdEscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmdEscrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(IsiLanguageParser.OUTPUT)
            self.bloc.append("write")
            self.state = 87
            self.match(IsiLanguageParser.AP)
            self.state = 88
            self.new_termo()
            self.bloc.command.termo=self._last_termo
            self.state = 90
            self.match(IsiLanguageParser.FP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignId(self):
            return self.getTypedRuleContext(IsiLanguageParser.AssignIdContext,0)


        def ASSIGN(self):
            return self.getToken(IsiLanguageParser.ASSIGN, 0)

        def new_termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.New_termoContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdAssign" ):
                listener.enterCmdAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdAssign" ):
                listener.exitCmdAssign(self)




    def cmdAssign(self):

        localctx = IsiLanguageParser.CmdAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmdAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.assignId()
            self.state = 93
            self.match(IsiLanguageParser.ASSIGN)
            self.bloc.append("assign")
            self.bloc.command.assign_id=self._last_assignment
            self.state = 96
            self.new_termo()
            self._last_assignment.var_type = self._last_termo_type
            self.bloc.command.termo=self._last_termo
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_assignId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignId" ):
                listener.enterAssignId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignId" ):
                listener.exitAssignId(self)




    def assignId(self):

        localctx = IsiLanguageParser.AssignIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(IsiLanguageParser.ID)
            self.assign_var(self._input.LT(-1).text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtrlFluxoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ctrlIF(self):
            return self.getTypedRuleContext(IsiLanguageParser.CtrlIFContext,0)


        def ctrlWhile(self):
            return self.getTypedRuleContext(IsiLanguageParser.CtrlWhileContext,0)


        def ctrlDoWhile(self):
            return self.getTypedRuleContext(IsiLanguageParser.CtrlDoWhileContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_ctrlFluxo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtrlFluxo" ):
                listener.enterCtrlFluxo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtrlFluxo" ):
                listener.exitCtrlFluxo(self)




    def ctrlFluxo(self):

        localctx = IsiLanguageParser.CtrlFluxoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ctrlFluxo)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.ctrlIF()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.ctrlWhile()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.ctrlDoWhile()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtrlIFContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(IsiLanguageParser.IF, 0)

        def AP(self):
            return self.getToken(IsiLanguageParser.AP, 0)

        def new_termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.New_termoContext,0)


        def FP(self):
            return self.getToken(IsiLanguageParser.FP, 0)

        def THEN(self):
            return self.getToken(IsiLanguageParser.THEN, 0)

        def bloco(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.BlocoContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.BlocoContext,i)


        def ENDIF(self):
            return self.getToken(IsiLanguageParser.ENDIF, 0)

        def ELSE(self):
            return self.getToken(IsiLanguageParser.ELSE, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_ctrlIF

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtrlIF" ):
                listener.enterCtrlIF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtrlIF" ):
                listener.exitCtrlIF(self)




    def ctrlIF(self):

        localctx = IsiLanguageParser.CtrlIFContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ctrlIF)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(IsiLanguageParser.IF)
            self.state = 109
            self.match(IsiLanguageParser.AP)
            self.state = 110
            self.new_termo()
            self.state = 111
            self.match(IsiLanguageParser.FP)
            self.state = 112
            self.match(IsiLanguageParser.THEN)
            self.state = 113
            self.bloco()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 114
                self.match(IsiLanguageParser.ELSE)
                self.state = 115
                self.bloco()


            self.state = 118
            self.match(IsiLanguageParser.ENDIF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtrlWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(IsiLanguageParser.WHILE, 0)

        def AP(self):
            return self.getToken(IsiLanguageParser.AP, 0)

        def new_termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.New_termoContext,0)


        def FP(self):
            return self.getToken(IsiLanguageParser.FP, 0)

        def DO(self):
            return self.getToken(IsiLanguageParser.DO, 0)

        def bloco(self):
            return self.getTypedRuleContext(IsiLanguageParser.BlocoContext,0)


        def ENDDO(self):
            return self.getToken(IsiLanguageParser.ENDDO, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_ctrlWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtrlWhile" ):
                listener.enterCtrlWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtrlWhile" ):
                listener.exitCtrlWhile(self)




    def ctrlWhile(self):

        localctx = IsiLanguageParser.CtrlWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ctrlWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(IsiLanguageParser.WHILE)
            self.state = 121
            self.match(IsiLanguageParser.AP)
            self.state = 122
            self.new_termo()
            self.state = 123
            self.match(IsiLanguageParser.FP)
            self.state = 124
            self.match(IsiLanguageParser.DO)
            self.state = 125
            self.bloco()
            self.state = 126
            self.match(IsiLanguageParser.ENDDO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtrlDoWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(IsiLanguageParser.DO, 0)

        def bloco(self):
            return self.getTypedRuleContext(IsiLanguageParser.BlocoContext,0)


        def ENDDO(self):
            return self.getToken(IsiLanguageParser.ENDDO, 0)

        def WHILE(self):
            return self.getToken(IsiLanguageParser.WHILE, 0)

        def AP(self):
            return self.getToken(IsiLanguageParser.AP, 0)

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


        def FP(self):
            return self.getToken(IsiLanguageParser.FP, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_ctrlDoWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtrlDoWhile" ):
                listener.enterCtrlDoWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtrlDoWhile" ):
                listener.exitCtrlDoWhile(self)




    def ctrlDoWhile(self):

        localctx = IsiLanguageParser.CtrlDoWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ctrlDoWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(IsiLanguageParser.DO)
            self.state = 129
            self.bloco()
            self.state = 130
            self.match(IsiLanguageParser.ENDDO)
            self.state = 131
            self.match(IsiLanguageParser.WHILE)
            self.state = 132
            self.match(IsiLanguageParser.AP)
            self.state = 133
            self.termo()
            self.state = 134
            self.match(IsiLanguageParser.FP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class New_termoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_new_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNew_termo" ):
                listener.enterNew_termo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNew_termo" ):
                listener.exitNew_termo(self)




    def new_termo(self):

        localctx = IsiLanguageParser.New_termoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_new_termo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.begin_termo()
            self.state = 137
            self.termo()
            self._last_termo.var_type=self._last_termo_type
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termol(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermolContext,0)


        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def NUM(self):
            return self.getToken(IsiLanguageParser.NUM, 0)

        def TEXTO(self):
            return self.getToken(IsiLanguageParser.TEXTO, 0)

        def BOOL(self):
            return self.getToken(IsiLanguageParser.BOOL, 0)

        def AP(self):
            return self.getToken(IsiLanguageParser.AP, 0)

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


        def FP(self):
            return self.getToken(IsiLanguageParser.FP, 0)

        def OP_LOG_U(self):
            return self.getToken(IsiLanguageParser.OP_LOG_U, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = IsiLanguageParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_termo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 140
                self.match(IsiLanguageParser.ID)
                self.acces_var(self._input.LT(-1).text)
                self.append_to_termo(self._input.LT(-1).text)
                pass
            elif token in [24]:
                self.state = 143
                self.match(IsiLanguageParser.NUM)
                self._last_termo_type=VarTypes.NUM
                self.append_to_termo(self._input.LT(-1).text)
                pass
            elif token in [22]:
                self.state = 146
                self.match(IsiLanguageParser.TEXTO)
                self._last_termo_type=VarTypes.TEXT
                self.append_to_termo(self._input.LT(-1).text)
                pass
            elif token in [23]:
                self.state = 149
                self.match(IsiLanguageParser.BOOL)
                self._last_termo_type=VarTypes.BOOL
                self.append_to_termo(self._input.LT(-1).text)
                pass
            elif token in [26]:
                self.state = 152
                self.match(IsiLanguageParser.AP)
                self.append_to_termo(OP('ap'))
                self.state = 154
                self.termo()
                self.state = 155
                self.match(IsiLanguageParser.FP)
                self.append_to_termo(OP('fp'))
                pass
            elif token in [17]:
                self.state = 158
                self.match(IsiLanguageParser.OP_LOG_U)
                self.append_to_termo(OP(self._input.LT(-1).text))
                self.state = 160
                self.termo()
                self.check_op(self._last_termo_type, 'Neg')
                pass
            else:
                raise NoViableAltException(self)

            self.state = 165
            self.termol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_NUM(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.OP_NUM)
            else:
                return self.getToken(IsiLanguageParser.OP_NUM, i)

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.TermoContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.TermoContext,i)


        def OP_LOG_B(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.OP_LOG_B)
            else:
                return self.getToken(IsiLanguageParser.OP_LOG_B, i)

        def OP_ORD(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.OP_ORD)
            else:
                return self.getToken(IsiLanguageParser.OP_ORD, i)

        def OP_REL(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLanguageParser.OP_REL)
            else:
                return self.getToken(IsiLanguageParser.OP_REL, i)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_termol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermol" ):
                listener.enterTermol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermol" ):
                listener.exitTermol(self)




    def termol(self):

        localctx = IsiLanguageParser.TermolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_termol)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self._first_p_type=self._last_termo_type
                        self.state = 168
                        self.match(IsiLanguageParser.OP_NUM)
                        self.append_to_termo(OP(self._input.LT(-1).text))
                        self.state = 170
                        self.termo()
                        self.check_2p_op('Add') 
                    self.state = 177
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self._first_p_type=self._last_termo_type
                        self.state = 179
                        self.match(IsiLanguageParser.OP_LOG_B)
                        self.append_to_termo(OP(self._input.LT(-1).text))
                        self.state = 181
                        self.termo()
                        self.check_2p_op('Log') 
                    self.state = 188
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self._first_p_type=self._last_termo_type
                        self.state = 190
                        self.match(IsiLanguageParser.OP_ORD)
                        self.append_to_termo(OP(self._input.LT(-1).text))
                        self.state = 192
                        self.termo()
                        self.check_2p_op('Ord') 
                    self.state = 199
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self._first_p_type=self._last_termo_type
                        self.state = 201
                        self.match(IsiLanguageParser.OP_REL)
                        self.append_to_termo(OP(self._input.LT(-1).text))
                        self.state = 203
                        self.termo()
                        self.check_2p_op('Comp') 
                    self.state = 210
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





