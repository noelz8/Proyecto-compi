import ply.lex as lex
import re
# Lista de nombres de tokens
tokens = [
    # Alfabeto completo en español
    'LETRA',
    # Números
    'NUMERO',
    # Tildes y ñ
    'TILDE',
    'ENYE',
    'COMENTARIO',
    # Símbolos especiales
    'SUMA',
    'RESTA',
    'DIVISION',
    'MULTIPLICACION',
    'IGUALDAD',
    # Puntuación
    'PUNTO',
    'COMA',
    'MAYUSCULA',
    'PUNTO_COMA',
    'COMILLAS',
    'GUION',
    'UNDERSCORE',
    'ARROBA',
    'LPARENTESIS',
    'RPARENTESIS',
    'IZQ_INTERROGACION',
    'DER_INTERROGACION',
    'IZQ_EXCLAMACION',
    'DER_EXCLAMACION',
    #Condiciones numericas
    'MAYOR_QUE',
    'MENOR_QUE',
    'IGUAL',
    'DISTINTO_QUE',
    'MAYOR_IGUAL_QUE',
    'MENOR_IGUAL_QUE',
    #Palabras reservadas
    'PROC',
    'MASTER',
    'CALL',
    'NEW',
    'ALTER',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'ALTERB',
    'SIGNAL',
    'VIEWSIGNAL',
    'ISTRUE',
    'REPEAT',
    'BREAK',
    'UNTIL',
    'WHILE',
    'CASE',
    'WHEN',
    'THEN',
    'ELSE',
    'PRINTVALUES',
    'VALUES',
    'ID',
    'VARIABLE',
    'TRUE',
    'FALSE',
    'STRING',
    'COND_NUMERICA',
    'OPERADOR',
    'DATATYPE',
    'BOOL'
]
datatype ={
    'Num':'NUM',
    'Bool':'BOOL'
}

reserved = {
    
    'Proc': 'PROC',
    '@Master': 'MASTER',
    'CALL': 'CALL',
    'New': 'NEW',
    'Alter': 'ALTER',
    'AlterB':'ALTERB',
    'Signal': 'SIGNAL',
    'ViewSignal':'VIEWSIGNAL',
    'IsTrue': 'ISTRUE',
    'Repeat':'REPEAT',
    'break': 'BREAK',
    'Until': 'UNTIL',
    'While': 'WHILE',
    'Case': 'CASE',
    'When':'WHEN',
    'Then':'THEN',
    'else': 'ELSE',
    'PrintValues': 'PRINTVALUES',
    'Values': 'VALUES',
    'ADD':'ADD',
    'SUB':'SUB',
    'MUL':'MUL',
    'DIV':'DIV'  
}




# Definición de tokens
t_TILDE = r'[áéíóúÁÉÍÓÚ]'
t_LETRA = r'[a-zA-ZáéíóúÁÉÍÓÚüÜ]'
t_NUMERO = r'\d+'
t_ENYE = r'ñ'
t_SUMA = r'\+'
t_RESTA = r'-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'
t_IGUALDAD = r'='
t_PUNTO = r'\.'
t_COMA = r','
t_MAYUSCULA = r'[A-Z]'
t_PUNTO_COMA = r';'
t_COMILLAS = r'\"'
t_GUION = r'-'
t_UNDERSCORE = r'_'
t_ARROBA = r'@'
t_LPARENTESIS = r'\('
t_RPARENTESIS = r'[\)]'
t_IZQ_INTERROGACION = r'\¿'
t_DER_INTERROGACION = r'\?'
t_IZQ_EXCLAMACION = r'¡'
t_DER_EXCLAMACION = r'!'

# Ignorar caracteres en blanco
t_ignore = ' \t'

cond_Numericas = {
    '>':'MAYOR_QUE',
    '<':'MENOR_QUE',
    '==':'IGUAL',
    '<>':'DISTINTO_QUE',
    '>=':'MAYOR_IGUAL_QUE',
    '<=':'MENOR_IGUAL_QUE'
}
def t_COMENTARIO(t):
    r'\/\/.*'
    t.type = 'COMENTARIO'
    return t  # Descarta los comentarios


def t_DATATYPE(t):
    r'Num|Bool'
    t.type = datatype.get(t.value)
    return t

# Regla para booleanos
def t_BOOL(t):
    r'True|False'
    t.type = reserved.get(t.value)
    return t

# Regla para la variable
def t_VARIABLE(t):
    r'@[?\w]{1,11}'
    if len(t.value) > 12:
        print("Error: La variable excede el máximo de 12 posiciones")
        t.lexer.skip(1)
    elif len(t.value) < 2:
        print("Error: La variable debe tener al menos 2 posiciones")
        t.lexer.skip(1)
    elif t.value[0] != '@':
        print("Error: La variable debe iniciar con una arroba (@)")
        t.lexer.skip(1)  
    else:
        # Verificar si es una palabra reservada
        if t.value in reserved:
            t.type = reserved[t.value]
        return t

# Regla para el operador
def t_OPERADOR(t):
    r'ADD|SUB|MUL|DIV'
    t.type = reserved.get(t.value)
    return t  


def t_COND_NUMERICA(t):
    r'>|<|==|<>|>=|<='
    t.type = cond_Numericas.get(t.value)
    return t

def t_RESERVED(t):
    r'[a-zA-Z_@][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Regla para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regla para manejar errores de caracteres no válidos
def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()