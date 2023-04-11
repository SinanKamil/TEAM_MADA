import RPi.GPIO as GPIO
from time import sleep
import serial
from Aileron_Control import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, aileron_init, Speed
from three_UARTS_pi4_get import aileron_validate_data
ser = serial.Serial("/dev/ttyS0", 115200)

def aileron_center():
    aileron_setup()
    p = GPIO.PWM(Speed, 2000)
    p.start(0)
    data_aileron = aileron_validate_data(ser)
    if data_aileron < 1.7650 or data_aileron > 1.7000:
        data_aileron = aileron_validate_data(ser)
        if(data_aileron > 1.7650):
            while data_aileron > 1.7650:
                data_aileron = aileron_validate_data(ser)
                aileron_forward(p)
            aileron_disable()
        else:
            data_aileron = aileron_validate_data(ser)

            while data_aileron < 1.71500:
                data_aileron = aileron_validate_data(ser)
                aileron_reverse(p)
            aileron_disable()

aileron_center()
