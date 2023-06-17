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
    'ALTERB',
    'ALTER',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
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
    'DATATYPE',
    'BOOL',
    'BOOLEAN'
]
datatype ={
    'Num':'NUMERO',
    'Bool':'BOOL'
}

# Definición de tokens
t_TILDE = r'[áéíóúÁÉÍÓÚ]'
t_LETRA = r'[a-zA-ZáéíóúÁÉÍÓÚüÜ]'
#t_NUMERO = r'\d+'
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
# Definicion de palabras reservadas
def t_MASTER(t):
    r'@Master'
    t.type = 'MASTER'
    return t

def t_CALL(t):
    r'CALL'
    t.type = 'CALL'
    return t

def t_NEW(t):
    r'New'
    t.type = 'NEW'
    return t

def t_ALTERB(t):
    r'AlterB'
    t.type = 'ALTERB'
    return t

def t_ALTER(t):
    r'Alter'
    t.type = 'ALTER'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
  
def t_BOOLEAN(t):
    r'(True|False)'
    if t.value == 'True':
        t.value = True
    elif t.value == 'False':
        t.value = False
    return t

def t_SIGNAL(t):
    r'Signal'
    t.type = 'SIGNAL'
    return t

def t_VIEWSIGNAL(t):
    r'ViewSignal'
    t.type = 'VIEWSIGNAL'
    return t

def t_ISTRUE(t):
    r'IsTrue'
    t.type = 'ISTRUE'
    return t

def t_REPEAT(t):
    r'Repeat'
    t.type = 'REPEAT'
    return t

def t_BREAK(t):
    r'break'
    t.type = 'BREAK'
    return t

def t_UNTIL(t):
    r'Until'
    t.type = 'UNTIL'
    return t

def t_WHILE(t):
    r'While'
    t.type = 'WHILE'
    return t

def t_CASE(t):
    r'Case'
    t.type = 'CASE'
    return t

def t_WHEN(t):
    r'When'
    t.type = 'WHEN'
    return t

def t_THEN(t):
    r'Then'
    t.type = 'THEN'
    return t

def t_ELSE(t):
    r'else'
    t.type = 'ELSE'
    return t

def t_PRINTVALUES(t):
    r'PrintValues'
    t.type = 'PRINTVALUES'
    return t

def t_VALUES(t):
    r'Values'
    t.type = 'VALUES'
    return t

def t_ADD(t):
    r'ADD'
    t.type = 'ADD'
    return t

def t_SUB(t):
    r'SUB'
    t.type = 'SUB'
    return t

def t_MUL(t):
    r'MUL'
    t.type = 'MUL'
    return t

def t_DIV(t):
    r'DIV'
    t.type = 'DIV'
    return t

def t_TRUE(t):
    r'True'
    t.type = 'TRUE'
    return t

def t_FALSE(t):
    r'False'
    t.type = 'FALSE'
    return t

def t_PROC(t):
    r'Proc'
    t.type = 'PROC'
    return t

def t_COMENTARIO(t):
    r'\/\/.*'
    t.type = 'COMENTARIO'
    return t  # Descarta los comentarios

def t_DATATYPE(t):
    r'Num|Bool'
    t.type = datatype.get(t.value)
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
        return t
    
def t_COND_NUMERICA(t):
    r'>|<|==|<>|>=|<='
    t.type = cond_Numericas.get(t.value)
    return t

def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]  # Eliminar las comillas alrededor del string
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
data = '''
//Nombre y funcionalidad del código
Proc @Master
(
    // Comentario de prueba
    New @variable3,(Num, 5);

    New @variable4,(Bool, True);
    
    Values (@variable3, 90);

    Values (@variable3, Alter(@variable3, MUL, 5););

    

    3 > 4

    @variable3 > 4

    While IsTrue(@variable4)
    (   Values (@variable3, 100);
    
        Values (@variable3, 150);

        Values(@variable3, Alter(@variable3, MUL, 5););
        AlterB(@variable4);
    );

    Repeat(
        Values (@variable3, 1);
        Signal(@variable3,1);
        break;
    );

    Until(
    Values(@variable3,Alter(@variable3, SUB, 50););
    )@variable3 < 50;

    PrintValues("Esto es un comentario " , @variable3);

    New @variable5,(Num, 5);

    Case @variable5
        When 1 Then
            ( Signal(1, 1);)
        When 2 Then
            ( Signal(2, 1);)
        When 5 Then
            ( Signal(3, 1););
    
    
);
'''

lexer.input(data)
while True:
    token = lexer.token()
    if not token:
        break
    print(token)