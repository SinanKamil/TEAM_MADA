import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from time import sleep
from TESTING import run
from Button_control_steering import forward_accelerate, disable_steering, reverse_accelerate
from steering_code import motors, MAX_SPEED
from centering_steering import center
current_value = 0


class GA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.numbers_clicked = []
        self.current_value = 0
        self.w1 = 0
        self.geometry("1920x1080")
        self.title('General Atomics')
        self.config(bg="white")
        #self.attributes("-fullscreen",True)
        ico = Image.open('images/GA.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)
        self.button_clicked = 0

# page for landing gear
        self.landing_gear_page = tk.Frame(self)
        self.landing_gear_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.landing_gear_page, "images/landing_gear_page.png")



        self.left = ImageTk.PhotoImage(Image.open("btn_images/LEFT.png"))
        self.steering = tk.Button(self.landing_gear_page, image=self.left, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.steering.bind("<ButtonPress>", lambda event: self.reverse_steering())
        self.steering.bind("<ButtonRelease>", lambda event: self.disable())
        self.steering.place(x=342, y=400)

        self.right = ImageTk.PhotoImage(Image.open("btn_images/RIGHT.png"))
        self.next_button = tk.Button(self.landing_gear_page, image=self.right, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.bind("<ButtonPress>", lambda event: self.forward_steering())
        self.next_button.bind("<ButtonRelease>", lambda event: self.disable())
        self.next_button.place(x=1250, y=400)



        self.left1 = ImageTk.PhotoImage(Image.open("btn_images/LEFT.png"))
        self.next_button = tk.Button(self.landing_gear_page, image=self.left1, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.reverse_retract,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=342, y=650)

        self.right1 = ImageTk.PhotoImage(Image.open("btn_images/RIGHT.png"))
        self.next_button = tk.Button(self.landing_gear_page, image=self.right1, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.forward_retract,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1250, y=650)



    def add_background_image(self, frame, file):
        img = Image.open(file)
        img = img.resize((1920, 1080), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        label = tk.Label(frame, image=img)
        label.image = img
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def show_page(self, page):
        self.landing_gear_page.pack_forget()
        page.pack(side="top", fill="both", expand=True)

    def show_landing_gear_page(self):
        self.show_page(self.landing_gear_page)

    def reverse_steering(self):
        print("reverse_steering")
        reverse_accelerate(-80)

    def reverse_retract(self):
        print("reverse_retract")
        
    
    def forward_steering(self):
        print("forward_steering")
        forward_accelerate(80)
        
    def disable(self):
        disable_steering()
    def forward_retract(self):
        print("forward_retract")
if __name__ == "__main__":
    app = GA()
    app.mainloop()
    
motors.setSpeeds(0, 0)
motors.forceStop()