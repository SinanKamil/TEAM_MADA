import RPi.GPIO as GPIO
from time import sleep

def DC_LED_function():
    times = 5
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
    GPIO.cleanup()





