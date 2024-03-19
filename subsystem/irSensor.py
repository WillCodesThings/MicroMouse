from machine import Pin

class IR_Sensor:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN)
    
    def value(self):
        return self.pin.value()