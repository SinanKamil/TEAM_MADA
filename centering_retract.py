import serial
from time import sleep
import RPi.GPIO as GPIO

import time
from steering_retract_code import motors, MAX_SPEED
from three_UARTS_pi4_get import retract_validate_data
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor2.getFault():
        raise DriverFault(1)

def retract_center():
    rev_accelerate = list(range(0, -int(MAX_SPEED), -40))

    motors.setSpeeds(0, 0)
    ser = serial.Serial("/dev/ttyS0", 115200)
    print(ser)
    data_float = retract_validate_data(ser)
    for_accelerate = list(range(0, int(MAX_SPEED), 40))
    for_constant = MAX_SPEED

    rev_constant = -MAX_SPEED
    if data_float > 0.9 or data_float < 1.8:
        if data_float > 1.75:
            for s in for_accelerate:
                motors.motor2.setSpeed(s)
                raiseIfFault()
                data_float = retract_validate_data(ser)
                print(data_float)

            while data_float > 1.75:
                motors.motor2.setSpeed(int(for_constant))
                raiseIfFault()
                data_float = retract_validate_data(ser)
                print(data_float)

        else:
            for s in rev_accelerate:
                motors.motor2.setSpeed(s)
                raiseIfFault()
                data_float = retract_validate_data(ser)
                print(data_float)

            while data_float < 1.75:
                motors.motor2.setSpeed(int(rev_constant))
                raiseIfFault()
                data_float = retract_validate_data(ser)
                print(data_float)
        motors.forceStop()
motors.forceStop()




