import RPi.GPIO as GPIO
import time

def antenna(callback):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT)#LEFT 
    GPIO.setup(27, GPIO.OUT)#RIGHT
    GPIO.setup(17, GPIO.OUT) #enable pin

    # Rotate the motor clockwise
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)

    # Turn on the motor by setting the enable pin to high
    GPIO.output(17, GPIO.HIGH)

    # Wait for 1 seconds
    time.sleep(1)

    # Pause the motor for 0.5
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.5)

    # Rotate the motor counterclockwise
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(3)

    # Pause the motor for 0.5
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    time.sleep(5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(4)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.2)

    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(1.5)

    # Turn off the motor by setting the enable pin to low
    GPIO.output(17, GPIO.LOW)
    
# Clean up the GPIO pins
    GPIO.cleanup()
    callback()
#antenna()

