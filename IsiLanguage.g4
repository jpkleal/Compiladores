grammar IsiLanguage;

options{
    language=Python3;
}

@header{
from vartypes import *
from exceptions import SemanticException
}

@members{
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

def ensure_expr_type(type):
    if self._crt_exp_type != type:
        raise SemanticException(f"Variable created and not used: {key}")
}

prog        : 'programa' declara bloco 'fimprog' FIM_CMD
            ;
declara     : 'declare' declaral (',' declaral)* FIM_CMD
            ;
declaral    : ID {self._symbol_table[self._input.LT(-1).text]=Var(name=self._input.LT(-1).text, var_type=VarTypes.UNDEFINED)}
            ;
bloco       : ((cmd FIM_CMD) | ctrlFluxo)+
            ;
cmd         : cmdLeitura | cmdEscrita | cmdExpr
            ;
cmdLeitura  : 'leia' AP declId {self.initialize(self._input.LT(-1).text)} FP
            ;
cmdEscrita  : 'escreva' AP termo FP
            ;
cmdExpr     : declId {self._atr_var=self.initialize(self._input.LT(-1).text)}
              ':=' {self._crt_exp_type = VarTypes.UNDEFINED} expr {self._atr_var.var_type=self._crt_exp_type}
            ;
ctrlFluxo   : ctrlIF | ctrlWhile | ctrlDoWhile
            ;
ctrlIF      : 'se' AP {self._crt_exp_type = VarTypes.UNDEFINED} expr {self._crt_exp_type = VarTypes.UNDEFINED} OP_REL {self._crt_exp_type = VarTypes.UNDEFINED} expr FP
              'entao' '{' bloco '}'
              ('senao' '{' bloco '}' )?
            ;
ctrlWhile   : 'enquanto' AP expr OP_REL expr FP 'faca' '{' bloco '}'
            ;
ctrlDoWhile : 'faca' '{' bloco '}' 'enquanto' AP expr OP_REL expr FP
            ;
expr        : termo {self._update_termo(self._lt)} exprl | '(' expr ')'
            ;
exprl       : (OP_NUM termo {self._update_termo(self._lt)})*
            ;
termo       : declId {self._lt=self.checkInitializedVar(self._input.LT(-1).text).var_type}
            | NUM {self._lt=VarTypes.NUM}
            | TEXTO {self._lt=VarTypes.TEXT}
			;
declId      : ID {self.checkExistingVar(self._input.LT(-1).text)}
            ;


OP_REL_INT  : '<' | '>' | '<=' | '>='
            ;
OP_LOG      : 'e' | 'ou' | 'não'
            ;
OP_REL      : '!=' | '==' | OP_REL_INT
            ;
OP_NUM      : '+' | '-' | '*' | '/'
			;
ID          : ([a-z] | [A-Z]) ([a-z] | [A-Z] | [0-9])*
            ;
TEXTO       : '"' ( [a-z] | [A-Z] | [0-9] | ',' | '.' | ' ' | '-' )* '"'
            ;
NUM         : ([0-9])+ ('.' [0-9]+ )?
            ;
AP          : '('
            ;
FP          : ')'
            ;
FIM_CMD     : '.'
            ;
WS          : (' ' | '\n' | '\r' | '\t' ) -> skip
			;