import RPi.GPIO as GPIO
import time

left = 18
right = 17
    
def antenna_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(left, GPIO.OUT) #left27
    GPIO.setup(right, GPIO.OUT) #right18
    
def Counter_clock():
    antenna_init()
    # Rotate the motor clockwise
    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.LOW)

def Clockwise():
    antenna_init()
    # Rotate the motor counterclockwise
    GPIO.output(left, GPIO.LOW)
    GPIO.output(right, GPIO.HIGH)
    
def pause():
    antenna_init()
    # Pause the motor
    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)

def disable_ant():
    antenna_init()
    GPIO.output(left, GPIO.LOW)
    GPIO.output(right, GPIO.LOW)

def run_ant(callback): 
    
    Clockwise()
    time.sleep(1)

    # Pause the motor for 0.5
    pause()
    time.sleep(0.5)

    # Rotate the motor counterclockwise
    Counter_clock()
    time.sleep(2)

    # Pause the motor for 0.5
    pause()
    time.sleep(0.5)

    Counter_clock()
    time.sleep(5)

    pause()
    time.sleep(0.5)

    Counter_clock()
    time.sleep(0.5)

    pause()
    time.sleep(0.5)

    Clockwise()
    time.sleep(4)

    pause()
    time.sleep(0.5)

    Counter_clock()
    time.sleep(0.5)

    pause()
    time.sleep(0.5)

    Counter_clock()
    time.sleep(0.5)

    pause()
    time.sleep(0.5)

    Counter_clock()
    time.sleep(0.5)

    pause()
    time.sleep(0.2)

    Clockwise()
    time.sleep(1.5)

    # Turn off the motor by setting the enable pin to low
    disable_ant()
    callback()


