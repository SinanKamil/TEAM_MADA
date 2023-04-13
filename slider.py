from tkinter import *



def show_values(event):
    global current_value
    slider_value = w1.get()
    if slider_value != current_value:
        current_value = slider_value
    converted_value = (slider_value / 100) * 25
    converted_value = round(converted_value, 2)
    print("Converted value: ", converted_value, "Current value: ", current_value)

def set_PWM(converted_value):
    p = float(converted_value)


current_value = 0

root = Tk()


w1 = Scale(root, from_=0, to=100, length=600, orient=HORIZONTAL, command=set_PWM,
           troughcolor='#092a81', sliderrelief='sunken',
           sliderlength=40, highlightbackground='black',
           showvalue=0)
w1.set(current_value)
w1.pack()

w1.bind("<B1-Motion>", show_values)

mainloop()