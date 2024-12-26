import utime
from machine import Pin
from constants import Constants
from subsystem.irSensor import IR_Sensor
from subsystem.stepperMotor import stepperMotor

# Define the pins for the stepper motor


# Define the sequence of steps for the motor to take
# step_sequence = [
#     [1, 0, 0, 1],
#     [1, 1, 0, 0],
#     [0, 1, 1, 0],
#     [0, 0, 1, 1],
# ]

IR_SENS_F = IR_Sensor(6)
#IR_SENS_L= Pin(1000, Pin.IN)
#IR_SENS_R = Pin(1000, Pin.IN)

mRight = stepperMotor(Constants.R_MOTOR_PINS)
mLeft = stepperMotor(Constants.L_MOTOR_PINS)


# Set the initial step index to 0
step_index = 0
# Take the specified number of steps in the anti-clockwise direction with a delay of 0.01 seconds between steps

while True:
    if IR_SENS_F.value() == 1:
        mRight.step(Constants.R_FOREWARD, Constants.STEPS_PER_CMD, Constants.MOTOR_STEP_RATE)
    else:
        mLeft.step(Constants.R_FOREWARD, Constants.STEPS_PER_CMD, Constants.MOTOR_STEP_RATE)
    
    
    
    