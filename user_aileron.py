import RPi.GPIO as GPIO
from time import sleep
import serial
from control_aileron import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, aileron_init, Speed, pwm_aileron, aileron_enable
from three_UARTS_pi4_get import aileron_validate_data
from centering_aileron import aileron_center
ser = serial.Serial("/dev/ttyS0", 115200)

up_limit = 1.8000
down_limit = 1.5200

def aileron_user(callback):
    times = 3
    for i in range(times):
        data_aileron = aileron_validate_data(ser)
        if 1.8000 > data_aileron > 1.5200:
            while 1.8000 > data_aileron:
                data_aileron = aileron_validate_data(ser)
                aileron_reverse(pwm_aileron,5)
            aileron_disable()

            while 1.5200 < data_aileron:
                data_aileron = aileron_validate_data(ser)
                aileron_forward(pwm_aileron,5)
            aileron_center()
        else:
            aileron_disable()
    callback()

