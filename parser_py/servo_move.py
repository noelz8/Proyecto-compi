from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM9'
board = Arduino(port)
pin = [3, 5, 6, 9, 10, 11]


for i in pin:
    board.digital[i].mode = SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

while True:
    rotateServo(3, 90)
    sleep(1)
    rotateServo(5, 90)
    sleep(1)
    rotateServo(5, 0)
    rotateServo(9, 90)
    sleep(1)
    rotateServo(3, 0)
    rotateServo(9, 0)
    sleep(100)
    