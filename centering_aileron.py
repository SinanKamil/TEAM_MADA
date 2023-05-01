import RPi.GPIO as GPIO
from time import sleep
import serial
from control_aileron import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, aileron_init, Speed, pwm_aileron, aileron_enable
from three_UARTS_pi4_get import aileron_validate_data
ser = serial.Serial("/dev/ttyS0", 115200)

def aileron_center(in_speed):
    data_aileron = aileron_validate_data(ser)
    print(data_aileron)
    aileron_enable()
    if(data_aileron > 1.6300):
        aileron_enable()
        while data_aileron > 1.6290:
            data_aileron = aileron_validate_data(ser)
            print(data_aileron)
            aileron_forward(pwm_aileron,in_speed)
        aileron_disable()
    else:
        aileron_enable()
        data_aileron = aileron_validate_data(ser)
        while data_aileron < 1.6200:
            data_aileron = aileron_validate_data(ser)
            print(data_aileron)
            aileron_reverse(pwm_aileron,in_speed)
        aileron_disable()