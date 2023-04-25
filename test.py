import RPi.GPIO as GPIO
import time

def antenna():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(27, GPIO.OUT) #left27
        GPIO.setup(18, GPIO.OUT) #right18
        GPIO.setup(17, GPIO.OUT) #enable pin
    
        # Turn on the motor by setting the enable pin to high
        GPIO.output(17, GPIO.HIGH)
    
        # Rotate the motor clockwise
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)

        # Wait for 1 seconds
        time.sleep(1)

        # Pause the motor for 0.5
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)

        # Rotate the motor counterclockwise
        GPIO.output(27, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        
        # Turn on the motor by setting the enable pin to high
        GPIO.output(17, GPIO.LOW)
