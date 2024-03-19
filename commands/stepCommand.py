from machine import Pin
from constants import Constants
import utime

class MotorStep:
    def __init__(self, direction, steps, delay, stepper_pins = Constants.MOTOR_PINS, step_sequence = Constants.STEP_SEQUENCE) -> None:
        self.direction = direction
        self.steps = steps
        self.delay = delay
        self.stepper_pins = stepper_pins
        self.step_index = 0
    
    def step(self):
        # Loop through the specified number of steps in the specified direction
        for i in range(self.steps):
            # Add the specified direction to the current step index to get the new step index
            step_index = (step_index + self.direction) % len(Constants.step_sequence)
            # Loop through each pin in the motor
            for pin_index in range(len(self.stepper_pins)):
                # Get the value for this pin from the step sequence using the current step index
                pin_value = self.step_sequence[step_index][pin_index] 
                # Set the pin to this value
                self.stepper_pins[pin_index].value(pin_value)
            # Delay for the specified amount of time before taking the next step
            utime.sleep(self.delay)