import RPi.GPIO as GPIO
from time import sleep



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)  # for DC motor
GPIO.setup(3, 0)  # for LED
   