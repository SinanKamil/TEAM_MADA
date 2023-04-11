import RPi.GPIO as GPIO
from time import sleep

Enable = 26 #by default is high
Speed = 21 #PWM 0 pin
F_R = 7 # 1 is forward and 0 is reverse(UP)
Break = 3

Aileron_max_speed = 5


GPIO.setmode(GPIO.BCM)#look at GPIO
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.output(21, 1)


p = GPIO.PWM(Speed,2000)  
p.start(0)
while True:
    GPIO.output(26, 1)
    GPIO.output(3, 1)
    GPIO.output(7, 0)
    p.start(0)
    p.ChangeDutyCycle(10)
    
    sleep(1)
    GPIO.output(26, 1)
    GPIO.output(3, 1)
    GPIO.output(7, 1)
    sleep(1)
GPIO.cleanup()


