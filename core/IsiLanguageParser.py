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
        4,1,23,158,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,42,8,
        1,10,1,12,1,45,9,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,4,3,56,8,
        3,11,3,12,3,57,1,4,1,4,1,4,3,4,63,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,86,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        3,9,103,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,135,8,12,1,13,1,13,1,13,1,
        13,5,13,141,8,13,10,13,12,13,144,9,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,3,14,153,8,14,1,15,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,0,0,153,0,32,1,0,0,0,2,37,1,0,0,0,4,48,
        1,0,0,0,6,55,1,0,0,0,8,62,1,0,0,0,10,64,1,0,0,0,12,70,1,0,0,0,14,
        75,1,0,0,0,16,85,1,0,0,0,18,87,1,0,0,0,20,104,1,0,0,0,22,115,1,0,
        0,0,24,134,1,0,0,0,26,142,1,0,0,0,28,152,1,0,0,0,30,154,1,0,0,0,
        32,33,5,1,0,0,33,34,3,2,1,0,34,35,3,6,3,0,35,36,5,2,0,0,36,1,1,0,
        0,0,37,38,5,3,0,0,38,43,3,4,2,0,39,40,5,4,0,0,40,42,3,4,2,0,41,39,
        1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,
        45,43,1,0,0,0,46,47,5,5,0,0,47,3,1,0,0,0,48,49,5,20,0,0,49,50,6,
        2,-1,0,50,5,1,0,0,0,51,52,3,8,4,0,52,53,5,5,0,0,53,56,1,0,0,0,54,
        56,3,16,8,0,55,51,1,0,0,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,
        0,0,57,58,1,0,0,0,58,7,1,0,0,0,59,63,3,10,5,0,60,63,3,12,6,0,61,
        63,3,14,7,0,62,59,1,0,0,0,62,60,1,0,0,0,62,61,1,0,0,0,63,9,1,0,0,
        0,64,65,5,6,0,0,65,66,5,7,0,0,66,67,3,30,15,0,67,68,6,5,-1,0,68,
        69,5,8,0,0,69,11,1,0,0,0,70,71,5,9,0,0,71,72,5,7,0,0,72,73,3,28,
        14,0,73,74,5,8,0,0,74,13,1,0,0,0,75,76,3,30,15,0,76,77,6,7,-1,0,
        77,78,5,10,0,0,78,79,6,7,-1,0,79,80,3,24,12,0,80,81,6,7,-1,0,81,
        15,1,0,0,0,82,86,3,18,9,0,83,86,3,20,10,0,84,86,3,22,11,0,85,82,
        1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,17,1,0,0,0,87,88,5,11,0,0,
        88,89,5,7,0,0,89,90,3,24,12,0,90,91,5,18,0,0,91,92,3,24,12,0,92,
        93,5,8,0,0,93,94,5,12,0,0,94,95,5,13,0,0,95,96,3,6,3,0,96,102,5,
        14,0,0,97,98,5,15,0,0,98,99,5,13,0,0,99,100,3,6,3,0,100,101,5,14,
        0,0,101,103,1,0,0,0,102,97,1,0,0,0,102,103,1,0,0,0,103,19,1,0,0,
        0,104,105,5,16,0,0,105,106,5,7,0,0,106,107,3,24,12,0,107,108,5,18,
        0,0,108,109,3,24,12,0,109,110,5,8,0,0,110,111,5,17,0,0,111,112,5,
        13,0,0,112,113,3,6,3,0,113,114,5,14,0,0,114,21,1,0,0,0,115,116,5,
        17,0,0,116,117,5,13,0,0,117,118,3,6,3,0,118,119,5,14,0,0,119,120,
        5,16,0,0,120,121,5,7,0,0,121,122,3,24,12,0,122,123,5,18,0,0,123,
        124,3,24,12,0,124,125,5,8,0,0,125,23,1,0,0,0,126,127,3,28,14,0,127,
        128,6,12,-1,0,128,129,3,26,13,0,129,135,1,0,0,0,130,131,5,7,0,0,
        131,132,3,24,12,0,132,133,5,8,0,0,133,135,1,0,0,0,134,126,1,0,0,
        0,134,130,1,0,0,0,135,25,1,0,0,0,136,137,5,19,0,0,137,138,3,28,14,
        0,138,139,6,13,-1,0,139,141,1,0,0,0,140,136,1,0,0,0,141,144,1,0,
        0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,27,1,0,0,0,144,142,1,0,0,
        0,145,146,3,30,15,0,146,147,6,14,-1,0,147,153,1,0,0,0,148,149,5,
        22,0,0,149,153,6,14,-1,0,150,151,5,21,0,0,151,153,6,14,-1,0,152,
        145,1,0,0,0,152,148,1,0,0,0,152,150,1,0,0,0,153,29,1,0,0,0,154,155,
        5,20,0,0,155,156,6,15,-1,0,156,31,1,0,0,0,9,43,55,57,62,85,102,134,
        142,152
    ]

