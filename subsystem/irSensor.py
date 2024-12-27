from machine import Pin

class IR_Sensor:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.IN)
        pass
    
    def value(self):
        print(((self.pin.value() + 1) % 2))
        return ((self.pin.value() + 1) % 2)
        # return 1
