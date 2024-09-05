grammar IsiLanguage;

options{
    language=Python3;
}

@header{
from vartypes import *
from exceptions import SemanticException
from base_structures import *
from commands import STR_TO_COMMAND
}

@members{
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

def begin_bloc(self, bloco):
    self._bloc_stack.append(bloco)

def end_bloc(self):
    self._bloc_stack.pop(-1)

def new_command(self, cmd):
    self.bloc.append(STR_TO_COMMAND[cmd]())

def last_command(self):
    return self.bloc.command

@property
def bloc(self):
    return self._bloc_stack[-1]

def begin_termo(self):
    self._last_termo = Termo()

def append_to_termo(self, text):
    self._last_termo.append(text)
}

//prog        : 'programa' declara bloco END ENDCMD
prog        : BEGIN declara {self.begin_bloc(self.program.command)} bloco END ENDCMD {self.program.symbol_table=self._symbol_table.values()}
            ;
declara     : DECLARE declaral (',' declaral)* ENDCMD
            ;
declaral    : ID {self.declare_var(self._input.LT(-1).text)}
            ;
bloco       : ((cmd ENDCMD) | ctrlFluxo)+ {self.end_bloc()}
            ;

// Command List
cmd         : cmdLeitura | cmdEscrita | cmdAssign
            ;
cmdLeitura  : INPUT {self.new_command("read")} {self._input_set_type=VarTypes.UNDEFINED}
              AP assignId {self.initialize(self._input.LT(-1).text)} {self.last_command().assign_id=self._last_assignment}
              (':' TYPE {self._input_set_type=INPUT_TYPES[self._input.LT(-1).text]})?
              {self.input_assignment_type()} FP
            ;
cmdEscrita  : OUTPUT {self.new_command("write")} AP new_termo {self.last_command().termo=self._last_termo} FP
            ;
cmdAssign   : assignId ASSIGN {self.new_command("assign")} {self.last_command().assign_id=self._last_assignment} new_termo {self._last_assignment.var_type = self._last_termo_type} {self.last_command().termo=self._last_termo}
            ;
assignId    : ID {self.assign_var(self._input.LT(-1).text)}
            ;

// Flow Control
ctrlFluxo   : ctrlIF | ctrlWhile | ctrlDoWhile
            ;
ctrlIF      : IF {self.new_command("if")} AP new_termo {self.last_command().termo=self._last_termo} FP
              THEN {self.begin_bloc(self.last_command().bloc_1)} bloco
              (ELSE {self.begin_bloc(self.last_command().bloc_2)} bloco)?
              ENDIF
            ;
ctrlWhile   : WHILE {self.new_command("while")} AP new_termo {self.last_command().termo=self._last_termo} FP DO {self.begin_bloc(self.last_command().bloc)} bloco ENDDO
            ;
ctrlDoWhile : DO {self.new_command("dowhile")} {self.begin_bloc(self.last_command().bloc)} bloco ENDDO WHILE AP new_termo {self.last_command().termo=self._last_termo} FP
            ;

// Values, Expr (Binary and Unary), Varibles
new_termo   : {self.begin_termo()} termo {self._last_termo.var_type=self._last_termo_type}
            ;
termo       : (ID {self.acces_var(self._input.LT(-1).text)} {self.append_to_termo(self._input.LT(-1).text)}
            | NUM {self._last_termo_type=VarTypes.NUM} {self.append_to_termo(self._input.LT(-1).text)}
            | TEXTO {self._last_termo_type=VarTypes.TEXT} {self.append_to_termo(self._input.LT(-1).text)}
            | BOOL {self._last_termo_type=VarTypes.BOOL} {self.append_to_termo(BOOL(self._input.LT(-1).text))}
            | AP {self.append_to_termo(OP('ap'))} termo FP {self.append_to_termo(OP('fp'))}
            | OP_LOG_U {self.append_to_termo(OP(self._input.LT(-1).text))} termo {self.check_op(self._last_termo_type, 'Neg')})
            termol
			;
termol      : ({self._first_p_type=self._last_termo_type} OP_NUM {self.append_to_termo(OP(self._input.LT(-1).text))} termo {self.check_2p_op('Add')})*
            | ({self._first_p_type=self._last_termo_type} OP_LOG_B {self.append_to_termo(OP(self._input.LT(-1).text))} termo {self.check_2p_op('Log')})*
            | ({self._first_p_type=self._last_termo_type} OP_ORD {self.append_to_termo(OP(self._input.LT(-1).text))} termo {self.check_2p_op('Ord')})*
            | ({self._first_p_type=self._last_termo_type} OP_REL {self.append_to_termo(OP(self._input.LT(-1).text))} termo {self.check_2p_op('Comp')})*
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
BOOL        :'Verdadeiro' | 'Falso'
            ;
ID          : ([a-z] | [A-Z]) ([a-z] | [A-Z] | [0-9])*
            ;
TEXTO       : '"' ( [a-z] | [A-Z] | [0-9] | ',' | '.' | ' ' | '-' )* '"'
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