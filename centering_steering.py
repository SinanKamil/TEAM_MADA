import serial
from time import sleep
import RPi.GPIO as GPIO

import time
from steering_retract_code import motors, MAX_SPEED
from three_UARTS_pi4_get import steering_validate_data
# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor1.getFault():
        raise DriverFault(1)
def center_steering():
    for_daccelerate = list(range(int(MAX_SPEED), 0, -40))#not being used
    rev_accelerate = list(range(0, -int(MAX_SPEED), -40))

    motors.setSpeeds(0, 0)
    ser = serial.Serial("/dev/ttyS0", 115200)
    print(ser)
    data_float = steering_validate_data(ser)
    for_accelerate = list(range(0, int(MAX_SPEED), 40))
    for_constant = MAX_SPEED

    rev_constant = -MAX_SPEED
    rev_daccelerate = list(range(-int(MAX_SPEED), 0, 40))#not being used
    if data_float < 1.68 or data_float > 1.73:
        if data_float > 0.7 and data_float < 1.72:
            for s in rev_accelerate:
                motors.motor1.setSpeed(s)
                raiseIfFault()
                data_float = steering_validate_data(ser)
                print(data_float)

            while data_float < 1.72:
                motors.motor1.setSpeed(int(rev_constant))
                raiseIfFault()
                data_float = steering_validate_data(ser)
                print(data_float)

        else:
            for s in for_accelerate:
                motors.motor1.setSpeed(s)
                raiseIfFault()
                data_float = steering_validate_data(ser)
                print(data_float)

            while data_float > 1.72 or data_float < 0.7:
                motors.motor1.setSpeed(int(for_constant))
                raiseIfFault()
                data_float = steering_validate_data(ser)
                print(data_float)
        motors.forceStop()
motors.forceStop()



