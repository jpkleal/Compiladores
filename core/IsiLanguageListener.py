# Generated from IsiLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IsiLanguageParser import IsiLanguageParser
else:
    from IsiLanguageParser import IsiLanguageParser

from vartypes import *
from exceptions import SemanticException


# This class defines a complete listener for a parse tree produced by IsiLanguageParser.
class IsiLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by IsiLanguageParser#prog.
    def enterProg(self, ctx:IsiLanguageParser.ProgContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#prog.
    def exitProg(self, ctx:IsiLanguageParser.ProgContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#declara.
    def enterDeclara(self, ctx:IsiLanguageParser.DeclaraContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#declara.
    def exitDeclara(self, ctx:IsiLanguageParser.DeclaraContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#declaral.
    def enterDeclaral(self, ctx:IsiLanguageParser.DeclaralContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#declaral.
    def exitDeclaral(self, ctx:IsiLanguageParser.DeclaralContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#bloco.
    def enterBloco(self, ctx:IsiLanguageParser.BlocoContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#bloco.
    def exitBloco(self, ctx:IsiLanguageParser.BlocoContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmd.
    def enterCmd(self, ctx:IsiLanguageParser.CmdContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmd.
    def exitCmd(self, ctx:IsiLanguageParser.CmdContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdLeitura.
    def enterCmdLeitura(self, ctx:IsiLanguageParser.CmdLeituraContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdLeitura.
    def exitCmdLeitura(self, ctx:IsiLanguageParser.CmdLeituraContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdEscrita.
    def enterCmdEscrita(self, ctx:IsiLanguageParser.CmdEscritaContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdEscrita.
    def exitCmdEscrita(self, ctx:IsiLanguageParser.CmdEscritaContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#cmdExpr.
    def enterCmdExpr(self, ctx:IsiLanguageParser.CmdExprContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#cmdExpr.
    def exitCmdExpr(self, ctx:IsiLanguageParser.CmdExprContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#assignId.
    def enterAssignId(self, ctx:IsiLanguageParser.AssignIdContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#assignId.
    def exitAssignId(self, ctx:IsiLanguageParser.AssignIdContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#ctrlFluxo.
    def enterCtrlFluxo(self, ctx:IsiLanguageParser.CtrlFluxoContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#ctrlFluxo.
    def exitCtrlFluxo(self, ctx:IsiLanguageParser.CtrlFluxoContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#ctrlIF.
    def enterCtrlIF(self, ctx:IsiLanguageParser.CtrlIFContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#ctrlIF.
    def exitCtrlIF(self, ctx:IsiLanguageParser.CtrlIFContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#ctrlWhile.
    def enterCtrlWhile(self, ctx:IsiLanguageParser.CtrlWhileContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#ctrlWhile.
    def exitCtrlWhile(self, ctx:IsiLanguageParser.CtrlWhileContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#ctrlDoWhile.
    def enterCtrlDoWhile(self, ctx:IsiLanguageParser.CtrlDoWhileContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#ctrlDoWhile.
    def exitCtrlDoWhile(self, ctx:IsiLanguageParser.CtrlDoWhileContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#termo.
    def enterTermo(self, ctx:IsiLanguageParser.TermoContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#termo.
    def exitTermo(self, ctx:IsiLanguageParser.TermoContext):
        pass


    # Enter a parse tree produced by IsiLanguageParser#termol.
    def enterTermol(self, ctx:IsiLanguageParser.TermolContext):
        pass

    # Exit a parse tree produced by IsiLanguageParser#termol.
    def exitTermol(self, ctx:IsiLanguageParser.TermolContext):
        pass



del IsiLanguageParser