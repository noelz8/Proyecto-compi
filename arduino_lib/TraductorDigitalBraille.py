from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM9'
board = Arduino(port)
pin = [3, 5, 6, 9, 10, 11]
global writeNumbers
writeNumbers = False

# Letras
char_a = [1, 0, 0, 0, 0, 0]
char_b = [1, 1, 0, 0, 0, 0]
char_c = [1, 0, 0, 1, 0, 0]
char_d = [1, 0, 0, 1, 1, 0]
char_e = [1, 0, 0, 0, 1, 0]
char_f = [1, 1, 0, 1, 0, 0]
char_g = [1, 1, 0, 1, 1, 0]
char_h = [1, 1, 0, 0, 1, 0]
char_i = [0, 1, 0, 1, 0, 0]
char_j = [0, 1, 0, 1, 1, 0]
char_k = [1, 0, 1, 0, 0, 0]
char_l = [1, 1, 1, 0, 0, 0]
char_m = [1, 0, 1, 1, 0, 0]
char_n = [1, 0, 1, 1, 1, 0]
char_nE = [1, 1, 0, 1, 1, 1]
char_o = [1, 0, 1, 0, 1, 0]
char_p = [1, 1, 1, 1, 0, 0]
char_q = [1, 1, 1, 1, 1, 0]
char_r = [1, 1, 1, 0, 1, 0]
char_s = [0, 1, 1, 1, 0, 0]
char_t = [0, 1, 1, 1, 1, 0]
char_u = [1, 0, 1, 0, 0, 1]
char_v = [1, 1, 1, 0, 0, 1]
char_w = [0, 1, 0, 1, 1, 1]
char_x = [1, 0, 1, 1, 0, 1]
char_y = [1, 0, 1, 1, 1, 1]
char_z = [1, 0, 1, 0, 1, 1]
char_aT = [1, 1, 1, 0, 1, 1]
char_eT = [0, 1, 1, 1, 0, 1]
char_iT = [0, 0, 1, 1, 0, 0]
char_oT = [0, 0, 1, 1, 0, 1]
char_uT = [0, 1, 1, 1, 1, 1]
char_uE = [1, 1, 0, 0, 1, 1]
charMayus = [0, 0, 0, 1, 0, 1]
charPunto = [0, 0, 1, 0, 0, 0]
charComa = [0, 1, 0, 0, 0, 0]
charPuntoComa = [0, 1, 1, 0, 0, 0]
charComillas = [0, 1, 1, 0, 0, 1]
charGuion = [0, 0, 1, 0, 0, 1]
charParentesisAbierto = [1, 1, 0, 0, 0, 1]
charParentesisCerrado = [0, 0, 1, 1, 1, 0]
charInterrogacion = [0, 1, 0, 0, 0, 1]
charExclamacion = [0, 1, 1, 0, 1, 0]
charInterruptor = [0, 0, 0, 0, 1, 0]

# Numeros
charNumero = [0, 0, 1, 1, 1, 1]
char1 = [1, 0, 0, 0, 0, 0]
char2 = [1, 1, 0, 0, 0, 0]
char3 = [1, 0, 0, 1, 0, 0]
char4 = [1, 0, 0, 1, 1, 0]
char5 = [1, 0, 0, 0, 1, 0]
char6 = [1, 1, 0, 1, 0, 0]
char7 = [1, 1, 0, 1, 1, 0]
char8 = [1, 1, 0, 0, 1, 0]
char9 = [0, 1, 0, 1, 0, 0]
char0 = [0, 1, 0, 1, 1, 0]
charSuma = [0, 1, 1, 0, 1, 0]
charResta = [0, 0, 1, 0, 0, 1]
charMultiplicacion = [0, 1, 1, 0, 0, 1]
charDivision = [0, 1, 0, 0, 1, 1]
charIgual = [0, 1, 1, 0, 1, 1]

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

def showChar(char):
    for i in range(6):
        if char[i] == 1:
            rotateServo(pin[i], 40)
        else:
            rotateServo(pin[i], 0)