class IsiLanguageParser ( Parser ):

    grammarFileName = "IsiLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'fimprog.'", "'declare'", 
                     "','", "'.'", "'leia'", "'('", "')'", "'escreva'", 
                     "':='", "'se'", "'entao'", "'{'", "'}'", "'senao'", 
                     "'enquanto'", "'faca'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OP_REL", "OP_NUM", "ID", 
                      "TEXTO", "NUM", "WS" ]

    RULE_prog = 0
    RULE_declara = 1
    RULE_declaral = 2
    RULE_bloco = 3
    RULE_cmd = 4
    RULE_cmdLeitura = 5
    RULE_cmdEscrita = 6
    RULE_cmdExpr = 7
    RULE_ctrlFluxo = 8
    RULE_ctrlIF = 9
    RULE_ctrlWhile = 10
    RULE_ctrlDoWhile = 11
    RULE_expr = 12
    RULE_exprl = 13
    RULE_termo = 14
    RULE_declId = 15

    ruleNames =  [ "prog", "declara", "declaral", "bloco", "cmd", "cmdLeitura", 
                   "cmdEscrita", "cmdExpr", "ctrlFluxo", "ctrlIF", "ctrlWhile", 
                   "ctrlDoWhile", "expr", "exprl", "termo", "declId" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    OP_REL=18
    OP_NUM=19
    ID=20
    TEXTO=21
    NUM=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self._symbol_table = {}
        self._atr_var = None
        self._lt_type = VarTypes.UNDEFINED
        self._crt_exp_type = VarTypes.UNDEFINED

    def showIds(self):
        for key, vals in self._symbol_table.items():
            print(key, vals)

    def checkExistingVar(self, var):
        if var not in self._symbol_table:
            raise SemanticException(f"Undeclared Variable: {var}")
        return self._symbol_table[var]

    def checkInitializedVar(self, var):
        if var not in self._symbol_table or not self._symbol_table[var].initialized:
            raise SemanticException(f"Uninitialized Variable: {var}")
        return self._symbol_table[var]

    def initialize(self, var):
        self._symbol_table[var].initialized = True
        return self._symbol_table[var]

    def _update_termo(self, new_type):
        print(self._crt_exp_type, new_type)
        if self._crt_exp_type == VarTypes.UNDEFINED:
            self._crt_exp_type = new_type
        elif self._crt_exp_type != new_type:
            raise SemanticException(f"Expressions types don't match")

    def verify_unused_variables(self):
        for key, vals in self._symbol_table.items():
            if not vals.initialized:
                raise SemanticException(f"Variable created and not used: {key}")




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declara(self):
            return self.getTypedRuleContext(IsiLanguageParser.DeclaraContext,0)


        def bloco(self):
            return self.getTypedRuleContext(IsiLanguageParser.BlocoContext,0)


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
            self.match(IsiLanguageParser.T__0)
            self.state = 33
            self.declara()
            self.state = 34
            self.bloco()
            self.state = 35
            self.match(IsiLanguageParser.T__1)
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

        def declaral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.DeclaralContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.DeclaralContext,i)


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
            self.state = 37
            self.match(IsiLanguageParser.T__2)
            self.state = 38
            self.declaral()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 39
                self.match(IsiLanguageParser.T__3)
                self.state = 40
                self.declaral()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(IsiLanguageParser.T__4)
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
            self.state = 48
            self.match(IsiLanguageParser.ID)
            self._symbol_table[self._input.LT(-1).text]=Var(name=self._input.LT(-1).text, var_type=VarTypes.UNDEFINED)
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
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 9, 20]:
                    self.state = 51
                    self.cmd()
                    self.state = 52
                    self.match(IsiLanguageParser.T__4)
                    pass
                elif token in [11, 16, 17]:
                    self.state = 54
                    self.ctrlFluxo()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1247808) != 0)):
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
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.cmdLeitura()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.cmdEscrita()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
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

        def declId(self):
            return self.getTypedRuleContext(IsiLanguageParser.DeclIdContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(IsiLanguageParser.T__5)
            self.state = 65
            self.match(IsiLanguageParser.T__6)
            self.state = 66
            self.declId()
            self.initialize(self._input.LT(-1).text)
            self.state = 68
            self.match(IsiLanguageParser.T__7)
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

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


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
            self.state = 70
            self.match(IsiLanguageParser.T__8)
            self.state = 71
            self.match(IsiLanguageParser.T__6)
            self.state = 72
            self.termo()
            self.state = 73
            self.match(IsiLanguageParser.T__7)
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

        def declId(self):
            return self.getTypedRuleContext(IsiLanguageParser.DeclIdContext,0)


        def expr(self):
            return self.getTypedRuleContext(IsiLanguageParser.ExprContext,0)


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
            self.state = 75
            self.declId()
            self._atr_var=self.initialize(self._input.LT(-1).text)
            self.state = 77
            self.match(IsiLanguageParser.T__9)
            self._crt_exp_type = VarTypes.UNDEFINED
            self.state = 79
            self.expr()
            self._atr_var.var_type=self._crt_exp_type
            print(self._atr_var)
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
        self.enterRule(localctx, 16, self.RULE_ctrlFluxo)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.ctrlIF()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.ctrlWhile()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.ExprContext,i)


        def OP_REL(self):
            return self.getToken(IsiLanguageParser.OP_REL, 0)

        def bloco(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.BlocoContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.BlocoContext,i)


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
        self.enterRule(localctx, 18, self.RULE_ctrlIF)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(IsiLanguageParser.T__10)
            self.state = 88
            self.match(IsiLanguageParser.T__6)
            self.state = 89
            self.expr()
            self.state = 90
            self.match(IsiLanguageParser.OP_REL)
            self.state = 91
            self.expr()
            self.state = 92
            self.match(IsiLanguageParser.T__7)
            self.state = 93
            self.match(IsiLanguageParser.T__11)
            self.state = 94
            self.match(IsiLanguageParser.T__12)
            self.state = 95
            self.bloco()
            self.state = 96
            self.match(IsiLanguageParser.T__13)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 97
                self.match(IsiLanguageParser.T__14)
                self.state = 98
                self.match(IsiLanguageParser.T__12)
                self.state = 99
                self.bloco()
                self.state = 100
                self.match(IsiLanguageParser.T__13)


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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.ExprContext,i)


        def OP_REL(self):
            return self.getToken(IsiLanguageParser.OP_REL, 0)

        def bloco(self):
            return self.getTypedRuleContext(IsiLanguageParser.BlocoContext,0)


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
        self.enterRule(localctx, 20, self.RULE_ctrlWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(IsiLanguageParser.T__15)
            self.state = 105
            self.match(IsiLanguageParser.T__6)
            self.state = 106
            self.expr()
            self.state = 107
            self.match(IsiLanguageParser.OP_REL)
            self.state = 108
            self.expr()
            self.state = 109
            self.match(IsiLanguageParser.T__7)
            self.state = 110
            self.match(IsiLanguageParser.T__16)
            self.state = 111
            self.match(IsiLanguageParser.T__12)
            self.state = 112
            self.bloco()
            self.state = 113
            self.match(IsiLanguageParser.T__13)
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

        def bloco(self):
            return self.getTypedRuleContext(IsiLanguageParser.BlocoContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(IsiLanguageParser.ExprContext,i)


        def OP_REL(self):
            return self.getToken(IsiLanguageParser.OP_REL, 0)

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
        self.enterRule(localctx, 22, self.RULE_ctrlDoWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(IsiLanguageParser.T__16)
            self.state = 116
            self.match(IsiLanguageParser.T__12)
            self.state = 117
            self.bloco()
            self.state = 118
            self.match(IsiLanguageParser.T__13)
            self.state = 119
            self.match(IsiLanguageParser.T__15)
            self.state = 120
            self.match(IsiLanguageParser.T__6)
            self.state = 121
            self.expr()
            self.state = 122
            self.match(IsiLanguageParser.OP_REL)
            self.state = 123
            self.expr()
            self.state = 124
            self.match(IsiLanguageParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self):
            return self.getTypedRuleContext(IsiLanguageParser.TermoContext,0)


        def exprl(self):
            return self.getTypedRuleContext(IsiLanguageParser.ExprlContext,0)


        def expr(self):
            return self.getTypedRuleContext(IsiLanguageParser.ExprContext,0)


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = IsiLanguageParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.termo()
                self._update_termo(self._lt)
                self.state = 128
                self.exprl()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(IsiLanguageParser.T__6)
                self.state = 131
                self.expr()
                self.state = 132
                self.match(IsiLanguageParser.T__7)
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


    class ExprlContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return IsiLanguageParser.RULE_exprl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprl" ):
                listener.enterExprl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprl" ):
                listener.exitExprl(self)




    def exprl(self):

        localctx = IsiLanguageParser.ExprlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 136
                self.match(IsiLanguageParser.OP_NUM)
                self.state = 137
                self.termo()
                self._update_termo(self._lt)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def declId(self):
            return self.getTypedRuleContext(IsiLanguageParser.DeclIdContext,0)


        def NUM(self):
            return self.getToken(IsiLanguageParser.NUM, 0)

        def TEXTO(self):
            return self.getToken(IsiLanguageParser.TEXTO, 0)

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
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.declId()
                self._lt=self.checkInitializedVar(self._input.LT(-1).text).var_type
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(IsiLanguageParser.NUM)
                self._lt=VarTypes.NUM
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(IsiLanguageParser.TEXTO)
                self._lt=VarTypes.TEXT
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


    class DeclIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLanguageParser.ID, 0)

        def getRuleIndex(self):
            return IsiLanguageParser.RULE_declId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclId" ):
                listener.enterDeclId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclId" ):
                listener.exitDeclId(self)




    def declId(self):

        localctx = IsiLanguageParser.DeclIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_declId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(IsiLanguageParser.ID)
            self.checkExistingVar(self._input.LT(-1).text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





