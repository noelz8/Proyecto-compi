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
    'SLASH',
    'COMENTARIO',
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
    'ID'
]
reserved = {
    
    'Proc': 'PROC',
    '@Master': 'MASTER',
    'CALL': 'CALL',
    'New': 'NEW',
    'Alter': 'ALTER',
    'ADD':'ADD',
    'SUB':'SUB',
    'MUL':'MUL',
    'DIV':'DIV',
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
    'Values': 'VALUES'
}

cond_Numericas = {
    '>':'MAYOR_QUE',
    '<':'MENOR_QUE',
    '==':'IGUAL',
    '<>':'DISTINTO_QUE',
    '>=':'MAYOR_IGUAL_QUE',
    '<=':'MENOR_IGUAL_QUE'
}
# Definición de tokens
t_TILDE = r'[áéíóúÁÉÍÓÚ]'
t_LETRA = r'[a-zA-ZáéíóúÁÉÍÓÚüÜ]'
t_NUMERO = r'\d+'
t_COMENTARIO = r'//'
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
t_SLASH = r'/'
t_LPARENTESIS = r'\('
t_RPARENTESIS = r'[\)]'
t_IZQ_INTERROGACION = r'\¿'
t_DER_INTERROGACION = r'\?'
t_IZQ_EXCLAMACION = r'¡'
t_DER_EXCLAMACION = r'!'

# Ignorar caracteres en blanco
t_ignore = ' \t'

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
data = '''// Nombre y funcionalidad del código

Proc @Master
(
  
    Values (@variable2, True);
    While IsTrue(@variale2)
        ( Signal(@variale2, 1);
        AlterB (@variable2);
);
    Values (@variable1, 100);
    While @variable1 > 10
        ( Signal(@variale1, 1);
        Values (@variable1,
        Alter (@variable1,SUB, 10));
 );
);'''
lexer.input(data)
while True:
    token = lexer.token()
    if not token:
        break
    print(token)