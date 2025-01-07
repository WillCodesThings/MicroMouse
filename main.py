import utime
from machine import Pin
from subsystem.stepperMotor import stepperMotor, SimultaneousMotorStep, DipSwitchSpeedControl
from subsystem.irSensor import IR_Sensor
import uasyncio as asyncio

speed_control = DipSwitchSpeedControl()

LED = Pin("LED", Pin.OUT)

lastSpeed = 0

LeftMotor = stepperMotor([19, 18, 17, 16])
RightMotor = stepperMotor([12, 13, 14, 15])
LSensor, FSensor, RSensor = IR_Sensor(4), IR_Sensor(5), IR_Sensor(6)

# Every time variable is accessed it will poll new sensor data
valueTuple = lambda: (LSensor.value(), FSensor.value(), RSensor.value())

# Optimized Command Scheduler
class CommandScheduler:
    def __init__(self):
        self.current_task = None

    async def run_command(self, command):
        if self.current_task and not self.current_task.done():
            self.current_task.cancel()
        self.current_task = asyncio.create_task(command())

scheduler = CommandScheduler()

async def turnRight(speed):
    await SimultaneousMotorStep.run_motors_simultaneously(RightMotor, LeftMotor, 1, 100, speed, -1, 100, speed)

async def turnLeft(speed):
    await SimultaneousMotorStep.run_motors_simultaneously(RightMotor, LeftMotor, -1, 100, speed, 1, 100, speed)

async def action(speed):
    await SimultaneousMotorStep.run_motors_simultaneously(RightMotor, LeftMotor, 1, 100, speed, 1, 100, speed)

async def simpleFigure(valueTuple):
    global lastSpeed

    # Unpack sensor data to get all values at once
    initTuple = valueTuple

    speed = speed_control.get_speed_delay()

    if lastSpeed != speed:
        for i in range(speed * 10):
            LED.toggle()
            await asyncio.sleep(0.2)
        lastSpeed = speed
        LED.off()

    if initTuple[2] == 0:
        await scheduler.run_command(lambda: turnRight(speed))
        await asyncio.sleep(0.1)
        await scheduler.run_command(lambda: action(speed))
    elif initTuple[1] == 0:
        await scheduler.run_command(lambda: action(speed))
    elif initTuple[0] == 0:
        await scheduler.run_command(lambda: turnLeft(speed))
        await asyncio.sleep(0.1)
        await scheduler.run_command(lambda: action(speed))
    else:
        await scheduler.run_command(lambda: turnLeft(speed))

async def main():
    while True:
        print("\n\n")
        await simpleFigure(valueTuple())
        print("\n\n")
        await asyncio.sleep(0.01)

        print("working")

asyncio.run(main())

