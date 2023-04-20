import RPi.GPIO as GPIO
from time import sleep

Enable = 26


def pump_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Enable, GPIO.OUT)


def pump_enable():
    pump_setup()
    GPIO.output(Enable, 1)


def pump_disable():
    pump_setup()
    GPIO.output(Enable, 0)


def user_fuel_pump_control(callback):
    pump_enable()
    sleep(20)
    pump_disable()
    callback()

# pump_enable()
# sleep(5)
#pump_disable()
#user_fuel_pump_control()
#GPIO.cleanup()
