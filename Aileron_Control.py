import RPi.GPIO as GPIO
from time import sleep
import RPi.GPIO as GPIO

Aileron_max_speed = 25
def aileron_setup():
    Enable = 26 # by default is high
    Speed = 21 # PWM 0 pin
    F_R = 7 # 1 is forward and 0 is reverse(UP)
    Break = 3

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Enable, GPIO.OUT)
    GPIO.setup(F_R, GPIO.OUT)
    GPIO.setup(Speed, GPIO.OUT)
    GPIO.setup(Break, GPIO.OUT)
    GPIO.output(Enable, 1)
    GPIO.output(Speed, 1)
    GPIO.output(Break, 1)

def aileron_forward(speed):
    aileron_setup()
    GPIO.output(F_R, 1)
    GPIO.output(Enable, 1)
    GPIO.output(Speed, 1)
    GPIO.output(Break, 1)

    p = GPIO.PWM(Speed, 2000)
    p.start(0)
    p.ChangeDutyCycle(speed)

def aileron_reverse(speed):
    aileron_setup()
    GPIO.output(F_R, 0)
    GPIO.output(Enable, 1)
    GPIO.output(Speed, 1)
    GPIO.output(Break, 1)

    p = GPIO.PWM(Speed, 2000)
    p.start(0)
    p.ChangeDutyCycle(speed)

def aileron_disable():
    aileron_setup()
    GPIO.output(Enable, 0)
    GPIO.output(Break, 0)























'''
Enable = 26 #by default is high
Speed = 21 #PWM 0 pin
F_R = 7 # 1 is forward and 0 is reverse(UP)
Break = 3

Aileron_max_speed = 25


def aileron_init(F_R_val, EN, Break_val):

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)#look at GPIO

    GPIO.setup(Enable, GPIO.OUT)
    GPIO.setup(F_R, GPIO.OUT)
    GPIO.setup(Speed, GPIO.OUT)
    GPIO.setup(Break, GPIO.OUT)

    GPIO.output(Enable, EN)
    GPIO.output(Speed, 1)
    GPIO.output(Break, Break_val)
    GPIO.output(F_R, F_R_val)


def aileron_control():
    while True:
        aileron_init(0,1,1)
        p = GPIO.PWM(Speed,2000)   # Initialize PWM on pin 12 with a frequency of 50Hz
        p.start(0)
        p.ChangeDutyCycle(25)
        sleep(0.25)
        aileron_init(1,1,1)
        p.ChangeDutyCycle(25)
        sleep(.5)
        aileron_init(0,1,1)
        sleep(0.25)
GPIO.cleanup()
'''

