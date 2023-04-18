
import serial
from time import sleep
import RPi.GPIO as GPIO
from steering_retract_code import motors, MAX_SPEED, Motor
from centering_steering import center_steering
from three_UARTS_pi4_get import steering_validate_data

# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

ser = serial.Serial("/dev/ttyS0", 115200)
def user_steering_run(callback):
    center_steering()

    ser = serial.Serial("/dev/ttyS0", 115200)
    print(ser)
    data_float = steering_validate_data(ser)
    print(data_float)
    for_accelerate = list(range(0, int(MAX_SPEED), 40))
    for_constant = MAX_SPEED
    for_daccelerate = list(range(int(MAX_SPEED), 0, -40))



    for s in for_accelerate:
        motors.motor1.setSpeed(s)
        data_float = steering_validate_data(ser)
        #motors.motor1.setSpeed(int(for_constant))
        print(data_float)
    while data_float > 1.5:
        motors.motor1.setSpeed(int(for_constant))
        #raiseIfFault()
        data_float = steering_validate_data(ser)
        print(data_float)
    for s in for_daccelerate:
        motors.motor1.setSpeed(s)
        data_float = steering_validate_data(ser)
        #motors.motor1.setSpeed(int(for_constant))
        print(data_float)

    ser = serial.Serial("/dev/ttyS0", 115200)
    print(ser)
    rev_accelerate = list(range(0, -int(MAX_SPEED), -40))
    rev_daccelerate = list(range(-int(MAX_SPEED), 0, 40))

    rev_constant = -MAX_SPEED
    for s in rev_accelerate:
        motors.motor1.setSpeed(s)
        data_float = steering_validate_data(ser)
        #motors.motor1.setSpeed(int(-for_constant))
        print(data_float)
    while data_float < 1.9:
        motors.motor1.setSpeed(int(rev_constant))
        #raiseIfFault()
        data_float = steering_validate_data(ser)
        print(data_float)
    for s in rev_daccelerate:
        motors.motor1.setSpeed(s)
        data_float = steering_validate_data(ser)
        #motors.motor1.setSpeed(int(-for_constant))
        print(data_float)

    for s in for_accelerate:
        motors.motor1.setSpeed(s)
        data_float = steering_validate_data(ser)
        #motors.motor1.setSpeed(int(for_constant))
        print(data_float)
    while data_float > 1.5:
        motors.motor1.setSpeed(int(for_constant))
        #raiseIfFault()
        data_float = steering_validate_data(ser)
        print(data_float)
    for s in for_daccelerate:
        motors.motor1.setSpeed(s)
        data_float = steering_validate_data(ser)
        #motors.motor1.setSpeed(int(for_constant))
        print(data_float)

    center_steering()
    callback()
def disable_steering():
    motors.forceStop()