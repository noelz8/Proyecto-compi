import ply.lex as lex

# Lista de nombres de tokens
tokens = [
    'ID',
    'INTEGER',
    'PLUS',
    'EQUAL',
    'LPAREN',
    'RPAREN'
]

# Definición de tokens
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INTEGER = r'\d+'
t_PLUS = r'\+'

t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignorar caracteres en blanco
t_ignore = ' \t'

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
