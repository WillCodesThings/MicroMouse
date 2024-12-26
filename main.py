# import utime
# from machine import Pin
# from subsystem.stepperMotor import stepperMotor
from subsystem.irSensor import IR_Sensor

# Define the pins for the stepper motor
# stepper_pins = [Pin(12, Pin.OUT), Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT)]

# LeftMotor = stepperMotor(stepper_pins)
# RightMotor = stepperMotor(stepper_pins)
LSensor, FSensor, RSensor= IR_Sensor(33), IR_Sensor(44), IR_Sensor(51)

# Everytime variable is accessed it will poll new sensor data
valueTuple = lambda: (LSensor.value(), FSensor.value(), RSensor.value())

### Testing
# valueTuple = lambda: (0, 0, 0)
# valueTuple = lambda: (0, 0, 1)
# valueTuple = lambda: (0, 1, 1)
# valueTuple = lambda: (1, 1, 1)
###

# # Take the specified number of steps in the anti-clockwise direction with a delay of 0.01 seconds between steps
# step(1, 500, 0.01)
# # Take the specified number of steps in the clockwise direction with a delay of 0.01 seconds between steps
# step(-1, 500, 0.01)

def turnRight():
    print("turning right")
def turnLeft():
    print("turning left")
def action():
    print("moving forward")

def simpeFigure(valueTuple):
    # Unpack sensor data to get all values at once
    initTuple = valueTuple

    if initTuple[2] == 0:
        turnRight()
        action()
    elif initTuple[1]== 0:
        action()
    elif initTuple[0] == 0:
        turnLeft()
        action()
    else: 
        turnLeft()

for h in range(2):
    for j in range(2):
        for i in range(2):
            valueTuple = (i, j, h)
            print(f"\n\n Case ({i},{j},{h})")
            print(valueTuple)
            simpeFigure(valueTuple)
            print("\n\n")