def sendBrailleChar(char):
    global writeNumbers
    if char.isupper() and writeNumbers == False:
        showChar(charMayus)
        char = char.lower()
        sleep(1)
    elif char.isupper() and writeNumbers == True:
        showChar(charInterruptor)
        sleep(1)
        showChar(charMayus)
        sleep(1)
        char = char.lower()
        writeNumbers = False
    elif char.islower() and writeNumbers == True:
        showChar(charInterruptor)
        writeNumbers = False
        sleep(1)
    elif char.isdigit() and writeNumbers == False:
        showChar(charNumero)
        writeNumbers = True
        sleep(1)

    # 1
    if char == '1' and writeNumbers == True:
        showChar(char1)
    # 2
    elif char == '2' and writeNumbers == True:
        showChar(char2)
    # 3
    elif char == '3' and writeNumbers == True:
        showChar(char3)
    # 4
    elif char == '4' and writeNumbers == True:
        showChar(char4)
    # 5
    elif char == '5' and writeNumbers == True:
        showChar(char5)
    # 6
    elif char == '6' and writeNumbers == True:
        showChar(char6)
    # 7
    elif char == '7' and writeNumbers == True:
        showChar(char7)
    # 8
    elif char == '8' and writeNumbers == True:
        showChar(char8)
    # 9
    elif char == '9' and writeNumbers == True:
        showChar(char9)
    # 0
    elif char == '0' and writeNumbers == True:
        showChar(char0)
    # +
    elif char == '+' and writeNumbers == True:
        showChar(charSuma)
    # -
    elif char == '-' and writeNumbers == True:
        showChar(charResta)
    # *
    elif char == '*' and writeNumbers == True:
        showChar(charMultiplicacion)
    # /
    elif char == '/' and writeNumbers == True:
        showChar(charDivision)
    # =
    elif char == '=' and writeNumbers == True:
        showChar(charIgual)
    # a
    elif char == 'a':
        showChar(char_a)
    # b
    elif char == 'b':
        showChar(char_b)
    # c
    elif char == 'c':
        showChar(char_c)
    # d
    elif char == 'd':
        showChar(char_d)
    # e
    elif char == 'e':
        showChar(char_e)
    # f
    elif char == 'f':
        showChar(char_f)
    # g
    elif char == 'g':
        showChar(char_g)
    # h
    elif char == 'h':
        showChar(char_h)
    # i
    elif char == 'i':
        showChar(char_i)
    # j
    elif char == 'j':
        showChar(char_j)
    # k
    elif char == 'k':
        showChar(char_k)
    # l
    elif char == 'l':
        showChar(char_l)
    # m
    elif char == 'm':
        showChar(char_m)
    # n
    elif char == 'n':
        showChar(char_n)
    # ñ
    elif char == 'ñ':
        showChar(char_nE)
    # o
    elif char == 'o':
        showChar(char_o)
    # p
    elif char == 'p':
        showChar(char_p)
    # q
    elif char == 'q':
        showChar(char_q)
    # r
    elif char == 'r':
        showChar(char_r)
    # s
    elif char == 's':
        showChar(char_s)
    # t
    elif char == 't':
        showChar(char_t)
    # u
    elif char == 'u':
        showChar(char_u)
    # v
    elif char == 'v':
        showChar(char_v)
    # w
    elif char == 'w':
        showChar(char_w)
    # x
    elif char == 'x':
        showChar(char_x)
    # y
    elif char == 'y':
        showChar(char_y)
    # z
    elif char == 'z':
        showChar(char_z)
    # á
    elif char == 'á':
        showChar(char_aT)
    # é
    elif char == 'é':
        showChar(char_eT)
    # í
    elif char == 'í':
        showChar(char_iT)
    # ó
    elif char == 'ó':
        showChar(char_oT)
    # ú
    elif char == 'ú':
        showChar(char_uT)
    # ü
    elif char == 'ü':
        showChar(char_uE)
    # .
    elif char == '.':
        showChar(charPunto)
    # ,
    elif char == ',':
        showChar(charComa)
    # ;
    elif char == ';':
        showChar(charPuntoComa)
    # "
    elif char == '"':
        showChar(charComillas)
    # -
    elif char == '-':
        showChar(charGuion)
    # (
    elif char == '(':
        showChar(charParentesisAbierto)
    # )
    elif char == ')':
        showChar(charParentesisCerrado)
    # ?
    elif char == '?':
        showChar(charInterrogacion)
    # !
    elif char == '!':
        showChar(charExclamacion)
    # other characters
    else:
        rotateServo(pin[0], 0)
        rotateServo(pin[1], 0)
        rotateServo(pin[2], 0)
        rotateServo(pin[3], 0)
        rotateServo(pin[4], 0)
        rotateServo(pin[5], 0) 
    sleep(1)

def sendBrailleString(string):
    for char in string:
        sendBrailleChar(char)

# Setup
for i in pin:
    board.digital[i].mode = SERVO

for i in pin:
    rotateServo(i, 40)
sleep(0.015)
for i in pin:
    rotateServo(i, 0)
sleep(0.015)

# Loop
while True:
    text = input("Ingrese una palabra: ")
    sendBrailleString(text)