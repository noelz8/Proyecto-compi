import ply.yacc as yacc
from lex_parser import tokens

#Tabla de Simbolos
table_symbols = {} #Se crea un diccionario para las variables que vamos a almacenar

if len(table_symbols) > 0:
    # Hay datos en table_symbols
    # Puedes realizar las acciones correspondientes
    print("Se ha almacenado datos")
else:
    # table_symbols está vacío
    # Puedes mostrar un mensaje o realizar otras acciones
    print("No se ha almacenado datos")

#Tabla de expresiones
table_expressions = {}

# Definicion de errores
list_errors = []


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

    #En caso de que sea el siguiente:

    # proc MASTER LPARENTESIS comentario list_statement RPARENTESIS PUNTO_COMA group_proc
    if len(p) == 9:
        proc_name = p[1] # Conseguir el nombre del procedimiento
        comments = p[4] # Conseguir los comentarios del procedimiento
        statements = p[5] # Conseguir la lista de declaraciones de los procedimientos
        group_proc = p[8] # Conseguir el grupo de procedimientos
    
    # group_proc proc MASTER LPARENTESIS comentario list_statement RPARENTESIS PUNTO_COMA group_proc
    elif len(p) == 10:
        group_proc1 = p[1] # Conseguir el primer grupo de procedimientos
        proc_name = p[2] # Conseguir el nombre del procedimiento
        comments = p[5] # Conseguir los comentarios del procedimiento
        statements = p[6] # Conseguir la lista de declaraciones de los procedimientos
        group_proc2 = p[9] # Conseguir el segundo grupo de procedimientos
    
def p_proc(p):
    '''
    proc : PROC
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el proc

    p[0] = p[1] #Asigna a p[0] el nombre del procedimiento


def p_group_proc(p):
    '''
    group_proc : PROC VARIABLE LPARENTESIS COMENTARIO list_statement RPARENTESIS PUNTO_COMA group_proc
               | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el bloque de código

    if len(p) ==2:
        pass # En caso de que venga un grupo de procedimiento vacio
    else:
        variable = p[2] #obtiene el nombre de las variables en el procedimiento
        comment = p[4] # obtiene los comentarios del procedimiento
        statements = p[5] # obtiene la lista de declaraciones
        group_proc = p[8] # obtiene el siguiente grupo de procedimientos

def p_list_statement(p):
    '''
    list_statement : statement list_statement
                    | comentario
                    | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una lista de sentencias

    if len(p) == 2:
        if isinstance(p[1],str):
            pass
        else:
            pass
    else:
        p[0] = [p[1],p[2]]

def p_statement(p):
    '''
    statement : no_return_statement
              | return_statement
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia

    p[0] = p[1]

def p_no_return_statement(p):
    '''
    no_return_statement : new_variable_statement
                        | alterb_statement
                        | values_statement
                        | repeat_statement
                        | until_statement
                        | while_statement
                        | case_statement
                        | printvalues_statement
                        | signal_statement
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia que no retorna valor

    p[0] = p[1]

def p_return_statement(p):
    '''
    return_statement : return_num_statement
                     | return_bool_statement
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia que retorna valor

    p[0] = p[1]
def p_return_num_statement(p):
    '''
    return_num_statement : viewsignal_statement
                        | alter_statement
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia que retorna un valor numérico

    p[0] = p[1]

def p_return_bool_statement(p):
    '''
    return_bool_statement : condition_statement
                          | istrue_statement
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia que retorna un valor booleano

    p[0] = p[1]

def p_new_variable_statement(p):
    '''
    new_variable_statement : NEW VARIABLE COMA LPARENTESIS datatype COMA value RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia New

    variable = p[2]
    tipoDato = p[5]
    variable_value = p[7]

    if tipoDato == 'Bool' and type(variable_value) == bool: #Verifica que el tipo de dato sea igual al valor que se agrega
        if variable not in table_symbols:
            table_symbols[variable] = variable_value #Asigna el valor a la variable en el diccionario table_symbols
            p[0] = [p[1],variable,variable_value]
        else:
            print(f"Error de sintaxis: la variable {variable} ha sido ya declarada")

    elif tipoDato == 'Num' and type(variable_value) == int: #Verifica que el tipo de dato sea igual al valor que se agrega
        if variable not in table_symbols:
            table_symbols[variable] = variable_value #Asigna el valor a la variable en el diccionario table_symbols
            p[0] = [p[1],variable,variable_value]
        else:
            print(f"Error de sintaxis: la variable {variable} ha sido ya declarada")
    else:
        list_errors.append(f"Error de sintaxis: el tipo de dato {tipoDato} no coincide con el valor {variable_value}")
        print(f"Error de sintaxis: el tipo de dato {tipoDato} no coincide con el valor {variable_value}")
        

def p_values_statement(p):
    '''
    values_statement : VALUES LPARENTESIS VARIABLE COMA value RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Values

