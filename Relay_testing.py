import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
<<<<<<< HEAD

GPIO.output(4, 1)

'''
Traceback (most recent call last):
  File "/home/pi/TEAM_MADA/GA_GUI.py", line 762, in <module>
    app = GA()
  File "/home/pi/TEAM_MADA/GA_GUI.py", line 28, in __init__
    super().__init__()
  File "/usr/lib/python3.7/tkinter/__init__.py", line 2023, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable
'''
=======


def relay(signal):
    GPIO.output(4, signal)
relay(1)
>>>>>>> c9392ba3965f6dfbefbee0f210f4ba5f68f244dc
