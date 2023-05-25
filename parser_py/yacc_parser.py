
import ply.yacc as yacc
from lex_parser import tokens

# Reglas de precedencia
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
)

# Definición de la gramática
def p_program(p):
    '''
    program : comentario procedimientos
    '''
    # Acciones semánticas correspondientes
    # ...

def p_comentario(p):
    '''
    comentario : COMENTARIO
    '''
    # Acciones semánticas correspondientes
    # ...

def p_procedimientos(p):
    '''
    procedimientos : procedimiento
                   | procedimientos procedimiento
    '''
    # Acciones semánticas correspondientes
    # ...

def p_procedimiento(p):
    '''
    procedimiento : PROC ID '(' cuerpo_procedimiento ')'
    '''
    # Acciones semánticas correspondientes
    # ...

def p_cuerpo_procedimiento(p):
    '''
    cuerpo_procedimiento : instrucciones
    '''
    # Acciones semánticas correspondientes
    # ...

def p_instrucciones(p):
    '''
    instrucciones : instruccion
                  | instrucciones instruccion
    '''
    # Acciones semánticas correspondientes
    # ...

def p_instruccion(p):
    '''
    instruccion : asignacion
                | llamada_procedimiento
    '''
    # Acciones semánticas correspondientes
    # ...

def p_asignacion(p):
    '''
    asignacion : ID '=' expresion ';'
    '''
    # Acciones semánticas correspondientes
    # ...

def p_llamada_procedimiento(p):
    '''
    llamada_procedimiento : CALL '(' ID ')' ';'
    '''
    # Acciones semánticas correspondientes
    # ...

def p_expresion(p):
    '''
    expresion : NUMERO
              | ID
              | expresion SUMA expresion
              | expresion RESTA expresion
              | expresion MULTIPLICACION expresion
              | expresion DIVISION expresion
    '''
    # Acciones semánticas correspondientes
    # ...

# Manejo de errores de análisis sintáctico
def p_error(p):
    print("Error de sintaxis:", p)

# Construir el parser
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