def p_alter_statement(p):
    '''
    alter_statement : ALTER LPARENTESIS VARIABLE COMA operador COMA return_num_statement RPARENTESIS PUNTO_COMA
                    | ALTER LPARENTESIS VARIABLE COMA operador COMA expression RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Alter

def p_operador(p):
    '''
    operador : ADD
            | SUB
            | MUL
            | DIV
    '''
    p[0] = p[1] # Se le asigna 

def p_alterb_statement(p):
    '''
    alterb_statement : ALTERB LPARENTESIS VARIABLE RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia AlterB

def p_condition_statement(p):
    '''
    condition_statement : expression condition expression
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
    until_statement : UNTIL LPARENTESIS list_statement RPARENTESIS condition_statement PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Until

def p_condition(p):
    '''
    condition :  MAYOR_QUE
                | MENOR_QUE
                | IGUAL
                | DISTINTO_QUE
                | MAYOR_IGUAL_QUE
                | MENOR_IGUAL_QUE
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una condición

    p[0] = p[1]

def p_while_statement(p):
    '''
    while_statement : WHILE condition_statement LPARENTESIS list_statement RPARENTESIS PUNTO_COMA
                    | WHILE istrue LPARENTESIS list_statement RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia While

def p_bool(p):
    '''
    bool : TRUE
         | FALSE
    '''
    # Aquí puedes realizar las acciones necesarias para procesar un valor booleano
    p[0] = p[1] # Asigna el valor del token a la varible p[0] en esa posición

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
    else_statement : list_statement
                   | empty
    '''
    # Aquí puedes realizar las acciones necesarias para procesar la cláusula Else en una sentencia Case

    p[0] = p[1] # Asigna el valor del token a la varible p[0] en esa posición

def p_printvalues_statement(p):
    '''
    printvalues_statement : PRINTVALUES LPARENTESIS list_content_print RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia PrintValues
def p_list_content_print(p):
    '''
    list_content_print : content_print COMA list_content_print
                       | content_print
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una lista de contenido de una sentencia PrintValues
def p_content_print(p):
    '''
    content_print : STRING
                  | VARIABLE
                  | value
    '''
    # Aquí puedes realizar las acciones necesarias para procesar el contenido de una sentencia PrintValues

    p[0] = p[1] # Asigna el valor del token a la varible p[0] en esa posición
def p_signal_statement(p):
    '''
    signal_statement : SIGNAL LPARENTESIS VARIABLE COMA return_num_statement RPARENTESIS PUNTO_COMA
                     | SIGNAL LPARENTESIS VARIABLE COMA expression RPARENTESIS PUNTO_COMA

    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia Signal

def p_viewsignal_statement(p):
    '''
    viewsignal_statement : VIEWSIGNAL LPARENTESIS VARIABLE RPARENTESIS PUNTO_COMA
                        | VIEWSIGNAL LPARENTESIS expression RPARENTESIS PUNTO_COMA
                        | VIEWSIGNAL LPARENTESIS alter_statement RPARENTESIS PUNTO_COMA
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una sentencia ViewSignal

def p_expression(p):
    '''
    expression : NUMERO
               | VARIABLE
               | LPARENTESIS expression RPARENTESIS
               | expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una expresión matemática

    p[0] = p[1] # Asigna el valor del token a la varible p[0] en esa posición

def p_istrue(p):
    '''
    istrue : ISTRUE LPARENTESIS VARIABLE RPARENTESIS
    '''
    # Aquí puedes realizar las acciones necesarias para procesar una expresión booleana

def p_value(p):
    '''
    value : expression
          | bool
          | return_num_statement
          | return_bool_statement
    '''
    # Aquí puedes realizar las acciones necesarias para procesar un valor

    p[0] = p[1] # Asigna el valor del token a la varible p[0] en esa posición

def p_datatype(p):
    '''
    datatype : NUMERO 
             | BOOL
    '''
    p[0] = p[1] # Asigna el valor del token a la varible p[0] en esa posición

def p_empty(p):
    '''
    empty :
    '''
    pass

# Manejo de errores de sintaxis
def p_error(p):
    print("Error de sintaxis en la entrada:", p)

parser = yacc.yacc()

# Prueba del parser
data = '''
//Nombre y funcionalidad del código
Proc @Master
(
    // Comentario de prueba
    New @variable1,(Bool, True);
    New @variable3,(Num, 5);
    Values (@variable1, False);

    Values (@variable2, True);
    While IsTrue(@variable2)
        ( Signal(@variable2, 1);
        AlterB (@variable2);
);
);
Proc @Procesofoo (
    // Comentario de prueba 
    Values (@variable1, 100);
    While @variable1 > 10
        (PrintValues("valor de prueba");
        Signal(@variale1, 1);
        Values (@variable1, Alter (@variable1,SUB, 10););
 );
);'''

parser.parse(data)
