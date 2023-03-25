
import serial
from time import sleep
import RPi.GPIO as GPIO
from steering_code import motors, MAX_SPEED, Motor
from centering_steering import center

# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num


def validate_data(serial_obj):
    while True:
        try:
            data = serial_obj.readline(4).decode('utf-8') # read 4 bytes
            data_float = float(data)
            if 0.0 <= data_float <= 2.0: # check if value is within expected range
                return data_float
        except (UnicodeDecodeError, ValueError):
            pass
def user_steering_run(callback):    
    center()

    ser = serial.Serial("/dev/ttyS0", 115200)
    print(ser)
    for_accelerate = list(range(0, int(MAX_SPEED), 40))
    for_constant = MAX_SPEED
    for_daccelerate = list(range(int(MAX_SPEED), 0, -40))



    for s in for_accelerate:
        motors.motor1.setSpeed(s)
        data_float = validate_data(ser)
        #motors.motor1.setSpeed(int(for_constant))
        print(data_float)
    while data_float > 0.9:
        motors.motor1.setSpeed(int(for_constant))
        #raiseIfFault()
        data_float = validate_data(ser)
        print(data_float)
    for s in for_daccelerate:
        motors.motor1.setSpeed(s)
        data_float = validate_data(ser)
        #motors.motor1.setSpeed(int(for_constant))
        print(data_float)

    ser = serial.Serial("/dev/ttyS0", 115200)
    print(ser)
    rev_accelerate = list(range(0, -int(MAX_SPEED), -40))
    rev_daccelerate = list(range(-int(MAX_SPEED), 0, 40))

    rev_constant = -MAX_SPEED
    for s in rev_accelerate:
        motors.motor1.setSpeed(s)
        data_float = validate_data(ser)
        #motors.motor1.setSpeed(int(-for_constant))
        print(data_float)
    while data_float < 1.4:
        motors.motor1.setSpeed(int(rev_constant))
        #raiseIfFault()
        data_float = validate_data(ser)
        print(data_float)
    for s in rev_daccelerate:
        motors.motor1.setSpeed(s)
        data_float = validate_data(ser)
        #motors.motor1.setSpeed(int(-for_constant))
        print(data_float)
    
    center()
    callback()
def disable_steering():
    motors.forceStop()






