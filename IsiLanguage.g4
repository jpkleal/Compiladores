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
}

//prog        : 'programa' declara bloco END ENDCMD
prog        : BEGIN declara bloco END ENDCMD
            ;
declara     : DECLARE declaral (',' declaral)* ENDCMD
            ;
declaral    : ID {self.declare_var(self._input.LT(-1).text)}
            ;
bloco       : ((cmd ENDCMD) | ctrlFluxo)+
            ;

// Command List
cmd         : cmdLeitura | cmdEscrita | cmdExpr
            ;
cmdLeitura  : INPUT {self._input_set_type=VarTypes.UNDEFINED}
              AP assignId {self.initialize(self._input.LT(-1).text)}
              (':' TYPE {self._input_set_type=INPUT_TYPES[self._input.LT(-1).text]})?
              {self.input_assignment_type()} FP
            ;
cmdEscrita  : OUTPUT AP termo FP
            ;
cmdExpr     : assignId ASSIGN termo {self._last_assignment.var_type = self._last_termo_type}
            ;
assignId    : ID {self.assign_var(self._input.LT(-1).text)}
            ;

// Flow Control
ctrlFluxo   : ctrlIF | ctrlWhile | ctrlDoWhile
            ;
ctrlIF      : IF AP termo FP
              THEN bloco
              (ELSE bloco )?
              ENDIF
            ;
ctrlWhile   : WHILE AP termo FP DO bloco ENDDO
            ;
ctrlDoWhile : DO bloco ENDDO WHILE AP termo FP
            ;

// Values, Expr (Binary and Unary), Varibles
termo       : (ID {self.acces_var(self._input.LT(-1).text)}
            | NUM {self._last_termo_type=VarTypes.NUM}
            | TEXTO {self._last_termo_type=VarTypes.TEXT}
            | BOOL {self._last_termo_type=VarTypes.BOOL}
            | AP termo FP
            | OP_LOG_U termo {self.check_op(self._last_termo_type, 'Neg')})
            termol
			;
termol      : ({self._first_p_type=self._last_termo_type} OP_NUM termo {self.check_2p_op('Add')})*
            | ({self._first_p_type=self._last_termo_type} OP_LOG_B termo {self.check_2p_op('Log')})*
            | ({self._first_p_type=self._last_termo_type} OP_ORD termo {self.check_2p_op('Ord')})*
            | ({self._first_p_type=self._last_termo_type} OP_REL termo {self.check_2p_op('Comp')})*
            ;

// Terminal values

// Reserved Words
BEGIN       : 'programa'
            ;
END         : 'fimprog'
            ;
DECLARE     : 'declare'
            ;
INPUT       : 'leia'
            ;
OUTPUT      : 'escreva'
            ;
IF          : 'se'
            ;
THEN        : 'entao'
            ;
ELSE        : 'senao'
            ;
ENDIF       : 'fimse'
            ;
WHILE       : 'enquanto'
            ;
DO          : 'faca'
            ;
ENDDO       : 'fimfaca'
            ;

// Operadores
OP_ORD      : '<' | '>' | '<=' | '>='
            ;
OP_LOG_B    : 'OU' | 'E'
            ;
OP_LOG_U    : 'NAO'
            ;
OP_REL      : '!=' | '=='
            ;
OP_NUM      : '+' | '-' | '*' | '/'
			;

// Values
TYPE        : 'NUM' | 'TEXTO'
            ;
ID          : ([a-z] | [A-Z]) ([a-z] | [A-Z] | [0-9])*
            ;
TEXTO       : '"' ( [a-z] | [A-Z] | [0-9] | ',' | '.' | ' ' | '-' )* '"'
            ;
BOOL        :'Verdadeiro' | 'Falso'
            ;
NUM         : ([0-9])+ ('.' [0-9]+ )?
            ;

// Others
ASSIGN      : ':='
            ;
AP          : '('
            ;
FP          : ')'
            ;
ENDCMD      : '.'
            ;
WS          : (' ' | '\n' | '\r' | '\t' ) -> skip
			;