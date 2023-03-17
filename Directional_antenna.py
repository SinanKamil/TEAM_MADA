import RPi.GPIO as GPIO
import time


def antenna():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT) #enable pin

    # Rotate the motor clockwise
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)

    # Turn on the motor by setting the enable pin to high
    GPIO.output(21, GPIO.HIGH)

    # Wait for 1 seconds
    time.sleep(1)

    # Pause the motor for 0.5
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)

    # Rotate the motor counterclockwise
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(3)

    # Pause the motor for 0.5
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    time.sleep(5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(4)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.2)

    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(1.5)

    # Turn off the motor by setting the enable pin to low
    GPIO.output(21, GPIO.LOW)
    
# Clean up the GPIO pins
GPIO.cleanup()


