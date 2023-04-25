import RPi.GPIO as GPIO
import time

def antenna():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    left = 27
    right = 18
    enable = 17

    GPIO.setup(left, GPIO.OUT) #left27
    GPIO.setup(right, GPIO.OUT) #right18
    GPIO.setup(enable, GPIO.OUT) #enable pin

    # Turn on the motor by setting the enable pin to high
    GPIO.output(enable, GPIO.HIGH)

    # Rotate the motor clockwise
    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.LOW)

    # Wait for 1 seconds
    time.sleep(1)

    # Pause the motor for 0.5
    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(0.5)

    # Rotate the motor counterclockwise
    GPIO.output(left, GPIO.LOW)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(3)

    # Pause the motor for 0.5
    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.LOW)
    time.sleep(5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(left, GPIO.LOW)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(4)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(left, GPIO.HIGH)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(0.2)

    GPIO.output(left, GPIO.LOW)
    GPIO.output(right, GPIO.HIGH)
    time.sleep(1.5)

    # Turn off the motor by setting the enable pin to low
    GPIO.output(enable, GPIO.LOW)
    

# Clean up the GPIO pins


