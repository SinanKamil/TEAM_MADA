import RPi.GPIO as GPIO
from time import sleep

Enable = 26 #by default is high
Speed = 21 #PWM 0 pin
F_R = 7 # 1 is forward and 0 is reverse(UP)
Break = 3

Aileron_max_speed = 25


def aileron_init(F_R_val):

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)#look at GPIO

    GPIO.setup(Enable, GPIO.OUT)
    GPIO.setup(F_R, GPIO.OUT)
    GPIO.setup(Speed, GPIO.OUT)
    GPIO.setup(Break, GPIO.OUT)

    GPIO.output(Enable, 1)
    GPIO.output(Speed, 1)
    GPIO.output(Break, 1)
    GPIO.output(F_R, F_R_val)


def aileron_control():
    while True:
        aileron_init(0)
        p = GPIO.PWM(Speed,2000)   # Initialize PWM on pin 12 with a frequency of 50Hz
        p.start(0)
        p.ChangeDutyCycle(25)
        sleep(0.25)
        aileron_init(1)
        p.ChangeDutyCycle(25)
        sleep(.5)
        aileron_init(0)
        sleep(0.25)
        break
    GPIO.cleanup()


