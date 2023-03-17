import RPi.GPIO as GPIO
from time import sleep

def DC_LED_function():

    times = 3
    for i in range(times):
        for duty in range(0,100,1):
            p.ChangeDutyCycle(duty)
            pwmDC.ChangeDutyCycle(duty)

            sleep(.02)
        sleep(.01)
        
        for duty in range(100,-1,-1):
            p.ChangeDutyCycle(duty)
            pwmDC.ChangeDutyCycle(duty)

            sleep(.02)
        sleep(.01)

        
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(9, GPIO.OUT)#for DC motor
GPIO.setup(10, GPIO.OUT)#for LED


p = GPIO.PWM(10,100)   # Initialize PWM on pin 12 with a frequency of 50Hz
pwmDC = GPIO.PWM(9, 100)
p.start(0)              # Start the PWM with a duty cycle of 0
pwmDC.start(0)

DC_LED_function()


