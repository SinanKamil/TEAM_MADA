import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)


GPIO.output(4, 1)

def relay(signal):
    GPIO.output(4, signal)
relay(1)

