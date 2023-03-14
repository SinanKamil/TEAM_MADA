from tkinter import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(0)

def set_duty_cycle(new_value):
    duty_cycle = float(new_value)
    pwm.ChangeDutyCycle(duty_cycle)

root = Tk()

def show_values(event):
    global current_value
    new_value = w1.get()
    if new_value != current_value:
        print(new_value)
        current_value = new_value

current_value = 0

w1 = Scale(root, from_=0, to=100, length=800, orient=HORIZONTAL, command=set_duty_cycle,
           troughcolor='green', width=50,tickinterval=100, font= ("Arial", 10),sliderrelief='sunken',
           sliderlength=40, highlightbackground='black',
           showvalue=0)
w1.set(current_value)
w1.pack()

w1.bind("<B1-Motion>", show_values)

mainloop()