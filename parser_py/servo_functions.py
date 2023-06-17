from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM9' # Cambiar por el puerto en el que se conecte el Arduino
board = Arduino(port)
pin = [3, 5, 6, 9, 10, 11]
servosState = [0, 0, 0, 0, 0, 0]

def rotateServo(servo, angle):
    board.digital[pin[servo]].write(angle*40)
    servosState[servo] = angle
    sleep(0.015)

def stateServo(servo):
    return servosState[pin[servo]]

# Setup
for i in pin:
    board.digital[i].mode = SERVO

# Test servos
for i in range(6):
    rotateServo(5-i, 1)
    sleep(0.1)
    rotateServo(5-i, 0)
    sleep(0.1)

