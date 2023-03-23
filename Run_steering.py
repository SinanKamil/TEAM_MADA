import time
from steering_code import motors, MAX_SPEED

# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor1.getFault():
        raise DriverFault(1)

# Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 200 + list(range(MAX_SPEED, 0, -1)) + [0]
print(test_forward_speeds)
test_reverse_speeds = list(range(0, (-MAX_SPEED-1), -1)) + \
  [-MAX_SPEED] * 200 + list(range(-MAX_SPEED, 0, 1)) + [0]
print(test_reverse_speeds)
try:
    motors.setSpeeds(0, 0)

    print("Motor 1 forward")
    for s in test_forward_speeds:
        motors.motor1.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)



    print("Motor 2 forward")
    for s in test_forward_speeds:
        motors.motor2.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)


    print("Motor 2 reverse")
    for s in test_reverse_speeds:
        motors.motor2.setSpeed(s)
        raiseIfFault()
        time.sleep(0.002)

except DriverFault as e:
    print("Driver %s fault!" % e.driver_num)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
    motors.forceStop()