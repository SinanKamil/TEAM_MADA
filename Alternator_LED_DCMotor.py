import RPi.GPIO as GPIO
from time import sleep

def function():
    times = 3
    for i in range(times):
        for duty in range(0,100,1):
            p.ChangeDutyCycle(duty)
            sleep(.02)
        sleep(.01)
        
        for duty in range(100,-1,-1):
            p.ChangeDutyCycle(duty)
            sleep(.02)
        sleep(.01)
        
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)


p = GPIO.PWM(21,100)   # Initialize PWM on pin 12 with a frequency of 50Hz
p.start(0)              # Start the PWM with a duty cycle of 0




