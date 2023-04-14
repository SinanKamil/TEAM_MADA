import RPi.GPIO as GPIO
from time import sleep
import serial
from control_aileron import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, aileron_init, Speed, pwm_aileron
from three_UARTS_pi4_get import aileron_validate_data
ser = serial.Serial("/dev/ttyS0", 115200)

aileron_upper_limit = #
aileron_lower_limit = #

def limit_up_aileron():
    current_position = aileron_validate_data(ser)
    if current_position >= aileron_upper_limit:
        aileron_disable()
        return

def limit_down_aileron():
    current_position = aileron_validate_data(ser)
    if current_position <= aileron_lower_limit:
        aileron_disable()
        return



