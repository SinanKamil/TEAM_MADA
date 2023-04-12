import serial
from time import sleep
import RPi.GPIO as GPIO

import time
from steering_retract_code import motors, MAX_SPEED


def forward_accelerate(val):
    for_accelerate = list(range(0, int(MAX_SPEED), val))
    for s in for_accelerate:
        motors.motor2.setSpeed(s)

def reverse_accelerate(val):
    for_accelerate = list(range(0, -int(MAX_SPEED), val))
    for s in for_accelerate:
        motors.motor2.setSpeed(s)


def disable_retract():
    motors.forceStop()
