import RPi.GPIO as GPIO
from time import sleep
import serial
from Aileron_Control import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, Aileron_max_speed
from three_UARTS_pi4_get import aileron_validate_data
ser = serial.Serial("/dev/ttyS0", 115200)

def aileron_center():
    while True:
        data_aileron = aileron_validate_data(ser)
        if data_aileron > 1.74:
            aileron_forward(Aileron_max_speed)
            aileron_disable()
        elif data_aileron < 1.74:
            aileron_reverse(Aileron_max_speed)
            print(aileron_validate_data(ser))
            #sleep(1)
            aileron_disable()
        else:
            aileron_disable()
            break
aileron_center()