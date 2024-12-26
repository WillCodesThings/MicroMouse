import machine
import utime
from constants import Constants
from commands.stepCommand import MotorStep

class stepperMotor:
    def __init__(self, pins):
        self.pins = pins
        self.step_index = 0

    def step(self, direction, steps, delay=0.1):
        motorStep = MotorStep(direction, steps, delay, self.pins)
        motorStep.step()
        return True

    
