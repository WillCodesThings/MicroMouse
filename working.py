import utime
from machine import Pin
from constants import Constants

# Define the pins for the stepper motor


# Define the sequence of steps for the motor to take
step_sequence = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
]

IR_SENS_F = Pin(6, Pin.IN)
#IR_SENS_L= Pin(1000, Pin.IN)
#IR_SENS_R = Pin(1000, Pin.IN)

def step(direction, steps, delay, stepper_pins = Constants.MOTOR_PINS):
    # Use the global step_index variable so that it can be modified by this function
    global step_index
    # Loop through the specified number of steps in the specified direction
    for i in range(steps):
        # Add the specified direction to the current step index to get the new step index
        step_index = (step_index + direction) % len(step_sequence)
        # Loop through each pin in the motor
        for pin_index in range(len(stepper_pins)):
            # Get the value for this pin from the step sequence using the current step index
            pin_value = step_sequence[step_index][pin_index] 
            # Set the pin to this value
            stepper_pins[pin_index].value(pin_value)
        # Delay for the specified amount of time before taking the next step
        utime.sleep(delay)
# Set the initial step index to 0
step_index = 0
# Take the specified number of steps in the anti-clockwise direction with a delay of 0.01 seconds between steps

while True:
    if IR_SENS_F.value() == 0:
        step(Constants.R_FOREWARD, Constants.STEPS_PER_CMD, Constants.MOTOR_STEP_RATE)
    
    
    
    