from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM9'
board = Arduino(port)
pin = [3, 5, 6, 9, 10, 11]

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

# Setup
for i in pin:
    board.digital[i].mode = SERVO

# Loop
while True:
    # # a
    # rotateServo(pin[0], 40)
    # sleep(1)
    # # b
    # rotateServo(pin[1], 40)
    # sleep(1)
    # # c
    # rotateServo(pin[1], 0)
    # rotateServo(pin[3], 40)
    # sleep(1)
    # # d
    # rotateServo(pin[4], 40)
    # sleep(1)
    # # e
    # rotateServo(pin[3], 0)
    # sleep(1)
    # # f
    # rotateServo(pin[1], 40)
    # rotateServo(pin[3], 40)
    # rotateServo(pin[4], 0)
    # sleep(1)
    # # g
    # rotateServo(pin[4], 40)
    # sleep(1)
    # # h
    # rotateServo(pin[3], 0)
    # sleep(1)
    # # i
    # rotateServo(pin[0], 0)
    # rotateServo(pin[3], 40)
    # rotateServo(pin[4], 0)
    # sleep(1)
    # # j
    # rotateServo(pin[4], 40)
    # sleep(1)
    # # k
    # rotateServo(pin[0], 40)
    # rotateServo(pin[1], 0)
    # rotateServo(pin[2], 40)
    # rotateServo(pin[3], 0)
    # rotateServo(pin[4], 0)
    # sleep(1)
    # # l
    # rotateServo(pin[1], 40)
    # sleep(1)
    # # m
    # rotateServo(pin[1], 0)
    # rotateServo(pin[3], 40)
    # sleep(1)
    # # n
    # rotateServo(pin[4], 40)
    # sleep(1)
    # # ñ
    # rotateServo(pin[1], 40)
    # rotateServo(pin[2], 0)
    # rotateServo(pin[5], 40)
    # sleep(1)
    # # o
    # rotateServo(pin[1], 0)
    # rotateServo(pin[2], 40)
    # rotateServo(pin[3], 0)
    # rotateServo(pin[5], 0)
    # sleep(1)
    # # p
    # rotateServo(pin[1], 40)
    # rotateServo(pin[3], 40)
    # rotateServo(pin[4], 0)
    # sleep(1)
    # # q
    # rotateServo(pin[4], 40)
    # sleep(1)
    # # r
    # rotateServo(pin[3], 0)
    # sleep(1)
    # # s
    # rotateServo(pin[0], 0)
    # rotateServo(pin[4], 0)
    # rotateServo(pin[3], 40)

    # sleep(1)
    # rotateServo(pin[0], 0)
    # rotateServo(pin[1], 0)
    # rotateServo(pin[2], 0)
    # rotateServo(pin[3], 0)
    # rotateServo(pin[4], 0)
    # rotateServo(pin[5], 0)
    # sleep(1)

    for i in pin:
        rotateServo(i, 40)
    sleep(1)
    for i in pin:
        rotateServo(i, 0)
    sleep(1)

    # rotateServo(pin[5], 50)
    # sleep(1)
    # rotateServo(pin[5], 0)
    # sleep(1)
