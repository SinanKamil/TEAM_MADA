from time import sleep
import RPi.GPIO as GPIO

def init_Alternator():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)  # for DC motor
    GPIO.setup(21, GPIO.OUT)  # for LED

def DC_LED_function(callback):
    init_Alternator()
    p = GPIO.PWM(21, 100)  # Initialize PWM on pin 12 with a frequency of 50Hz
    pwmDC = GPIO.PWM(20, 100)
    p.start(0)  # Start the PWM with a duty cycle of 0
    pwmDC.start(0)
    for duty in range(0,100,1):
        pwmDC.ChangeDutyCycle(100)
        sleep(0.25)
        p.ChangeDutyCycle(duty)
            #sleep(.02)
    sleep(.01)
    for duty in range(100,-1,-1):
        p.ChangeDutyCycle(duty)
        sleep(0.01)
        pwmDC.ChangeDutyCycle(duty)
           # sleep(.02)
    sleep(.01)
    callback()
    
