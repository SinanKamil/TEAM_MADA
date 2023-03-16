import RPi.GPIO as GPIO
from time import sleep

Enable = 15 #by default is high 
Speed = 21 #PWM 0 pin
F_R = 7 # 1 is forward and 0 is reverse(UP)
Break = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)#look at GPIO

GPIO.setup(Enable, GPIO.OUT)
GPIO.setup(F_R, GPIO.OUT)
GPIO.setup(Speed, GPIO.OUT)
GPIO.setup(Break, GPIO.OUT)

GPIO.output(Enable, 1)
GPIO.output(Speed, 1)
GPIO.output(Break, 1)
p = GPIO.PWM(Speed,2000)   # Initialize PWM on pin 12 with a frequency of 50Hz
p.start(0)

#for duty in range(0,100,5):
#    p.ChangeDutyCycle(duty)
while True:
    GPIO.output(F_R, 1)
    p.ChangeDutyCycle(5)
    sleep(1)
    GPIO.output(F_R, 0)
    p.ChangeDutyCycle(5)
    sleep(3)
    GPIO.output(Enable, 0)


GPIO.cleanup()
    
    
