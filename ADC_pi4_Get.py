import serial
from time import sleep
import RPi.GPIO as GPIO

import time
from steering_code import motors, MAX_SPEED

# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor1.getFault():
        raise DriverFault(1)

def validate_data(serial_obj):
    while True:
        try:
            data = serial_obj.readline(4).decode('utf-8') # read 4 bytes
            data_float = float(data)
            if 0.0 <= data_float <= 2.0: # check if value is within expected range
                return data_float
        except (UnicodeDecodeError, ValueError):
            pass

# Set up sequences of motor speeds.
for_accelerate = list(range(0, int(MAX_SPEED), 40))
for_constant = MAX_SPEED
for_daccelerate = list(range(int(MAX_SPEED), 0, -40))

rev_accelerate = list(range(0, -int(MAX_SPEED), -40))
rev_constant = -MAX_SPEED
rev_daccelerate = list(range(-int(MAX_SPEED), 0, 40))

ser = serial.Serial("/dev/ttyS0", 115200)
print(ser)

motors.setSpeeds(0, 0)

for s in for_accelerate:
    motors.motor1.setSpeed(s)
    raiseIfFault()
    data_float = validate_data(ser)
    print(data_float)

while 0.5 <= data_float <= 1.5:
    motors.motor1.setSpeed(int(for_constant))
    raiseIfFault()
    data_float = validate_data(ser)
    print(data_float)

for s in rev_accelerate:
    motors.motor1.setSpeed(s)
    raiseIfFault()
    data_float = validate_data(ser)
    print(data_float)

while 0.5 <= data_float <= 1.5:
    motors.motor1.setSpeed(int(rev_constant))
    raiseIfFault()
    data_float = validate_data(ser)
    print(data_float)

motors.forceStop()
ser.close()