import RPi.GPIO as GPIO
import time

def init_ant():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(16, GPIO.OUT) #left
    GPIO.setup(20, GPIO.OUT) #right
    GPIO.setup(21, GPIO.OUT) #enable pin


def right_antenna():
    init_ant()
    # Rotate the motor clockwise
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    # Turn on the motor by setting the enable pin to high
    GPIO.output(21, GPIO.HIGH)

def left_antenna():
    init_ant()
    
    # Rotate the motor counterclockwise
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    
    # Turn on the motor by setting the enable pin to high
    GPIO.output(21, GPIO.HIGH)
    
def disable_antenna():
    # Turn off the motor by setting the enable pin to low
    GPIO.output(21, GPIO.LOW)
    # Clean up the GPIO pins
    GPIO.cleanup()


