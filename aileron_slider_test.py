import RPi.GPIO as GPIO
from time import sleep
from Aileron_Control import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, aileron_init, Speed
from tkinter import *


Enable = 26 #by default is high
Speed = 21 #PWM 0 pin
F_R = 7 # 1 is forward (down) and 0 is reverse(UP)
Break = 3


aileron_setup()

p = GPIO.PWM(Speed, 2000)
p.start(0)

def show_values(event):
    global current_value
    slider_value = w1.get()
    if slider_value != current_value:
        current_value = slider_value
    converted_value = (slider_value / 100) * 25
    converted_value = round(converted_value, 2)
    print("Converted value: ", converted_value, "Current value: ", current_value)
    
def set_PWM(converted_value):
    duty_cycle = float(converted_value)
    p.ChangeDutyCyle(duty_cycle)
    aileron_forward(p)
    sleep(1)
    aileron_reverse(p)
    sleep(1)

root = Tk()

w1 = Scale(root, from_=0, to=100, length=600, orient=HORIZONTAL, command=set_PWM,
           troughcolor='#092a81', sliderrelief='sunken',
           sliderlength=40, highlightbackground='black',
           showvalue=0)
w1.set(current_value)
w1.pack()

w1.bind("<B1-Motion>", show_values)

mainloop()


    aileron_forward(p)
    sleep(1)
    aileron_reverse(p)
    sleep(1)





