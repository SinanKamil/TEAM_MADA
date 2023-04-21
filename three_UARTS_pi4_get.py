import serial
import RPi.GPIO as GPIO
import smbus
from time import sleep
ser = serial.Serial("/dev/ttyS0", 115200)
def retract_validate_data(serial_obj):
        try:
            data = serial_obj.readline(16).decode('utf-8')
            data_str = str(data)
            split_float = data_str.split(" ")
            data_float_retract = float(split_float[1])
            if 0 <= data_float_retract <= 2.00:
                data_float_retract = "{:.2f}".format(data_float_retract)
            return float(data_float_retract)
        except ValueError:
            pass
def steering_validate_data(serial_obj):
        try:
            data = serial_obj.readline(16).decode('utf-8')
            data_str = str(data)
            split_float = data_str.split(" ")
            data_float_steering = float(split_float[0])
            if 0 <= data_float_steering <= 2.00:
                data_float_steering = "{:.2f}".format(data_float_steering)
            return float(data_float_steering)
        except ValueError:
            pass
def aileron_validate_data(serial_obj):
    try:
        data = serial_obj.readline(16).decode('utf-8')
        data_str = str(data)
        split_float = data_str.split(" ")
        data_float_aileron = float(split_float[2])
        if 0.0000 <= data_float_aileron <= 2.0000:
            data_float_aileron = "{:.4f}".format(data_float_aileron)
        return float(data_float_aileron)
    except ValueError:
        pass
ser = serial.Serial("/dev/ttyS0", 115200)


'''
while True:
    steering = steering_validate_data(ser)
    retract = retract_validate_data(ser)
    aileron = aileron_validate_data(ser)
    print("Aileron: ", aileron, "Steering: ", steering, "Retract: ", retract)
    sleep(0.1)
ser.close()
'''