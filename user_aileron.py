import RPi.GPIO as GPIO
import serial
import time

from control_aileron import (
    aileron_forward,
    aileron_reverse,
    aileron_disable,
    aileron_setup,
    aileron_init,
    Speed,
    pwm_aileron,
    aileron_enable,
)
from three_UARTS_pi4_get import aileron_validate_data
from centering_aileron import aileron_center

ser = serial.Serial("/dev/ttyS0", 115200)
up_limit = 1.728
down_limit = 1.57

def aileron_user(in_speed,callback):
    aileron_center(in_speed)
    times = 3
    for i in range(times):
        try:
            data_aileron = aileron_validate_data(ser)
            if up_limit > data_aileron > down_limit:
                while up_limit > data_aileron:
                    data_aileron = aileron_validate_data(ser)
                    aileron_reverse(pwm_aileron, in_speed)
                aileron_disable()

                while down_limit < data_aileron:
                    data_aileron = aileron_validate_data(ser)
                    aileron_forward(pwm_aileron, in_speed)
                aileron_disable()
                aileron_center(in_speed)
            else:
                aileron_disable()
        except serial.SerialException as e:
            print(f"SerialException occurred: {e}")
            aileron_disable()
        except Exception as e:
            print(f"Error occurred: {e}")
            aileron_disable()
    callback()
