import RPi.GPIO as GPIO
from time import sleep
from Run_aileron import aileron_init
Aileron_max_speed = 5
Enable = 26 # by default is high
Speed = 21 # PWM 0 pin
F_R = 7 # 1 is forward and 0 is reverse(UP)
Break = 3


def aileron_forward():
    aileron_init(0,1,1)
    p = GPIO.PWM(Speed,2000)   # Initialize PWM on pin 12 with a frequency of 50Hz
    p.ChangeDutyCycle(10)

def aileron_reverse():
    aileron_init(1,1,1)
    p = GPIO.PWM(Speed,2000)   # Initialize PWM on pin 12 with a frequency of 50Hz
    p.ChangeDutyCycle(10)

def aileron_disable():
    GPIO.output(26, 0)
    GPIO.output(3, 0)


while True:
    aileron_forward()
    sleep(0.5)
    break

















