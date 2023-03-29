import RPi.GPIO as GPIO
from time import sleep

from tkinter import *

class MyApplication:
    def __init__(self):
        self.current_value = 0
        self.init_Alternator()
        self.init_GUI()

    def init_GUI(self):
        self.alternator_page = Tk()
        self.alternator_page.geometry('1200x800')
        self.alternator_page.title("Alternator Control Panel")
        self.alternator_page.config(bg='#092a81')

        self.w1 = Scale(self.alternator_page, from_=0, to=100, length=1000, orient=HORIZONTAL, command=self.slider_function,
                        troughcolor='#0e3999', width=67, sliderrelief='groove', highlightbackground='#0e3999',
                        sliderlength=40, font=("Tactic Sans Extra Extended", 15), showvalue=0)
        self.w1.set(self.current_value)
        self.w1.pack()

        self.value_label = Label(self.alternator_page, text=self.current_value, font=("Tactic Sans Extra Extended", 25), fg='white', bg="#092a81")
        self.value_label.pack()
        self.value_label.place(x=935, y=450)

        self.alternator_page.mainloop()

    def init_Alternator(self):

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9, GPIO.OUT)  # for DC motor
        GPIO.setup(10, GPIO.OUT)  # for LED
        self.p = GPIO.PWM(10, 100)  # Initialize PWM on pin 12 with a frequency of 50Hz
        self.pwmDC = GPIO.PWM(9, 100)
        self.p.start(0)  # Start the PWM with a duty cycle of 0
        self.pwmDC.start(0)

    def slider_function(self, slider_value):
        slider_value = int(slider_value)
        if slider_value != self.current_value:
            self.current_value = slider_value
            self.p.ChangeDutyCycle(slider_value)
            self.pwmDC.ChangeDutyCycle(slider_value)
            self.value_label.config(text=self.current_value)

    def __del__(self):
        self.p.stop()
        self.pwmDC.stop()
           def init_Alternator(self):

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9, GPIO.OUT)  # for DC motor
        GPIO.setup(10, GPIO.OUT)  # for LED
        self.p = GPIO.PWM(10, 100)  # Initialize PWM on pin 12 with a frequency of 50Hz
        self.pwmDC = GPIO.PWM(9, 100)
        self.p.start(0)  # Start the PWM with a duty cycle of 0
        self.pwmDC.start(0)

    def slider_function(self, slider_value):
        slider_value = int(slider_value)
        if slider_value != self.current_value:
            self.current_value = slider_value
            self.p.ChangeDutyCycle(slider_value)
            self.pwmDC.ChangeDutyCycle(slider_value)
            self.value_label.config(text=self.current_value)

    def __del__(self):
        self.p.stop()
        self.pwmDC.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    app = MyApplication()
