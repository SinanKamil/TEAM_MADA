import RPi.GPIO as GPIO
from time import sleep

Enable = 26 #by default is high
Speed = 21 #PWM 0 pin
F_R = 7 # 1 is forward (down) and 0 is reverse(UP)
Break = 3



def aileron_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)#look at GPIO

    GPIO.setup(Enable, GPIO.OUT)
    GPIO.setup(F_R, GPIO.OUT)
    GPIO.setup(Speed, GPIO.OUT)
    GPIO.setup(Break, GPIO.OUT)


def aileron_init(F_R_val, EN, Break_val):
    GPIO.output(Enable, EN)
    GPIO.output(Speed, 1)
    GPIO.output(Break, Break_val)
    GPIO.output(F_R, F_R_val)


def aileron_forward(p):
    try:
        aileron_init(0, 1, 1)
        p.ChangeDutyCycle(10)

    except Exception as e:
        print(f"Error moving aileron forward: {e}")
        GPIO.cleanup()
        exit()

def aileron_reverse(p):
    try:
        aileron_init(1,1,1)
        p.ChangeDutyCycle(10)

    except Exception as e:
        print(f"Error moving aileron reverse: {e}")
        GPIO.cleanup()
        exit()

def aileron_disable():
    try:
        GPIO.output(Enable, 0)
        GPIO.output(Break, 0)

    except Exception as e:
        print(f"Error disabling aileron: {e}")
        GPIO.cleanup()
        p.stop()
        exit()

def cleanup():
    try:
        GPIO.cleanup()
        p.stop()
        print("GPIO pins cleaned up successfully.")

    except Exception as e:
        print(f"Error cleaning up GPIO pins: {e}")
        exit()


if __name__ == '__main__':
    aileron_setup()
    p = GPIO.PWM(Speed, 2000)
    p.start(0)
    while True:
        try:
            aileron_reverse(p)
            sleep(0.5)
            aileron_disable()
            sleep(0.5)
            aileron_forward(p)
            sleep(.5)
            aileron_disable()
            sleep(0.5)

        except KeyboardInterrupt:
            print("Exiting script due to keyboard interrupt.")
            break

    cleanup()
    aileron_disable()