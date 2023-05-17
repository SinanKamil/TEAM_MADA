import RPi.GPIO as GPIO
from time import sleep



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)  # for DC motor
GPIO.setup(26, 1)  # for LED
   