import RPi.GPIO as GPIO
from time import sleep
import RPi.GPIO as GPIO

Aileron_max_speed = 5
Enable = 26 # by default is high
Speed = 21 # PWM 0 pin
F_R = 7 # 1 is forward and 0 is reverse(UP)
Break = 3

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

def aileron_forward():
    aileron_init(0,1,1)
    p = GPIO.PWM(Speed,2000)   # Initialize PWM on pin 12 with a frequency of 50Hz
    p.start(0)
    p.ChangeDutyCycle(10)

def aileron_reverse():
    aileron_init(1,1,1)
    p = GPIO.PWM(Speed,2000)   # Initialize PWM on pin 12 with a frequency of 50Hz
    p.start(0)
    p.ChangeDutyCycle(10)

def aileron_disable():
    GPIO.output(26, 0)
    GPIO.output(3, 0)


while True:
    aileron_reverse()
    sleep(.5)
    aileron_disable()
    sleep(.5)
    aileron_forward()
    sleep(.5)
    aileron_disable()


















