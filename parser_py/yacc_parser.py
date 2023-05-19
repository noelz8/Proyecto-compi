
import ply.yacc as yacc
from lex_parser import tokens

# Definición de reglas de producción
def p_expression(p):
    'expression : INTEGER PLUS INTEGER'
    p[0] = p[1] + p[3]

# Regla para manejar errores de sintaxis
def p_error(p):
    print("Error de sintaxis en la entrada")

# Crear el analizador sintáctico
parser = yacc.yacc()

