import RPi.GPIO as GPIO
import time

def init_ant():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(18, GPIO.OUT) #left27
    GPIO.setup(17, GPIO.OUT) #right18

def counterclockwise_ant():
    init_ant()
    # Rotate the motor clockwise
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)

def clockwise_ant():
    init_ant()
    
    # Rotate the motor counterclockwise
    GPIO.output(18, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
        
def disable_antenna():
    # Turn off the motor by setting the enable pin to low
    GPIO.output(18, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)


