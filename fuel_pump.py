import RPi.GPIO as GPIO
from time import sleep
Enable = 26


def pump_setup():
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(Enable, GPIO.OUT)


def pump_enable():
	GPIO.output(Enable, 1)


def pump_disble():
	GPIO.output(Enable, 0)

pump_enable()
sleep(15)
