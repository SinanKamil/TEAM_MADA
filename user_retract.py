import serial
from time import sleep
import RPi.GPIO as GPIO
from steering_retract_code import motors, MAX_SPEED, Motor
from centering_retract import retract_center
from three_UARTS_pi4_get import retract_validate_data

# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def user_retract_run(callback):
    try:
        retract_center()

        ser = serial.Serial("/dev/ttyS0", 115200)
        print(ser)
        data_float = retract_validate_data(ser)
        print(data_float)
        rev_accelerate = list(range(0, -int(MAX_SPEED), -40))
        rev_daccelerate = list(range(-int(MAX_SPEED), 0, 40))
        rev_constant = -MAX_SPEED

        for s in rev_accelerate:
            motors.motor2.setSpeed(s)
            data_float = retract_validate_data(ser)
            print(data_float)
        while data_float > 1.0:
            motors.motor2.setSpeed(int(rev_constant))
            data_float = retract_validate_data(ser)
            print(data_float)
        for s in rev_daccelerate:
            motors.motor2.setSpeed(s)
            data_float = retract_validate_data(ser)
            print(data_float)

        retract_center()
        callback()

    except DriverFault as e:
        # Handle driver fault exception
        print(f"Driver {e.driver_num} fault detected. Stopping...")
        disable_retract()

    except Exception as e:
        # Handle any other exceptions
        print(f"Error occurred: {e}. Stopping...")
        disable_retract()

def disable_retract():
    motors.forceStop()
