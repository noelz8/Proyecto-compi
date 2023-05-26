import ply.yacc as yacc
from lexer import tokens

# Regla inicial
def p_program(p):
    '''
    program : comment_list code_block
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el programa completo

def p_comment_list(p):
    '''
    comment_list : comment comment_list
                 | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar los comentarios

def p_comment(p):
    '''
    comment : COMMENT
    '''
    # Aquí puedes realizar las acciones necesarias para procesar un comentario

def p_code_block(p):
    '''
    code_block : statement code_block
               | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el bloque de código

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
    new_variable_statement : NEW VARNAME ',' '(' DATATYPE ',' value ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia New

def p_values_statement(p):
    '''
    values_statement : VALUES '(' VARNAME ',' value ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Values

def p_alter_statement(p):
    '''
    alter_statement : ALTER '(' VARNAME ',' OPERATOR ',' value ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Alter

def p_alterb_statement(p):
    '''
    alterb_statement : ALTERB '(' VARNAME ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia AlterB

def p_condition_statement(p):
    '''
    condition_statement : expression COMPARISON_OPERATOR expression
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia condicional

def p_istrue_statement(p):
    '''
    istrue_statement : ISTRUE '(' VARNAME ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia IsTrue

def p_repeat_statement(p):
    '''
    repeat_statement : REPEAT '(' code_block break_statement ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Repeat

def p_break_statement(p):
    '''
    break_statement : BREAK ';'
                    | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Break

def p_until_statement(p):
    '''
    until_statement : UNTIL code_block CONDITION ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Until

def p_while_statement(p):
    '''
    while_statement : WHILE expression '(' code_block ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia While

def p_case_statement(p):
    '''
    case_statement : CASE VARNAME case_when_statements else_statement ';'
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
    case_when_statement : WHEN value THEN code_block
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
    printvalues_statement : PRINTVALUES '(' VARNAME ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia PrintValues

def p_signal_statement(p):
    '''
    signal_statement : SIGNAL '(' VARNAME ',' value ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Signal

def p_viewsignal_statement(p):
    '''
    viewsignal_statement : VIEWSIGNAL '(' VARNAME ')' ';'
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia ViewSignal

def p_expression(p):
    '''
    expression : value
               | VARNAME
               | '(' expression ')'
               | expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una expresión matemática

def p_value(p):
    '''
    value : NUMBER
          | STRING
          | BOOLEAN
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

# Construcción del parser
parser = yacc.yacc()



# Prueba del parser
data = '''
// Nombre y funcionalidad del código

Proc @Master
(
  // Instrucciones
);

Proc nombre_del_procedimiento
(
  // Instrucciones
);
'''
parser.parse(data)
