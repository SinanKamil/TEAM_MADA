import RPi.GPIO as GPIO
from time import sleep

Enable = 24
Speed = 18 #PWM 0 pin
F_R = 16 # 1 is forward and 0 is reverse(UP)
Break = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Enable, GPIO.OUT)
GPIO.setup(F_R, GPIO.OUT)
GPIO.setup(Speed, GPIO.OUT)
GPIO.setup(Break, GPIO.OUT)

GPIO.output(Enable, 0)
GPIO.output(F_R, 1)
GPIO.output(Speed, 1)
GPIO.output(Break, 1)
p = GPIO.PWM(Speed,2000)   # Initialize PWM on pin 12 with a frequency of 50Hz
p.start(0)

#for duty in range(0,100,5):
#    p.ChangeDutyCycle(duty)
while True:
    p.ChangeDutyCycle(5)



    
    