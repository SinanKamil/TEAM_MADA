import RPi.GPIO as GPIO
from time import sleep

Enable = 10 #by default is high
Speed = 9 #PWM 0 pin
F_R = 7 # 1 is forward (down) and 0 is reverse(UP)
Break = 11

Aileron_max_speed = 5


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
times = 1
def aileron_control():
    for f in range(times):
        aileron_init(0,1,1)
        p = GPIO.PWM(Speed,2000)
        p.start(0)
        p.ChangeDutyCycle(5)
        sleep(1)
        aileron_init(1,1,1)
        sleep(1)
        p.stop()
    GPIO.cleanup()

aileron_control()
GPIO.cleanup()