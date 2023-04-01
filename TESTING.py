import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import time
import threading

aileron_speed_value = 0

class GA(tk.Tk):
    def __init__(self):
        super().__init__()

        self.Fuel_pump_en = False
        self.aileron_speed_value = 0
        self.current_value = 0
        self.geometry("1920x1080")
        self.title('General Atomics')
        self.config(bg="white")
        self.attributes("-fullscreen",True)

        # Load images
        self.images = {}
        self.preload_images()

        # Create instances of each page class with hidden attribute set to True
        self.page3 = tk.Frame(self)
        self.fuel_pump_page = tk.Frame(self)
        self.alternator_page = tk.Frame(self)
        self.landing_gear_page = tk.Frame(self)
        self.antenna_page = tk.Frame(self)


        self.page3.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page3, "images/admin_page.png")

        self.exit_btn = self.images["btn_images/exit_btn.png"]
        self.next_button = tk.Button(self.page3, image=self.exit_btn, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.exit,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1700, y=50)

        # page for fuel pump
        self.fuel_pump_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.fuel_pump_page, "images/fuel_pump_page.png")

        self.next_button_img18 = self.images["btn_images/fuel_pump.png"]
        self.next_button = tk.Button(self.page3, image=self.next_button_img18, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.show_fuel_pump_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=342, y=450)

        # Create the switch button for fuel pump
        self.switch_button_fuel_on = self.images["btn_images/Fuel_pump_on.png"]
        self.switch_button_fuel_off = self.images["btn_images/Fuel_pump_off.png"]
        self.switch_button_fuel = tk.Button(self.fuel_pump_page, image=self.switch_button_fuel_off,
                                            command=self.fuelpump_on_off,
                                            highlightthickness=0,
                                            activebackground='#092a81', background='#092a81', borderwidth=0,
                                            relief="flat", bd=0)
        self.switch_button_fuel.place(x=800, y=500)

        self.next_button_img19 = self.images["images/adminmenu_btn.png"]
        self.next_button = tk.Button(self.fuel_pump_page, image=self.next_button_img19, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)

        # page for alternator
        self.alternator_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.alternator_page, "images/alternator_page.png")

        self.alternator_img_btn = self.images["btn_images/alternator.png"]
        self.alternator_btn = tk.Button(self.page3, image=self.alternator_img_btn, highlightthickness=0,
                                        activebackground='#092a81', background='#092a81',
                                        command=self.show_alternator_page,
                                        borderwidth=0, relief="flat", bd=0)
        self.alternator_btn.place(x=973, y=650)

        self.w1 = Scale(self.alternator_page, from_=0, to=100, length=1000, orient=HORIZONTAL,
                        # command=self.slider_function,
                        troughcolor='#0e3999', width=67, sliderrelief='groove', highlightbackground='#0e3999',
                        sliderlength=40, font=("Tactic Sans Extra Extended", 15), showvalue=0)
        self.w1.set(self.current_value)
        self.w1.pack()
        self.w1.place(x=450, y=503)

        self.value_label = Label(self.alternator_page, text=self.current_value, font=("Tactic Sans Extra Extended", 25),
                                 fg='white', bg="#092a81")
        self.value_label.pack()
        self.value_label.place(x=935, y=450)

        self.back = self.images["images/adminmenu_btn.png"]
        self.next_button = tk.Button(self.alternator_page, image=self.back, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)
        # page for landing gear
        self.landing_gear_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.landing_gear_page, "images/landing_gear_page.png")

        self.landing_gear_btn = self.images["btn_images/landing_gear.png"]
        self.landing_gear_btn_fun = tk.Button(self.page3, image=self.landing_gear_btn, highlightthickness=0,
                                              activebackground='#092a81', background='#092a81',
                                              command=self.show_landing_gear_page,
                                              borderwidth=0, relief="flat", bd=0)
        self.landing_gear_btn_fun.place(x=550, y=650)

        self.back1 = self.images["images/adminmenu_btn.png"]
        self.next_button = tk.Button(self.landing_gear_page, image=self.back1, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=234, y=884)

        self.left = self.images["btn_images/steer_left.png"]
        self.left_steering = tk.Button(self.landing_gear_page, image=self.left, highlightthickness=0,
                                       activebackground='#092a81', background='#092a81',
                                       borderwidth=0, relief="flat", bd=0)
        self.left_steering.bind("<ButtonPress>", lambda event: self.reverse_steering())
        self.left_steering.bind("<ButtonRelease>", lambda event: self.disable_steering())
        self.left_steering.place(x=400, y=500)

        self.right = self.images["btn_images/steer_right.png"]
        self.right_steering = tk.Button(self.landing_gear_page, image=self.right, highlightthickness=0,
                                        activebackground='#092a81', background='#092a81',
                                        borderwidth=0, relief="flat", bd=0)
        self.right_steering.bind("<ButtonPress>", lambda event: self.forward_steering())
        self.right_steering.bind("<ButtonRelease>", lambda event: self.disable_steering())
        self.right_steering.place(x=1192, y=500)
        # center
        self.center = self.images["btn_images/center.png"]
        self.center_landing = tk.Button(self.landing_gear_page, image=self.center, highlightthickness=0,
                                        command=self.center_landing_gear,
                                        activebackground='#092a81', background='#092a81',
                                        borderwidth=0, relief="flat", bd=0)
        self.center_landing.place(x=800, y=500)

        self.retract_down = self.images["btn_images/retract_down.png"]
        self.next_button = tk.Button(self.landing_gear_page, image=self.retract_down, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.reverse_retract,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=800, y=725)

        self.retract_up = self.images["btn_images/retract_up.png"]
        self.next_button = tk.Button(self.landing_gear_page, image=self.retract_up, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.forward_retract,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=800, y=275)
        self.show_page(self.page3)

    def add_background_image(self, frame, file):
        with Image.open(file) as img:
            img = ImageTk.PhotoImage(img)
            label = tk.Label(frame, image=img)
            label.image = img
            label.place(x=0, y=0, relwidth=1, relheight=1)

    def show_page(self, page):
        self.page3.pack_forget()
        self.fuel_pump_page.pack_forget()
        self.landing_gear_page.pack_forget()
        self.alternator_page.pack_forget()
        page.pack(side="top", fill="both", expand=True)

    def show_fuel_pump_page(self):
        self.show_page(self.fuel_pump_page)



    def show_alternator_page(self):
        self.show_page(self.alternator_page)

    def show_landing_gear_page(self):
        self.show_page(self.landing_gear_page)



    def show_page3(self):
        self.show_page(self.page3)


    def fuel_toggle_switch(self):
        print("Fuel Pump ON")

    def dir_toggle_switch(self):
        # Disable the button
        print("Directional Antenna ON")
        self.switch_button1.config(state=tk.DISABLED)
        self.update()

        def callback_directional():  # this to enable button
            self.switch_button1.config(state=tk.NORMAL)

        antenna_thread = threading.Thread(target=antenna, args=(callback_directional,))
        antenna_thread.start()

    def aileron_toggle_switch(self):
        print("Aileron ON")

    def landing_gear_toggle_switch(self):
        print("Landing Gear ON")
        self.switch_button4.config(state=tk.DISABLED)
        self.update()

        def callback_landing_gear():  # this to enable button
            self.switch_button4.config(state=tk.NORMAL)

        steering_thread = threading.Thread(target=user_steering_run, args=(callback_landing_gear,))
        steering_thread.start()

    def Alternator_toggle_switch(self):
        print("Alternator ON")
        self.switch_button5.config(state=tk.DISABLED)
        self.update()

        def callback_alternator():  # this to enable button
            self.switch_button5.config(state=tk.NORMAL)

        # Create a new thread to run the DC LED function
        led_thread = threading.Thread(target=self.DC_LED_function, args=(callback_alternator,))
        led_thread.start()

    def aileron_show_values(self, event):
        new_value = self.aileron_speed.get()
        if new_value != self.aileron_speed_value:
            self.aileron_speed_value = new_value
            self.aileron_value_label.config(text=self.aileron_speed_value)
            print(self.aileron_speed_value)

    def center_landing_gear(self):
        center()
        print("Center")

    def forward_steering(self):
        print("forward_steering")

    def reverse_steering(self):
        print("reverse_steering")
        reverse_accelerate(-80)

    def forward_steering(self):
        print("forward_steering")
        forward_accelerate(80)

    def disable_steering(self):
        disable_steering()

    def forward_retract(self):
        print("forward_retract")

    def reverse_retract(self):
        print("forward_retract")

    def exit(self):
        res = mb.askquestion('EXIT APPLICATION',
                             'Would you like to terminate the program and exit the application?')
        if res == 'yes':
            self.destroy()

    def up_aileron(self):
        print("UP_Aileron")

    def down_aileron(self):
        print("DOWM_Aileron")

    def left_antenna(self):
        left_antenna()

    def right_antenna(self):
        right_antenna()

    def disable_dir_antenna(self):
        disable_antenna()

    def center_aileron(self):
        print("Center_Aileron")

    # Define the toggle switch function
    def fuelpump_on_off(self):
        if not self.Fuel_pump_en:
            self.Fuel_pump_en = True
            self.switch_button_fuel.config(image=self.switch_button_fuel_on)
        else:
            self.Fuel_pump_en = False
            self.switch_button_fuel.config(image=self.switch_button_fuel_off)

    def preload_images(self):
        # Create a dictionary of all image file paths
        self.images = {}
        image_paths = ["images/Enter_btn.png",
                       "images/homemenu_btn.png",
                       "btn_images/exit_btn.png",
                       "btn_images/fuel_pump.png",
                       "btn_images/Fuel_pump_on.png",
                       "btn_images/Fuel_pump_off.png",
                       "images/adminmenu_btn.png",
                       "btn_images/alternator.png",
                       "images/adminmenu_btn.png",
                       "btn_images/landing_gear.png",
                       "btn_images/steer_left.png",
                       "btn_images/steer_right.png",
                       "btn_images/center.png",
                       "btn_images/retract_down.png",
                       "btn_images/retract_up.png",
                       "btn_images/aileron.png",
                       "btn_images/center.png",
                       "btn_images/aileron_down.png",
                       "btn_images/aileron_up.png",
                       "images/adminmenu_btn.png",
                       "btn_images/directional_antenna.png",
                       "btn_images/antenna_left.png",
                       "btn_images/antenna_right.png",
                       "images/adminmenu_btn.png"
                       ]

        # Load each image and store it as an attribute of the class
        for path in image_paths:
            img = Image.open(path)
            self.images[path] = ImageTk.PhotoImage(img)


if __name__ == "__main__":
    app = GA()
    app.mainloop()
