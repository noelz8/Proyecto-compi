from lex_parser import lexer
from yacc_parser import parser

#Este es el archivo princial

# Cadena de entrada
input_string = "2 + 3"


# Establecer el analizador léxico
lexer.input(input_string)

# Analizar la cadena de entrada
result = parser.parse(input_string)

# Imprimir el resultado
print(result)

