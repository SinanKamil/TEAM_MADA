import RPi.GPIO as GPIO
import time

def init_ant():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(27, GPIO.OUT) #left27
    GPIO.setup(18, GPIO.OUT) #right18
    GPIO.setup(17, GPIO.OUT) #enable pin17

def counterclockwise_ant():
    init_ant()
    # Rotate the motor clockwise
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    # Turn on the motor by setting the enable pin to high
    GPIO.output(17, GPIO.HIGH)

def clockwise_ant():
    init_ant()
    
    # Rotate the motor counterclockwise
    GPIO.output(27, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    
    # Turn on the motor by setting the enable pin to high
    GPIO.output(17, GPIO.HIGH)
    
def disable_antenna():
    # Turn off the motor by setting the enable pin to low
    GPIO.output(27, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)


