import serial
from time import sleep
import RPi.GPIO as GPIO

import time


def validate_data(serial_obj):
    while True:
        try:
            data = serial_obj.readline(4).decode('utf-8') # read 4 bytes
            data_float = float(data)
            if 0.0 <= data_float <= 2.0: # check if value is within expected range
                return data_float
        except (UnicodeDecodeError, ValueError):
            pass

ser = serial.Serial("/dev/ttyS0", 115200)
print(validate_data(ser))
ser.close()