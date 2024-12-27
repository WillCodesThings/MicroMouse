from machine import Pin
import utime
import uasyncio as asyncio

# Define the step sequence for the motor
STEP_SEQUENCE = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

# Class to handle motor steps
class MotorStep:
    def __init__(self, direction, steps, delay, stepper_pins, step_sequence=STEP_SEQUENCE):
        # Initialize stepper motor variables
        self.direction = direction
        self.steps = steps
        self.delay = delay
        self.stepper_pins = stepper_pins
        self.step_sequence = step_sequence
        self.step_index = 0

        # Input validation
        if self.steps <= 0:
            raise ValueError("Steps must be a positive integer.")
        if direction not in [-1, 1]:
            raise ValueError("Direction must be -1 or 1.")
        if delay <= 0:
            raise ValueError("Delay must be positive.")

    async def step(self):
        for i in range(self.steps):
            # Update the current step index considering the direction
            self.step_index = (self.step_index + self.direction) % len(self.step_sequence)

            # Set each pin's value based on the step sequence
            for pin_index, pin in enumerate(self.stepper_pins):
                pin_value = self.step_sequence[self.step_index][pin_index]
                pin.value(pin_value)

            # Debug log for step activity
            # print(f"Step {i+1}/{self.steps}: Index {self.step_index}, Pins: {[pin.value() for pin in self.stepper_pins]}")

            # Delay for the specified time
            await asyncio.sleep(self.delay)

# Class to handle stepper motor
class stepperMotor:
    def __init__(self, pins):
        self.pins = [Pin(pin, Pin.OUT) for pin in pins]

    async def step(self, direction, steps, delay=0.1):
        try:
            motor_step = MotorStep(direction, steps, delay, self.pins)
            await motor_step.step()
        except Exception as e:
            print(f"Error during step execution: {e}")

class SimultaneousMotorStep:

    def __init__(self) -> None:
        pass

    @staticmethod
    async def run_motors_simultaneously(left_motor, right_motor, direction_left, steps_left, delay_left, direction_right, steps_right, delay_right):
        # Run both motors concurrently
        await asyncio.gather(
            left_motor.step(direction_left, steps_left, delay_left),
            right_motor.step(direction_right, steps_right, delay_right)
        )


class DipSwitchSpeedControl:
    def __init__(self):
        self.dip1 = Pin(11, Pin.IN)
        self.dip2 = Pin(10, Pin.IN)
        self.dip3 = Pin(9, Pin.IN)
        self.dip4 = Pin(8, Pin.IN)

    def get_speed_delay(self):
        # Read DIP switch values
        dip_value = (1 - self.dip1.value() << 3) | (1- self.dip2.value() << 2) | (1- self.dip3.value() << 1) | 1- self.dip4.value()
        # Map DIP switch settings to delays
        print(f"Decimal Value: {dip_value}, dip1: {self.dip1.value()}, dip2: {self.dip2.value()}, dip3: {self.dip3.value()}, dip4: {self.dip4.value()}")
        speed_map = {
            0b0000: 0.01, # Fastest
            0b0001: 0.02,
            0b0010: 0.03,
            0b0011: 0.04,
            0b0100: 0.05,
            0b0101: 0.06,
            0b0110: 0.07,
            0b0111: 0.08,
            0b1000: 0.09,
            0b1001: 0.1,  # Slowest
        }
        return speed_map.get(dip_value, 0.01)  # Default to 0.01 if DIP setting is invalid
