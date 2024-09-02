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

def serializedATN():
    return [
        4,1,29,185,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,41,8,1,10,
        1,12,1,44,9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,4,3,55,8,3,11,
        3,12,3,56,1,4,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,72,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,9,1,9,1,9,3,9,93,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,3,10,103,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,139,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,148,8,14,10,
        14,12,14,151,9,14,1,14,1,14,1,14,1,14,1,14,5,14,158,8,14,10,14,12,
        14,161,9,14,1,14,1,14,1,14,1,14,1,14,5,14,168,8,14,10,14,12,14,171,
        9,14,1,14,1,14,1,14,1,14,1,14,5,14,178,8,14,10,14,12,14,181,9,14,
        3,14,183,8,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        0,0,190,0,30,1,0,0,0,2,36,1,0,0,0,4,47,1,0,0,0,6,54,1,0,0,0,8,61,
        1,0,0,0,10,63,1,0,0,0,12,76,1,0,0,0,14,81,1,0,0,0,16,86,1,0,0,0,
        18,92,1,0,0,0,20,94,1,0,0,0,22,106,1,0,0,0,24,114,1,0,0,0,26,138,
        1,0,0,0,28,182,1,0,0,0,30,31,5,3,0,0,31,32,3,2,1,0,32,33,3,6,3,0,
        33,34,5,4,0,0,34,35,5,28,0,0,35,1,1,0,0,0,36,37,5,5,0,0,37,42,3,
        4,2,0,38,39,5,1,0,0,39,41,3,4,2,0,40,38,1,0,0,0,41,44,1,0,0,0,42,
        40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,28,
        0,0,46,3,1,0,0,0,47,48,5,21,0,0,48,49,6,2,-1,0,49,5,1,0,0,0,50,51,
        3,8,4,0,51,52,5,28,0,0,52,55,1,0,0,0,53,55,3,18,9,0,54,50,1,0,0,
        0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,7,1,
        0,0,0,58,62,3,10,5,0,59,62,3,12,6,0,60,62,3,14,7,0,61,58,1,0,0,0,
        61,59,1,0,0,0,61,60,1,0,0,0,62,9,1,0,0,0,63,64,5,6,0,0,64,65,6,5,
        -1,0,65,66,5,26,0,0,66,67,3,16,8,0,67,71,6,5,-1,0,68,69,5,2,0,0,
        69,70,5,20,0,0,70,72,6,5,-1,0,71,68,1,0,0,0,71,72,1,0,0,0,72,73,
        1,0,0,0,73,74,6,5,-1,0,74,75,5,27,0,0,75,11,1,0,0,0,76,77,5,7,0,
        0,77,78,5,26,0,0,78,79,3,26,13,0,79,80,5,27,0,0,80,13,1,0,0,0,81,
        82,3,16,8,0,82,83,5,25,0,0,83,84,3,26,13,0,84,85,6,7,-1,0,85,15,
        1,0,0,0,86,87,5,21,0,0,87,88,6,8,-1,0,88,17,1,0,0,0,89,93,3,20,10,
        0,90,93,3,22,11,0,91,93,3,24,12,0,92,89,1,0,0,0,92,90,1,0,0,0,92,
        91,1,0,0,0,93,19,1,0,0,0,94,95,5,8,0,0,95,96,5,26,0,0,96,97,3,26,
        13,0,97,98,5,27,0,0,98,99,5,9,0,0,99,102,3,6,3,0,100,101,5,10,0,
        0,101,103,3,6,3,0,102,100,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,
        0,104,105,5,11,0,0,105,21,1,0,0,0,106,107,5,12,0,0,107,108,5,26,
        0,0,108,109,3,26,13,0,109,110,5,27,0,0,110,111,5,13,0,0,111,112,
        3,6,3,0,112,113,5,14,0,0,113,23,1,0,0,0,114,115,5,13,0,0,115,116,
        3,6,3,0,116,117,5,14,0,0,117,118,5,12,0,0,118,119,5,26,0,0,119,120,
        3,26,13,0,120,121,5,27,0,0,121,25,1,0,0,0,122,123,5,21,0,0,123,139,
        6,13,-1,0,124,125,5,24,0,0,125,139,6,13,-1,0,126,127,5,22,0,0,127,
        139,6,13,-1,0,128,129,5,23,0,0,129,139,6,13,-1,0,130,131,5,26,0,
        0,131,132,3,26,13,0,132,133,5,27,0,0,133,139,1,0,0,0,134,135,5,17,
        0,0,135,136,3,26,13,0,136,137,6,13,-1,0,137,139,1,0,0,0,138,122,
        1,0,0,0,138,124,1,0,0,0,138,126,1,0,0,0,138,128,1,0,0,0,138,130,
        1,0,0,0,138,134,1,0,0,0,139,140,1,0,0,0,140,141,3,28,14,0,141,27,
        1,0,0,0,142,143,6,14,-1,0,143,144,5,19,0,0,144,145,3,26,13,0,145,
        146,6,14,-1,0,146,148,1,0,0,0,147,142,1,0,0,0,148,151,1,0,0,0,149,
        147,1,0,0,0,149,150,1,0,0,0,150,183,1,0,0,0,151,149,1,0,0,0,152,
        153,6,14,-1,0,153,154,5,16,0,0,154,155,3,26,13,0,155,156,6,14,-1,
        0,156,158,1,0,0,0,157,152,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,
        0,159,160,1,0,0,0,160,183,1,0,0,0,161,159,1,0,0,0,162,163,6,14,-1,
        0,163,164,5,15,0,0,164,165,3,26,13,0,165,166,6,14,-1,0,166,168,1,
        0,0,0,167,162,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,
        0,0,0,170,183,1,0,0,0,171,169,1,0,0,0,172,173,6,14,-1,0,173,174,
        5,18,0,0,174,175,3,26,13,0,175,176,6,14,-1,0,176,178,1,0,0,0,177,
        172,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,
        183,1,0,0,0,181,179,1,0,0,0,182,149,1,0,0,0,182,159,1,0,0,0,182,
        169,1,0,0,0,182,179,1,0,0,0,183,29,1,0,0,0,13,42,54,56,61,71,92,
        102,138,149,159,169,179,182
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
    RULE_cmdExpr = 7
    RULE_assignId = 8
    RULE_ctrlFluxo = 9
    RULE_ctrlIF = 10
    RULE_ctrlWhile = 11
    RULE_ctrlDoWhile = 12
    RULE_termo = 13
    RULE_termol = 14

    ruleNames =  [ "prog", "declara", "declaral", "bloco", "cmd", "cmdLeitura", 
                   "cmdEscrita", "cmdExpr", "assignId", "ctrlFluxo", "ctrlIF", 
                   "ctrlWhile", "ctrlDoWhile", "termo", "termol" ]

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
        self._last_assignment = None
        self._last_termo_type = VarTypes.UNDEFINED
        self._input_set_type = VarTypes.UNDEFINED
        self._first_p_type = VarTypes.UNDEFINED

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
            self.state = 30
            self.match(IsiLanguageParser.BEGIN)
            self.state = 31
            self.declara()
            self.state = 32
            self.bloco()
            self.state = 33
            self.match(IsiLanguageParser.END)
            self.state = 34
            self.match(IsiLanguageParser.ENDCMD)
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
            self.state = 36
            self.match(IsiLanguageParser.DECLARE)
            self.state = 37
            self.declaral()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 38
                self.match(IsiLanguageParser.T__0)
                self.state = 39
                self.declaral()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
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
            self.state = 47
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
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 7, 21]:
                    self.state = 50
                    self.cmd()
                    self.state = 51
                    self.match(IsiLanguageParser.ENDCMD)
                    pass
                elif token in [8, 12, 13]:
                    self.state = 53
                    self.ctrlFluxo()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2109888) != 0)):
                    break

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


        def cmdExpr(self):
            return self.getTypedRuleContext(IsiLanguageParser.CmdExprContext,0)


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
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.cmdLeitura()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.cmdEscrita()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.cmdExpr()
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
            self.state = 63
            self.match(IsiLanguageParser.INPUT)
            self._input_set_type=VarTypes.UNDEFINED
            self.state = 65
            self.match(IsiLanguageParser.AP)
            self.state = 66
            self.assignId()
            self.initialize(self._input.LT(-1).text)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 68
                self.match(IsiLanguageParser.T__1)
                self.state = 69
                self.match(IsiLanguageParser.TYPE)
                self._input_set_type=INPUT_TYPES[self._input.LT(-1).text]


            self.input_assignment_type()
            self.state = 74
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

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


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
            self.state = 76
            self.match(IsiLanguageParser.OUTPUT)
            self.state = 77
            self.match(IsiLanguageParser.AP)
            self.state = 78
            self.termo()
            self.state = 79
            self.match(IsiLanguageParser.FP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignId(self):
            return self.getTypedRuleContext(IsiLanguageParser.AssignIdContext,0)


        def ASSIGN(self):
            return self.getToken(IsiLanguageParser.ASSIGN, 0)

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_cmdExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdExpr" ):
                listener.enterCmdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdExpr" ):
                listener.exitCmdExpr(self)




    def cmdExpr(self):

        localctx = IsiLanguageParser.CmdExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmdExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.assignId()
            self.state = 82
            self.match(IsiLanguageParser.ASSIGN)
            self.state = 83
            self.termo()
            self._last_assignment.var_type = self._last_termo_type
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
            self.state = 86
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
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.ctrlIF()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.ctrlWhile()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
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

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


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
            self.state = 94
            self.match(IsiLanguageParser.IF)
            self.state = 95
            self.match(IsiLanguageParser.AP)
            self.state = 96
            self.termo()
            self.state = 97
            self.match(IsiLanguageParser.FP)
            self.state = 98
            self.match(IsiLanguageParser.THEN)
            self.state = 99
            self.bloco()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 100
                self.match(IsiLanguageParser.ELSE)
                self.state = 101
                self.bloco()


            self.state = 104
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

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


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
            self.state = 106
            self.match(IsiLanguageParser.WHILE)
            self.state = 107
            self.match(IsiLanguageParser.AP)
            self.state = 108
            self.termo()
            self.state = 109
            self.match(IsiLanguageParser.FP)
            self.state = 110
            self.match(IsiLanguageParser.DO)
            self.state = 111
            self.bloco()
            self.state = 112
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
            self.state = 114
            self.match(IsiLanguageParser.DO)
            self.state = 115
            self.bloco()
            self.state = 116
            self.match(IsiLanguageParser.ENDDO)
            self.state = 117
            self.match(IsiLanguageParser.WHILE)
            self.state = 118
            self.match(IsiLanguageParser.AP)
            self.state = 119
            self.termo()
            self.state = 120
            self.match(IsiLanguageParser.FP)
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
        self.enterRule(localctx, 26, self.RULE_termo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 122
                self.match(IsiLanguageParser.ID)
                self.acces_var(self._input.LT(-1).text)
                pass
            elif token in [24]:
                self.state = 124
                self.match(IsiLanguageParser.NUM)
                self._last_termo_type=VarTypes.NUM
                pass
            elif token in [22]:
                self.state = 126
                self.match(IsiLanguageParser.TEXTO)
                self._last_termo_type=VarTypes.TEXT
                pass
            elif token in [23]:
                self.state = 128
                self.match(IsiLanguageParser.BOOL)
                self._last_termo_type=VarTypes.BOOL
                pass
            elif token in [26]:
                self.state = 130
                self.match(IsiLanguageParser.AP)
                self.state = 131
                self.termo()
                self.state = 132
                self.match(IsiLanguageParser.FP)
                pass
            elif token in [17]:
                self.state = 134
                self.match(IsiLanguageParser.OP_LOG_U)
                self.state = 135
                self.termo()
                self.check_op(self._last_termo_type, 'Neg')
                pass
            else:
                raise NoViableAltException(self)

            self.state = 140
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
        self.enterRule(localctx, 28, self.RULE_termol)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self._first_p_type=self._last_termo_type
                        self.state = 143
                        self.match(IsiLanguageParser.OP_NUM)
                        self.state = 144
                        self.termo()
                        self.check_2p_op('Add') 
                    self.state = 151
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self._first_p_type=self._last_termo_type
                        self.state = 153
                        self.match(IsiLanguageParser.OP_LOG_B)
                        self.state = 154
                        self.termo()
                        self.check_2p_op('Log') 
                    self.state = 161
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self._first_p_type=self._last_termo_type
                        self.state = 163
                        self.match(IsiLanguageParser.OP_ORD)
                        self.state = 164
                        self.termo()
                        self.check_2p_op('Ord') 
                    self.state = 171
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self._first_p_type=self._last_termo_type
                        self.state = 173
                        self.match(IsiLanguageParser.OP_REL)
                        self.state = 174
                        self.termo()
                        self.check_2p_op('Comp') 
                    self.state = 181
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





