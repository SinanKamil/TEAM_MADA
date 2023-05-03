import serial
from time import sleep
import RPi.GPIO as GPIO
from steering_retract_code import motors, MAX_SPEED, Motor
from centering_retract import retract_center
from three_UARTS_pi4_get import retract_validate_data
from user_steering import user_steering_run
from centering_steering import center_steering
# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def checkforError():
    STOP_PIN = 8
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(STOP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    if GPIO.input(STOP_PIN) == GPIO.HIGH:
        print("Terminating program...")
        motors.forceStop()
        exit()
        
def user_retract_run(feedback):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        center_steering()
        retract_center()
        
        ser = serial.Serial("/dev/ttyS0", 115200)
        print(ser)
        data_float = retract_validate_data(ser)
        print(data_float)
        for_accelerate = list(range(0, int(MAX_SPEED), 80))
        for_constant = MAX_SPEED
        for_daccelerate = list(range(int(MAX_SPEED), 0, -80))

        for s in for_accelerate:
            checkforError()
            motors.motor2.setSpeed(s)
            data_float = retract_validate_data(ser)
            print(data_float)
        while data_float > 0.93:
            checkforError()
            motors.motor2.setSpeed(int(for_constant))
            data_float = retract_validate_data(ser)
            print(data_float)
        for s in for_daccelerate:
            checkforError()
            motors.motor2.setSpeed(s)
            data_float = retract_validate_data(ser)
            print(data_float)
        retract_center()
        user_steering_run(feedback)


    except DriverFault as e:
        # Handle driver fault exception
        print(f"Driver {e.driver_num} fault detected. Stopping...")
        disable_retract()

    except Exception as e:
        # Handle any other exceptions
        print(f"Error occurred: {e}. Stopping...")
        disable_retract()
def disable_retract():
    motors.forceStop()


