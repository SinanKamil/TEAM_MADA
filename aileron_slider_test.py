import RPi.GPIO as GPIO
from time import sleep
from Aileron_Control import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, aileron_init, Speed


Enable = 26 #by default is high
Speed = 21 #PWM 0 pin
F_R = 7 # 1 is forward (down) and 0 is reverse(UP)
Break = 3


aileron_setup()
p = GPIO.PWM(Speed, 2000)
p.start(0)


while True:
    aileron_forward(p)
    sleep(1)
    aileron_reverse(p)
    sleep(1)





