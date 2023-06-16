from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM9' # Cambiar por el puerto en el que se conecte el Arduino
board = Arduino(port)
pin = [3, 5, 6, 9, 10, 11]
servosState = [0, 0, 0, 0, 0, 0]

def rotateServo(servo, angle):
    board.digital[pin[servo]].write(angle)
    if angle == 0:
        servosState[servo] = 0
    else:
        servosState[servo] = 1
    sleep(0.015)

def stateServo(servo):
    return servosState[pin[servo]]

# Setup
for i in pin:
    board.digital[i].mode = SERVO

# Loop
while True:
    for i in range(len(pin)):
        rotateServo(i, 40)
    sleep(1)
    for i in range(len(pin)):
        rotateServo(i, 0)
    sleep(1)
    # board.exit()


