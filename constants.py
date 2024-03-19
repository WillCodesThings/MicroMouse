from machine import Pin

class Constants:
    def __init__(self):
        self._STEPS_PER_CMD = 300

        self._MOTOR_STEP_RATE = 0.002

        self._L_FOREWARD = 1
        self._R_FOREWARD = -1

        self._L_BACKWARD = -1
        self._R_BACKWARD = 1

        self._MOTOR_PINS = [Pin(15, Pin.OUT), Pin(14, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT)]

        self._STEP_SEQUENCE = [
            [1, 0, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
        ]
    
    @property
    def L_FOREWARD(self):
        return self._L_FOREWARD
    
    @L_FOREWARD.setter
    def value(self, new_value):
        raise AttributeError("ERROR : Cannot change the value of an ImmutableValue instance.")
    
    @property
    def R_FOREWARD(self):
        return self._R_FOREWARD
    
    @R_FOREWARD.setter
    def value(self, new_value):
        raise AttributeError("ERROR : Cannot change the value of an ImmutableValue instance.")

    @property
    def L_BACKWARD(self):
        return self._L_BACKWARD
    
    @L_BACKWARD.setter
    def value(self, new_value):
        raise AttributeError("ERROR : Cannot change the value of an ImmutableValue instance.")
    
    @property
    def R_BACKWARD(self):
        return self._R_BACKWARD
    
    @R_BACKWARD.setter
    def value(self, new_value):
        raise AttributeError("ERROR : Cannot change the value of an ImmutableValue instance.")
    
    @property
    def MOTOR_PINS(self):
        return self._MOTOR_PINS
    
    @MOTOR_PINS.setter
    def value(self, new_value):
        raise AttributeError("ERROR : Cannot change the value of an ImmutableValue instance.")
    
    @property
    def STEP_SEQUENCE(self):
        return self._STEP_SEQUENCE
    
    @STEP_SEQUENCE.setter
    def value(self, new_value):
        raise AttributeError("ERROR : Cannot change the value of an ImmutableValue instance.")
    
    @property
    def MOTOR_STEP_RATE(self):
        return self._MOTOR_STEP_RATE
    
    @MOTOR_STEP_RATE.setter
    def value(self, new_value):
        raise AttributeError("ERROR : Cannot change the value of an ImmutableValue instance.")
    
    @property
    def STEPS_PER_CMD(self):
        return self._STEPS_PER_CMD
    
    @STEPS_PER_CMD.setter
    def value(self, new_value):
        raise AttributeError("ERROR : Cannot change the value of an ImmutableValue instance.")

    