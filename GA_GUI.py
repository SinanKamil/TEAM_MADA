import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from time import sleep
from TESTING import run
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(0)

current_value = 0
#new code
class GA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.numbers_clicked = []
        self.current_value = 0
        self.w1 = 0
        self.geometry("1920x1080")
        self.title('General Atomics')
        self.config(bg="white")
        self.attributes("-fullscreen",True)
        ico = Image.open('images/GA.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

#page 1 here:
        # Create the first page
        self.page1 = tk.Frame(self)
        self.page1.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page1, "images/user_page.png")

        # Create the button to go to page 2
        self.next_button_img = ImageTk.PhotoImage(Image.open("images/adminlogin_btn.png"))
        self.next_button = tk.Button(self.page1, image=self.next_button_img, activebackground ='white', background ='white', highlightthickness = 0, command=self.show_page2, bd=0)
        self.next_button.place(x=1432, y=882)

        # Create the button to go to slideshow
        self.next_button_img1 = ImageTk.PhotoImage(Image.open("images/slideshow_btn.png"))
        self.next_button = tk.Button(self.page1, image=self.next_button_img1, activebackground ='white', background ='white', command=self.slideshow, highlightthickness = 0, highlightbackground = '#ffffff', borderwidth=None, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)

        # Create the switch button for fuel pump
        self.switch_button_img_on = ImageTk.PhotoImage(Image.open("btn_images/fuel_pump.png"))
        self.switch_button = tk.Button(self.page1, image=self.switch_button_img_on, command=self.fuel_toggle_switch, highlightthickness=0,
                                     activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                     relief="flat", bd=0)
        self.switch_button.place(x=342, y=450)
        #This is for the directional antenna
        self.switch_button_img_on1 = ImageTk.PhotoImage(Image.open("btn_images/directional_antenna.png"))
        self.switch_button1 = tk.Button(self.page1, image=self.switch_button_img_on1, command=self.dir_toggle_switch, highlightthickness=0,
                                     activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                     relief="flat", bd=0)
        self.switch_button1.place(x=765, y=450)
        # This is for the aileron smart servo
        self.switch_button_img_on2 = ImageTk.PhotoImage(Image.open("btn_images/aileron.png"))
        self.switch_button2 = tk.Button(self.page1, image=self.switch_button_img_on2, command=self.aileron_toggle_switch,
                                        highlightthickness=0,
                                        activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button2.place(x=1188, y=450)

        # This is for the Steering and retract servo
        self.switch_button_img_on4 = ImageTk.PhotoImage(Image.open("btn_images/landing_gear.png"))
        self.switch_button4 = tk.Button(self.page1, image=self.switch_button_img_on4,
                                        command=self.landing_gear_toggle_switch,
                                        highlightthickness=0,
                                        activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button4.place(x=550, y=650)


        # This is for the alternator
        self.switch_button_img_on5 = ImageTk.PhotoImage(Image.open("btn_images/alternator.png"))
        self.switch_button5 = tk.Button(self.page1, image=self.switch_button_img_on5,
                                        command=self.Alternator_toggle_switch,
                                        highlightthickness=0,
                                        activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button5.place(x=973, y=650)
# page 2 here:
        # Create the second page
        self.page2 = tk.Frame(self)
        self.page2.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page2, "images/admin_access.png")

        # Create the button to go back to page 1
        self.next_button_img2 = ImageTk.PhotoImage(Image.open("images/homemenu_btn.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img2, highlightthickness = 0, activebackground ='white', background ='white', command=self.show_page1, borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)

        #create a text box
        self.password_entry = tk.Entry(self.page2, font=('Rubik Medium', 38), background= "#092a81",fg="white", width=3,show='*', bd=0, borderwidth=0)
        self.password_entry.place(x=1010, y=220)


        #create the number buttons
        # one
        self.next_button_img3 = ImageTk.PhotoImage(Image.open("keypad_num_images/1.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img3, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store1, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=735, y=365)
        # two
        self.next_button_img4 = ImageTk.PhotoImage(Image.open("keypad_num_images/2.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img4, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store2, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=880, y=365)

        # three
        self.next_button_img5 = ImageTk.PhotoImage(Image.open("keypad_num_images/3.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img5, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store3, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1025, y=365)
        # four
        self.next_button_img7 = ImageTk.PhotoImage(Image.open("keypad_num_images/4.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img7, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store4, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=720, y=500)
        # five
        self.next_button_img8 = ImageTk.PhotoImage(Image.open("keypad_num_images/5.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img8, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store5, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=878, y=500)

        # six
        self.next_button_img9 = ImageTk.PhotoImage(Image.open("keypad_num_images/6.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img9, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store6, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1040, y=500)
        # seven
        self.next_button_img10 = ImageTk.PhotoImage(Image.open("keypad_num_images/7.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img10, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store7, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=720, y=640)
        # eight
        self.next_button_img11 = ImageTk.PhotoImage(Image.open("keypad_num_images/8.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img11, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store8, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=880, y=640)

        #nine
        self.next_button_img12 = ImageTk.PhotoImage(Image.open("keypad_num_images/9.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img12, highlightthickness=0,
                                     activebackground ='white', background ='white', command=self.store9, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1040, y=640)

        # zero
        self.next_button_img13 = ImageTk.PhotoImage(Image.open("keypad_num_images/0.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img13, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store0, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=732, y=780)

        # Clear
        self.next_button_img14 = ImageTk.PhotoImage(Image.open("keypad_num_images/clear.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img14, highlightthickness=0,
                                     activebackground='white', background='white', command=self.clear_text,
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=870, y=795)

        # Enter button
        self.next_button_img6 = ImageTk.PhotoImage(Image.open("images/Enter_btn.png"))
        self.next_button = tk.Button(self.page2, image=self.next_button_img6, highlightthickness = 0, activebackground ='white', background ='white', command=self.checkpasscode, borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1432, y=882)

#page 3
        self.page3 = tk.Frame(self)
        self.page3.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page3, "images/admin_page.png")

        self.next_button_img17 = ImageTk.PhotoImage(Image.open("images/adminlogin_btn.png"))
        self.next_button = tk.Button(self.page3, image=self.next_button_img17, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page2,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=882)


#page for fuel pump
        self.fuel_pump_page = tk.Frame(self)
        self.fuel_pump_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.fuel_pump_page, "images/fuel_pump_page.png")

        self.next_button_img18 = ImageTk.PhotoImage(Image.open("btn_images/fuel_pump.png"))
        self.next_button = tk.Button(self.page3, image=self.next_button_img18, highlightthickness=0,
                                     activebackground ='#092a81', background ='#092a81', command=self.show_fuel_pump_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=342, y=450)


        self.next_button_img19 = ImageTk.PhotoImage(Image.open("images/adminmenu_btn.png"))
        self.next_button = tk.Button(self.fuel_pump_page, image=self.next_button_img19, highlightthickness=0,
                                       activebackground='white', background='white', command=self.show_page3,
                                       borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)

#page for alternator
        self.alternator_page = tk.Frame(self)
        self.alternator_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.alternator_page, "images/alternator_page.png")

        self.alternator_btn = ImageTk.PhotoImage(Image.open("btn_images/alternator.png"))
        self.next_button = tk.Button(self.page3, image=self.alternator_btn, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.show_alternator_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=973, y=650)



        self.w1 = Scale(self.alternator_page, from_=0, to=100, length=1000, orient=HORIZONTAL, command=self.set_duty_cycle,
                        troughcolor='#0e3999', width=67, sliderrelief='groove', highlightbackground='#0e3999',
                        sliderlength=40, font= ("Tactic Sans Extra Extended", 15), showvalue=0)
        self.w1.set(current_value)
        self.w1.pack()

        self.w1.bind("<B1-Motion>", self.show_values)
        self.w1.place(x=450, y=503)
        self.value_label = Label(self.alternator_page, text=self.current_value, font= ("Tactic Sans Extra Extended", 25), fg='white',bg="#092a81")
        self.value_label.pack()
        self.value_label.place(x=935, y=450)


        self.back = ImageTk.PhotoImage(Image.open("images/adminmenu_btn.png"))
        self.next_button = tk.Button(self.alternator_page, image=self.back, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)
# page for landing gear
        self.landing_gear_page = tk.Frame(self)
        self.landing_gear_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.landing_gear_page, "images/landing_gear_page.png")
        self.show_page(self.page1)

        self.landing_gear_btn = ImageTk.PhotoImage(Image.open("btn_images/landing_gear.png"))
        self.next_button = tk.Button(self.page3, image=self.landing_gear_btn, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.show_landing_gear_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=550, y=650)

        self.back1 = ImageTk.PhotoImage(Image.open("images/adminmenu_btn.png"))
        self.next_button = tk.Button(self.landing_gear_page, image=self.back1, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)

        self.left = ImageTk.PhotoImage(Image.open("btn_images/LEFT.png"))
        self.next_button = tk.Button(self.landing_gear_page, image=self.left, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.reverse_steering,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=342, y=400)

        self.right = ImageTk.PhotoImage(Image.open("btn_images/RIGHT.png"))
        self.next_button = tk.Button(self.landing_gear_page, image=self.right, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.forward_steering,
                                     borderwidth=0, relief="flat", bd=0)
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
        self.page1.pack_forget()
        self.page2.pack_forget()
        self.page3.pack_forget()
        self.fuel_pump_page.pack_forget()
        #self.Dir_antenna.pack_forget()
        #self.Aileron_page.pack_forget()
        self.landing_gear_page.pack_forget()
        self.alternator_page.pack_forget()
        page.pack(side="top", fill="both", expand=True)

    def show_fuel_pump_page(self):
        self.show_page(self.fuel_pump_page)

    def show_alternator_page(self):
         self.show_page(self.alternator_page)
    def show_landing_gear_page(self):
         self.show_page(self.landing_gear_page)

    def show_page2(self):
        self.show_page(self.page2)
    def show_page3(self):
        self.show_page(self.page3)

    def clear_text(self):
        self.password_entry.delete(0, END)
        self.numbers_clicked = []

    def show_page1(self):
        self.numbers_clicked = []
        self.show_page(self.page1)
        self.clear_text()

    def store1(self):
        print("Number 1 is Clicked")
        self.numbers_clicked.append(1)
        self.password_entry.insert(END, '1')

    def store2(self):
        print("Number 2 is Clicked")
        self.numbers_clicked.append(2)
        self.password_entry.insert(END, '2')
    def store3(self):
        print("Number 3 is Clicked")
        self.numbers_clicked.append(3)
        self.password_entry.insert(END, '3')
    def store4(self):
        print("Number 4 is Clicked")
        self.numbers_clicked.append(4)
        self.password_entry.insert(END, '4')
    def store5(self):
        print("Number 5 is Clicked")
        self.numbers_clicked.append(5)
        self.password_entry.insert(END, '5')

    def store6(self):
        print("Number 6 is Clicked")
        self.numbers_clicked.append(6)
        self.password_entry.insert(END, '6')

    def store7(self):
        print("Number 7 is Clicked")
        self.numbers_clicked.append(7)
        self.password_entry.insert(END, '7')

    def store8(self):
        print("Number 8 is Clicked")
        self.numbers_clicked.append(8)
        self.password_entry.insert(END, '8')

    def store9(self):
        print("Number 9 is Clicked")
        self.numbers_clicked.append(9)
        self.password_entry.insert(END, '9')

    def store0(self):
        print("Number 0 is Clicked")
        self.numbers_clicked.append(0)
        self.password_entry.insert(END, '0')

    def checkpasscode(self):
        # Check if all the numbers have been clicked
        if len(self.numbers_clicked) == 4:
            if self.numbers_clicked == [0, 7, 8, 9]:
                # Grant access
                self.show_page3()
                print("Access Granted!")

                self.numbers_clicked = []
                self.clear_text()
            else:
                # Access denied
                tk.messagebox.showerror(message="Access Denied!")
                print("Access denied. Incorrect passcode.")
                self.numbers_clicked = []
                self.clear_text()
        else:
            tk.messagebox.showerror(message="Access Denied!")
            print("Access denied. Incorrect passcode.")
            self.numbers_clicked = []
            self.clear_text()

    def slideshow(self):
        print("slideShow HERE")

    def show_page3(self):
        self.page1.pack_forget()
        self.page2.pack_forget()
        self.fuel_pump_page.pack_forget()
        self.alternator_page.pack_forget()
        self.landing_gear_page.pack_forget()
        ##put the rest of pageessssssssssssssssss
        self.page3.pack(side="top", fill="both", expand=True)

# Define the toggle switch function
    def fuel_toggle_switch(self):
        print("Fuel Pump ON")

    def dir_toggle_switch(self):
        # Disable the button
        print("Directional Antenna ON")
        self.switch_button1.config(state=tk.DISABLED)
        self.update()
        # Run the function
        run()

        # Enable the button after a delay
        self.switch_button1.after(3000, lambda: self.switch_button1.config(state=tk.NORMAL))

    def aileron_toggle_switch(self):
        print("Aileron ON")
    def landing_gear_toggle_switch(self):
        print("Landing Gear ON")
    def Alternator_toggle_switch(self):
        print("Alternator ON")
        self.switch_button5.config(state=tk.DISABLED)
        self.update()
        # Run the function
        run()

        # Enable the button after a delay
        self.switch_button5.after(3000, lambda: self.switch_button1.config(state=tk.NORMAL))


    
    def set_duty_cycle(self, new_value):
        self.duty_cycle = float(new_value)
        pwm.ChangeDutyCycle(self.duty_cycle)

    def show_values(self, event):
        new_value = self.w1.get()
        if new_value != self.current_value:
            self.current_value = new_value
            self.value_label.config(text=self.current_value)
            print(self.current_value)

    def reverse_steering(self):
        print("reverse_steering")

    def reverse_retract(self):
        print("reverse_retract")

    def forward_steering(self):
        print("forward_steering")

    def forward_retract(self):
        print("forward_retract")
if __name__ == "__main__":
    app = GA()
    app.mainloop()
