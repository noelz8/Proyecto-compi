import ply.yacc as yacc
from lex_parser import tokens

# Regla inicial
def p_program(p):
    '''
    program : lista_comentarios code_block
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el programa completo

def p_lista_comentarios(p):
    '''
    lista_comentarios : comentario lista_comentarios
                 | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar los comentarios

def p_comentario(p):
    '''
    comentario : COMENTARIO
    '''
    # Aquí puedes realizar las acciones necesarias para procesar un comentario

def p_code_block(p):
    '''
    code_block : proc MASTER LPARENTESIS comentario list_statement RPARENTESIS PUNTO_COMA group_proc
            | group_proc proc MASTER LPARENTESIS comentario list_statement RPARENTESIS PUNTO_COMA group_proc
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el bloque de código

def p_proc(p):
    '''
    proc : PROC
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el proc

"""def p_master(p):
    '''
    master : MASTER
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el master
"""
def p_group_proc(p):
    '''
    group_proc : PROC VARIABLE LPARENTESIS COMENTARIO statement RPARENTESIS PUNTO_COMA group_proc
               | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el bloque de códig

def p_operador(p):
    '''
    operador : ADD
            | SUB
            | MUL
            | DIV
    '''
def p_list_statement(p):
    '''
    list_statement : statement list_statement
                  | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una lista de sentencias
def p_statement(p):
    '''
    statement : new_variable_statement
              | values_statement
              | alter_statement
              | alterb_statement
              | condition_statement
              | istrue_statement
              | repeat_statement
              | until_statement
              | while_statement
              | case_statement
              | printvalues_statement
              | signal_statement
              | viewsignal_statement
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia

def p_new_variable_statement(p):
    '''
    new_variable_statement : NEW VARIABLE COMA LPARENTESIS DATATYPE COMA value RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia New

def p_values_statement(p):
    '''
    values_statement : VALUES LPARENTESIS VARIABLE COMA value RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Values

def p_alter_statement(p):
    '''
    alter_statement : ALTER LPARENTESIS VARIABLE COMA operador COMA value RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Alter

def p_alterb_statement(p):
    '''
    alterb_statement : ALTERB LPARENTESIS VARIABLE RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia AlterB

def p_condition_statement(p):
    '''
    condition_statement : expression COND_NUMERICA expression
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia condicional

def p_istrue_statement(p):
    '''
    istrue_statement : ISTRUE LPARENTESIS VARIABLE RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia IsTrue

def p_repeat_statement(p):
    '''
    repeat_statement : REPEAT LPARENTESIS list_statement break_statement RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Repeat

def p_break_statement(p):
    '''
    break_statement : BREAK PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Break

def p_until_statement(p):
    '''
    until_statement : UNTIL list_statement condition PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Until
def p_condition(p):
    '''
    condition : expression COND_NUMERICA expression
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una condición
def p_while_statement(p):
    '''
    while_statement : WHILE expression LPARENTESIS list_statement RPARENTESIS PUNTO_COMA
                    | WHILE istrue LPARENTESIS list_statement RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia While
def p_bool(p):
    '''
    bool : TRUE
         | FALSE
    '''
    # Aquí puedes realizar las acciones necesarias para procesar un valor booleano
def p_case_statement(p):
    '''
    case_statement : CASE VARIABLE case_when_statements else_statement PUNTO_COMA
    '''

    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Case
def p_case_when_statements(p):
    '''
    case_when_statements : case_when_statement case_when_statements
                         | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar los casos When en una sentencia Case
def p_case_when_statement(p):
    '''
    case_when_statement : WHEN value THEN list_statement
    '''
    # Aquí puedes realizar las acciones necesarias para procesar un caso When en una sentencia Case

def p_else_statement(p):
    '''
    else_statement : ELSE code_block
                   | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar la cláusula Else en una sentencia Case

def p_printvalues_statement(p):
    '''
    printvalues_statement : PRINTVALUES LPARENTESIS VARIABLE RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia PrintValues

def p_signal_statement(p):
    '''
    signal_statement : SIGNAL LPARENTESIS VARIABLE COMA value RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Signal

def p_viewsignal_statement(p):
    '''
    viewsignal_statement : VIEWSIGNAL LPARENTESIS VARIABLE RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia ViewSignal

def p_expression(p):
    '''
    expression : value
               | VARIABLE
               | LPARENTESIS expression RPARENTESIS
               | expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una expresión matemática

def p_istrue(p):
    '''
    istrue : ISTRUE LPARENTESIS VARIABLE RPARENTESIS
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una expresión booleana

def p_value(p):
    '''
    value : NUMERO
          | bool
    '''
    # Aquí puedes realizar las acciones necesarias para procesar un valor

def p_empty(p):
    '''
    empty :
    '''
    pass

# Manejo de errores de sintaxis
def p_error(p):
    print("Error de sintaxis en la entrada:", p)

def p_values(p):
    '''
    values : VALUES
    '''
# Construcción del parser
parser = yacc.yacc()



# Prueba del parser
data = '''
//Nombre y funcionalidad del código
Proc @Master
(
    // Comentario de prueba
    Values (@variable2, True);
    While IsTrue(@variable2)
        ( Signal(@variable2, 1);
        AlterB (@variable2);
);
Proc @Procesofoo (
    // Comentario de prueba
    Values (@variable1, 100);
    While @variable1 > 10
        ( Signal(@variale1, 1);
        Values (@variable1, Alter (@variable1,SUB, 10));
 );
);'''

parser.parse(data)
