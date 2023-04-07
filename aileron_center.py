import RPi.GPIO as GPIO
from time import sleep
import serial
from Aileron_Control import aileron_init, aileron_control, Aileron_max_speed
from three_UARTS_pi4_get import aileron_validate_data

aileron_forward_speeds = list(range(0, Aileron_max_speed, 1))
print(aileron_forward_speeds)




aileron_control()