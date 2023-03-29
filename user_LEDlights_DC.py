import RPi.GPIO as GPIO
from time import sleep

def init_Alternator():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(9, GPIO.OUT)#for DC motor
    GPIO.setup(10, GPIO.OUT)#for LED


    
    
def slider_function(slider_value):
    init_Alternator()
    p = GPIO.PWM(10,100)   # Initialize PWM on pin 12 with a frequency of 50Hz
    pwmDC = GPIO.PWM(9, 100)
    p.start(0)              # Start the PWM with a duty cycle of 0
    pwmDC.start(0)
    while True:
        p.ChangeDutyCycle(slider_value)
        pwmDC.ChangeDutyCycle(slider_value)

        sleep(.02)
    sleep(.01)
    GPIO.cleanup()




