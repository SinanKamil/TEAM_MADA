import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from time import sleep
from tkinter import messagebox as mb
import time
# from control_aileron import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, aileron_init, Speed, pwm_aileron
from slideshow_video_player import play_video
#import RPi.GPIO as GPIO
#from control_aileron import aileron_forward, aileron_reverse, aileron_disable, aileron_setup, aileron_init, Speed, pwm_aileron
from fuel_pump import pump_enable, pump_disable, user_fuel_pump_control
#from centering_aileron import aileron_center

#from Alternator_LED_DCMotor import DC_LED_function
#from Directional_antenna import antenna
import threading
from control_steering import forward_accelerate, reverse_accelerate, disable_steering
from centering_steering import center_steering
#from admin_antenna import left_antenna, right_antenna, disable_antenna
from user_steering import user_steering_run


aileron_speed_value = 1
class GA(tk.Tk):
    def __init__(self):
        super().__init__()
        # Create instances of each page class with hidden attribute set to True
        self.Fuel_pump_en = False
        self.aileron_speed_value = 1
        self.current_value = 0
        #self.init_Alternator()
        self.numbers_clicked = []
        self.current_value = 0
        self.w1 = 0
        self.geometry("1920x1080")
        self.title('General Atomics')
        self.config(bg="white")
        self.attributes("-fullscreen",True)
        ico = Image.open('/home/pi/TEAM_MADA/images/GA.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)
        self.preload_images()
        self.minutes = 0.20
        self.inactive_time = 10
        self.total_seconds = self.minutes * 60
        self.last_active_time = time.time()
        self.retract_data_float = 0.8


#page 1 here:
        # Create the first page
        self.page1 = tk.Frame(self)
        self.page1.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page1, "/home/pi/TEAM_MADA/images/home_page.png")
        #meet the team bttn

        self.meet_the_team = tk.Frame(self)
        self.meet_the_team.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.meet_the_team, "/home/pi/TEAM_MADA/images/Meet_the_Team_page.png")

        self.next_button_img77 = self.images["/home/pi/TEAM_MADA/images/homemenu_btn.png"]
        self.next_button = tk.Button(self.meet_the_team, image=self.next_button_img77, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page1,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)

        # Create the button to go to slideshow
        self.next_button_img1 = self.images["/home/pi/TEAM_MADA/images/slideshow_btn.png"]
        self.next_button = tk.Button(self.page1, image=self.next_button_img1, activebackground ='white', background ='white', command=self.slideshow, highlightthickness = 0, highlightbackground = '#ffffff', borderwidth=None, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)

        self.meet_team_img = self.images["/home/pi/TEAM_MADA/btn_images/team_btn.png"]
        self.meet_team_btn = tk.Button(self.page1, image=self.meet_team_img,
                                     command=self.show_meet_the_team_page, highlightthickness=0,
                                     activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                     relief="flat", bd=0)
        self.meet_team_btn.place(x=275, y=125)

        # Create the switch button for fuel pump
        self.switch_button_img_on = self.images["/home/pi/TEAM_MADA/btn_images/fuel_pump.png"]
        self.fuel_pump_btn = tk.Button(self.page1, image=self.switch_button_img_on, command=self.fuel_toggle_switch, highlightthickness=0,
                                     activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                     relief="flat", bd=0)
        self.fuel_pump_btn.place(x=342, y=450)
        #This is for the directional antenna
        self.switch_button_img_on1 = self.images["/home/pi/TEAM_MADA/btn_images/directional_antenna.png"]
        self.switch_button1 = tk.Button(self.page1, image=self.switch_button_img_on1, command=self.dir_toggle_switch, highlightthickness=0,
                                     activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                     relief="flat", bd=0)
        self.switch_button1.place(x=765, y=450)
        # This is for the aileron smart servo
        self.switch_button_img_on2 = self.images["/home/pi/TEAM_MADA/btn_images/aileron.png"]
        self.switch_button2 = tk.Button(self.page1, image=self.switch_button_img_on2, command=self.aileron_toggle_switch,
                                        highlightthickness=0,
                                        activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button2.place(x=1188, y=450)

        # This is for the Steering and retract servo
        self.switch_button_img_on4 = self.images["/home/pi/TEAM_MADA/btn_images/landing_gear.png"]
        self.switch_button4 = tk.Button(self.page1, image=self.switch_button_img_on4,
                                        command=self.landing_gear_toggle_switch,
                                        highlightthickness=0,
                                        activebackground ='#092a81', background ='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button4.place(x=550, y=650)


        # This is for the alternator
        self.switch_button_img_on5 = self.images["/home/pi/TEAM_MADA/btn_images/alternator.png"]
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
        self.add_background_image(self.page2, "/home/pi/TEAM_MADA/images/admin_access.png")

        # Create the button to go to page 2
        self.next_button_img = self.images["/home/pi/TEAM_MADA/images/adminlogin_btn.png"]
        self.adminlogin_btn = tk.Button(self.page1, image=self.next_button_img, activebackground='white',
                                        background='white', highlightthickness=0, command=self.show_page2, bd=0)
        self.adminlogin_btn.place(x=1432, y=882)

        # Create the button to go back to page 1
        self.next_button_img2 = self.images["/home/pi/TEAM_MADA/images/homemenu_btn.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img2, highlightthickness = 0, activebackground ='white', background ='white', command=self.show_page1, borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)

        self.label = tk.Label(self.page2, font=("Arial", 20))
        self.label.pack(expand=True)

        self.label.place(x=222, y=200)
        self.bind('<Any-KeyPress>', self.reset_timer)
        self.bind('<Any-Button>', self.reset_timer)
        self.bind('<Motion>', self.reset_timer)


        #create a text box
        self.password_entry = tk.Entry(self.page2, font=('Rubik Medium', 38),  highlightbackground = "#092a81", background= "#092a81",fg="white", width=3,show='*', bd=0, borderwidth=0)
        self.password_entry.place(x=1010, y=217)

        # create the number buttons
        # one
        self.next_button_img3 = self.images["/home/pi/TEAM_MADA/keypad_num_images/1.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img3, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(1),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=735, y=365)
        # two
        self.next_button_img4 = self.images["/home/pi/TEAM_MADA/keypad_num_images/2.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img4, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(2),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=880, y=365)

        # three
        self.next_button_img5 = self.images["/home/pi/TEAM_MADA/keypad_num_images/3.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img5, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(3),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1025, y=365)
        # four
        self.next_button_img7 = self.images["/home/pi/TEAM_MADA/keypad_num_images/4.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img7, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(4),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=720, y=500)
        # five
        self.next_button_img8 = self.images["/home/pi/TEAM_MADA/keypad_num_images/5.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img8, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(5),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=878, y=500)

        # six
        self.next_button_img9 = self.images["/home/pi/TEAM_MADA/keypad_num_images/6.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img9, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(6),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1040, y=500)
        # seven
        self.next_button_img10 = self.images["/home/pi/TEAM_MADA/keypad_num_images/7.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img10, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(7),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=720, y=640)
        # eight
        self.next_button_img11 = self.images["/home/pi/TEAM_MADA/keypad_num_images/8.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img11, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(8),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=880, y=640)

        # nine
        self.next_button_img12 = self.images["/home/pi/TEAM_MADA/keypad_num_images/9.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img12, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(9),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1040, y=640)

        # zero
        self.next_button_img13 = self.images["/home/pi/TEAM_MADA/keypad_num_images/0.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img13, highlightthickness=0,
                                     activebackground='white', background='white', command=lambda: self.store(0),
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=732, y=780)

        # Clear
        self.next_button_img14 = self.images["/home/pi/TEAM_MADA/keypad_num_images/clear.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img14, highlightthickness=0,
                                     activebackground='white', background='white', command=self.clear_text,
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=870, y=795)

        # Enter button
        self.next_button_img6 = self.images["/home/pi/TEAM_MADA/images/Enter_btn.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img6, highlightthickness = 0, activebackground ='white', background ='white', command=self.checkpasscode, borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1432, y=882)

#page 3
        self.page3 = tk.Frame(self)
        self.page3.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page3, "/home/pi/TEAM_MADA/images/admin_page.png")

        self.next_button_img17 = self.images["/home/pi/TEAM_MADA/images/homemenu_btn.png"]
        self.next_button = tk.Button(self.page3, image=self.next_button_img17, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page1,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)


        self.exit_btn = self.images["/home/pi/TEAM_MADA/btn_images/exit_btn.png"]
        self.next_button = tk.Button(self.page3, image=self.exit_btn, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.exit,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1700, y=50)

#page for fuel pump
        self.fuel_pump_page = tk.Frame(self)
        self.fuel_pump_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.fuel_pump_page, "/home/pi/TEAM_MADA/images/fuel_pump_page.png")

        self.next_button_img18 = self.images["/home/pi/TEAM_MADA/btn_images/fuel_pump.png"]
        self.next_button = tk.Button(self.page3, image=self.next_button_img18, highlightthickness=0,
                                     activebackground ='#092a81', background ='#092a81', command=self.show_fuel_pump_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=342, y=450)

        # Create the switch button for fuel pump
        self.switch_button_fuel_on = self.images["/home/pi/TEAM_MADA/btn_images/Fuel_pump_on.png"]
        self.switch_button_fuel_off = self.images["/home/pi/TEAM_MADA/btn_images/Fuel_pump_off.png"]
        self.switch_button_fuel = tk.Button(self.fuel_pump_page, image=self.switch_button_fuel_off, command=self.fuelpump_on_off,
                                       highlightthickness=0,
                                       activebackground='#092a81', background='#092a81', borderwidth=0,
                                       relief="flat", bd=0)
        self.switch_button_fuel.place(x=800, y=500)

        self.next_button_img19 = self.images["/home/pi/TEAM_MADA/images/adminmenu_btn.png"]
        self.fuel_home = tk.Button(self.fuel_pump_page, image=self.next_button_img19, highlightthickness=0,
                                       activebackground='white', background='white', command=self.show_page3,
                                       borderwidth=0, relief="flat", bd=0)
        self.fuel_home.place(x=230, y=884)

#page for alternator
        self.alternator_page = tk.Frame(self)
        self.alternator_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.alternator_page, "/home/pi/TEAM_MADA/images/alternator_page.png")

        self.alternator_img_btn = self.images["/home/pi/TEAM_MADA/btn_images/alternator.png"]
        self.alternator_btn = tk.Button(self.page3, image=self.alternator_img_btn, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.show_alternator_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.alternator_btn.place(x=973, y=650)



        self.w1 = Scale(self.alternator_page, from_=0, to=100, length=1000, orient=HORIZONTAL,
                        troughcolor='#0e3999', width=67, sliderrelief='groove', highlightbackground='#0e3999',
                        sliderlength=40, font= ("Tactic Sans Extra Extended", 15), showvalue=0)
        self.w1.set(self.current_value)
        self.w1.pack()
        self.w1.place(x=450, y=503)

        self.value_label = Label(self.alternator_page, text=self.current_value, font=("Tactic Sans Extra Extended", 25), fg='white', bg="#092a81")
        self.value_label.pack()
        self.value_label.place(x=935, y=450)


        self.back = self.images["/home/pi/TEAM_MADA/images/adminmenu_btn.png"]
        self.next_button = tk.Button(self.alternator_page, image=self.back, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)
# page for landing gear
        self.landing_gear_page = tk.Frame(self)
        self.landing_gear_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.landing_gear_page, "/home/pi/TEAM_MADA/images/landing_gear_page.png")


        self.landing_gear_btn = self.images["/home/pi/TEAM_MADA/btn_images/landing_gear.png"]
        self.landing_gear_btn_fun = tk.Button(self.page3, image=self.landing_gear_btn, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.show_landing_gear_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.landing_gear_btn_fun.place(x=550, y=650)

        self.back1 = self.images["/home/pi/TEAM_MADA/images/adminmenu_btn.png"]
        self.next_button = tk.Button(self.landing_gear_page, image=self.back1, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=234, y=884)

        self.left = self.images["/home/pi/TEAM_MADA/btn_images/steer_left.png"]
        self.left_steering = tk.Button(self.landing_gear_page, image=self.left, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.left_steering.bind("<ButtonPress>", lambda event: self.reverse_steering())
        self.left_steering.bind("<ButtonRelease>", lambda event: self.disable_steering())
        self.left_steering.place(x=400, y=500)

        self.right = self.images["/home/pi/TEAM_MADA/btn_images/steer_right.png"]
        self.right_steering = tk.Button(self.landing_gear_page, image=self.right, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.right_steering.bind("<ButtonPress>", lambda event: self.forward_steering())
        self.right_steering.bind("<ButtonRelease>", lambda event: self.disable_steering())
        self.right_steering.place(x=1192, y=500)
        #center
        self.center = self.images["/home/pi/TEAM_MADA/btn_images/center.png"]
        self.center_landing = tk.Button(self.landing_gear_page, image=self.center, highlightthickness=0,command=self.center_landing_gear,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.center_landing.place(x=800, y=500)

        self.retract_down = self.images["/home/pi/TEAM_MADA/btn_images/retract_down.png"]
        self.retract_down_btn = tk.Button(self.landing_gear_page, image=self.retract_down, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.reverse_retract,
                                     borderwidth=0, relief="flat", bd=0)
        self.retract_down_btn.place(x=800, y=725)

        self.retract_up = self.images["/home/pi/TEAM_MADA/btn_images/retract_up.png"]
        self.retract_up_btn = tk.Button(self.landing_gear_page, image=self.retract_up, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.forward_retract,
                                     borderwidth=0, relief="flat", bd=0)
        self.retract_up_btn.place(x=800, y=275)
#page for Aileron Smart Servo
        # 10 slide show and five for inactive
        self.aileron_servo_page = tk.Frame(self)
        self.aileron_servo_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.aileron_servo_page, "/home/pi/TEAM_MADA/images/aileron_page.png")

        self.aileron_btn = self.images["/home/pi/TEAM_MADA/btn_images/aileron.png"]
        self.next_button = tk.Button(self.page3, image=self.aileron_btn, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.show_aileron_servo_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1188, y=450)

        self.aileron_speed = Scale(self.aileron_servo_page, from_=100, to=1, length=360, orient=VERTICAL,
                        troughcolor='#0e3999', width=76, sliderrelief='groove', highlightbackground='#0e3999',
                        sliderlength=40, font=("Tactic Sans Extra Extended", 15), showvalue=0)
        self.aileron_speed.set(aileron_speed_value)
        self.aileron_speed.pack()

        self.aileron_speed.bind("<B1-Motion>", self.aileron_show_values)
        self.aileron_speed.place(x=1259, y=385)
        self.aileron_value_label = Label(self.aileron_servo_page, text=self.aileron_speed_value, font=("Tactic Sans Extra Extended", 25),
                                 fg='white', bg="#092a81")
        self.aileron_value_label.pack()
        self.aileron_value_label.place(x=1280, y=840)

        # center
        self.center_aileron_img = self.images["/home/pi/TEAM_MADA/btn_images/center.png"]
        self.aileron_centering = tk.Button(self.aileron_servo_page, image=self.center_aileron_img, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.center_aileron,
                                     borderwidth=0, relief="flat", bd=0)
        self.aileron_centering.place(x=800, y=500)

        self.down_aileron_img = self.images["/home/pi/TEAM_MADA/btn_images/aileron_down.png"]
        self.down_aileron_btn = tk.Button(self.aileron_servo_page, image=self.down_aileron_img, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.down_aileron_btn.bind("<ButtonPress>", lambda event: self.down_aileron())
        self.down_aileron_btn.bind("<ButtonRelease>", lambda event: self.disable_aileron())
        self.down_aileron_btn.place(x=800, y=725)

        self.up_aileron_img = self.images["/home/pi/TEAM_MADA/btn_images/aileron_up.png"]
        self.up_aileron_btn = tk.Button(self.aileron_servo_page, image=self.up_aileron_img, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.up_aileron_btn.bind("<ButtonPress>", lambda event: self.up_aileron())
        #
        self.up_aileron_btn.bind("<ButtonRelease>", lambda event: self.disable_aileron())
        self.up_aileron_btn.place(x=800, y=275)

        self.back2 = self.images["/home/pi/TEAM_MADA/images/adminmenu_btn.png"]
        self.next_button = tk.Button(self.aileron_servo_page, image=self.back2, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)
# page for Directional Antenna
        self.directional_antenna_page = tk.Frame(self)
        self.directional_antenna_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.directional_antenna_page, "/home/pi/TEAM_MADA/images/directional_antenna_page.png")
        self.show_page(self.page1)
        self.directional_antenna_btn = self.images["/home/pi/TEAM_MADA/btn_images/directional_antenna.png"]
        self.next_button = tk.Button(self.page3, image=self.directional_antenna_btn, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     command=self.show_directional_antenna_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=765, y=450)

        self.left_antenna_img = self.images["/home/pi/TEAM_MADA/btn_images/antenna_left.png"]
        self.left_antenna_btn = tk.Button(self.directional_antenna_page, image=self.left_antenna_img, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.left_antenna_btn.bind("<ButtonPress>", lambda event: self.left_antenna())
        self.left_antenna_btn.bind("<ButtonRelease>", lambda event: self.disable_dir_antenna())
        self.left_antenna_btn.place(x=350, y=480)

        self.right_antenna_img = self.images["/home/pi/TEAM_MADA/btn_images/antenna_right.png"]
        self.right_antenna_btn = tk.Button(self.directional_antenna_page, image=self.right_antenna_img, highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     borderwidth=0, relief="flat", bd=0)
        self.right_antenna_btn.bind("<ButtonPress>", lambda event: self.right_antenna())
        self.right_antenna_btn.bind("<ButtonRelease>", lambda event: self.disable_dir_antenna())
        self.right_antenna_btn.place(x=1250, y=480)

        self.back3 = self.images["/home/pi/TEAM_MADA/images/adminmenu_btn.png"]
        self.next_button = tk.Button(self.directional_antenna_page, image=self.back3, highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)


    def add_background_image(self, frame, file):
        img = Image.open(file)
        img = ImageTk.PhotoImage(img)
        label = tk.Label(frame, image=img)
        label.image = img
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def show_page(self, page):
        self.page1.pack_forget()
        self.page2.pack_forget()
        self.page3.pack_forget()
        self.fuel_pump_page.pack_forget()
        self.directional_antenna_page.pack_forget()
        self.aileron_servo_page.pack_forget()
        self.landing_gear_page.pack_forget()
        self.alternator_page.pack_forget()
        self.meet_the_team.pack_forget()
        page.pack(side="top", fill="both", expand=True)

    def show_fuel_pump_page(self):
        self.show_page(self.fuel_pump_page)
        self.reset_timer()
        self.update_label()
    def show_aileron_servo_page(self):
        self.show_page(self.aileron_servo_page)
        self.reset_timer()
        self.update_label()
    def show_alternator_page(self):
        self.show_page(self.alternator_page)
        self.reset_timer()
        self.update_label()
    def show_landing_gear_page(self):
         self.show_page(self.landing_gear_page)
         self.reset_timer()
         self.update_label()

         if 0.9 >= self.retract_data_float:
             self.retract_up_btn.config(state=tk.DISABLED)
         if 1.65 <= self.retract_data_float:
             self.retract_down_btn.config(state=tk.DISABLED)
    def show_directional_antenna_page(self):
        self.show_page(self.directional_antenna_page)
        self.reset_timer()
        self.update_label()
    def show_page2(self):
        self.show_page(self.page2)
        self.reset_timer()
        self.update_label()
    def show_page3(self):
        self.show_page(self.page3)
        self.reset_timer()
        self.update_label()

    def show_meet_the_team_page(self):
        self.show_page(self.meet_the_team)
        self.reset_timer()
        self.update_label()

    def clear_text(self):
        self.password_entry.delete(0, END)
        self.numbers_clicked = []

    def show_page1(self):
        self.numbers_clicked = []
        self.show_page(self.page1)
        self.clear_text()

    def store(self, number):
        print("Number", number, "is Clicked")
        self.numbers_clicked.append(number)
        self.password_entry.insert(END, 'x')

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
        #play_video()
        play_video()
# Define the toggle switch function
    def fuel_toggle_switch(self):
        print("fuel pump ON")
        self.fuel_pump_btn.config(state=tk.DISABLED)
        self.adminlogin_btn.config(state=tk.DISABLED)
        self.update()

        def callback_fuelpump():  # this to enable button
            self.fuel_pump_btn.config(state=tk.NORMAL)
            self.adminlogin_btn.config(state=tk.NORMAL)
        
        # Create a new thread to run the DC LED function
        led_thread = threading.Thread(target=user_fuel_pump_control, args=(callback_fuelpump,))
        led_thread.start()

    def dir_toggle_switch(self):
        # Disable the button
        print("Directional Antenna ON")
        self.switch_button1.config(state=tk.DISABLED)
        self.adminlogin_btn.config(state=tk.DISABLED)
        self.update()

        def callback_directional():  # this to enable button
            self.switch_button1.config(state=tk.NORMAL)
            self.adminlogin_btn.config(state=tk.NORMAL)
        antenna_thread = threading.Thread(target=antenna, args=(callback_directional,))
        antenna_thread.start()

    def aileron_toggle_switch(self):
        print("Aileron ON")
    def landing_gear_toggle_switch(self):
        print("Landing Gear ON")
        self.switch_button4.config(state=tk.DISABLED)
        self.adminlogin_btn.config(state=tk.DISABLED)
        self.update()


        def callback_landing_gear():  # this to enable button
            self.switch_button4.config(state=tk.NORMAL)
            self.adminlogin_btn.config(state=tk.NORMAL)

        steering_thread = threading.Thread(target=user_steering_run, args=(callback_landing_gear,))
        steering_thread.start()
    def Alternator_toggle_switch(self):
        print("Alternator ON")
        self.switch_button5.config(state=tk.DISABLED)
        self.adminlogin_btn.config(state=tk.DISABLED)
        self.update()

        def callback_alternator():  # this to enable button
            self.switch_button5.config(state=tk.NORMAL)
            self.adminlogin_btn.config(state=tk.NORMAL)

        # Create a new thread to run the DC LED function
        led_thread = threading.Thread(target=self.DC_LED_function, args=(callback_alternator,))
        led_thread.start()

    def init_Alternator(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9, GPIO.OUT)  # for DC motor
        GPIO.setup(21, GPIO.OUT)  # for LED
        self.p = GPIO.PWM(21, 100)  # Initialize PWM on pin 12 with a frequency of 50Hz
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
    def DC_LED_function(self, callback):
        times = 3
        for i in range(times):
            for duty in range(0,100,1):
                self.p.ChangeDutyCycle(duty)
                self.pwmDC.ChangeDutyCycle(duty)

                sleep(.02)
            sleep(.01)

            for duty in range(100,-1,-1):
                self.p.ChangeDutyCycle(duty)
                self.pwmDC.ChangeDutyCycle(duty)

                sleep(.02)
            sleep(.01)
        callback()




    def __del__(self):
        self.p.stop()
        self.pwmDC.stop()
        GPIO.cleanup()



    #def __del__(self):
    #    self.p.stop()
    #    self.pwmDC.stop()
    #    GPIO.cleanup()


    def aileron_show_values(self, event):
        new_value = self.aileron_speed.get()
        if new_value != self.aileron_speed_value:
            self.aileron_speed_value = new_value
            self.aileron_value_label.config(text=self.aileron_speed_value)
            self.converted_value = (self.aileron_speed_value / 100) * 25
            if self.converted_value <= 1:
                self.value = 1
            else:
                self.value = round(self.converted_value)
            print(self.value)
    def center_landing_gear(self):
        center_steering()
        print("Center")

    def reverse_steering(self):
        print("reverse_steering")
        reverse_accelerate(-80)

    def forward_steering(self):
        print("forward_steering")
        forward_accelerate(80)

    def disable_steering(self):
        disable_steering()

    def forward_retract(self):
        self.retract_data_float -= 0.05
        # self.retract_data_float = retract_validate_data()
        print(self.retract_data_float)
        if 0.9 <= self.retract_data_float <= 1.65:
            self.retract_up_btn.config(state=tk.NORMAL)
            self.retract_down_btn.config(state=tk.NORMAL)
        else:
            if self.retract_data_float < 0.9:
                self.retract_up_btn.config(state=tk.DISABLED)
            else:
                self.retract_up_btn.config(state=tk.NORMAL)

    def reverse_retract(self):
        self.retract_data_float += 0.05
        # self.retract_data_float = retract_validate_data()
        print(self.retract_data_float)
        if 0.9 <= self.retract_data_float <= 1.65:
            self.retract_up_btn.config(state=tk.NORMAL)
            self.retract_down_btn.config(state=tk.NORMAL)
        else:
            if self.retract_data_float > 1.65:
                self.retract_down_btn.config(state=tk.DISABLED)
            else:
                self.retract_down_btn.config(state=tk.NORMAL)

    def exit(self):
        res = mb.askquestion('EXIT APPLICATION', 'Would you like to terminate the program and exit the application?')
        if res == 'yes':
            self.destroy()

    def up_aileron(self):
        aileron_reverse(pwm_aileron, self.value)
    def down_aileron(self):
        aileron_forward(pwm_aileron, self.value)
    def disable_aileron(self):
        aileron_disable()
    def center_aileron(self):
        aileron_center()

    def left_antenna(self):
        left_antenna()
    def right_antenna(self):
        right_antenna()
    def disable_dir_antenna(self):
        disable_antenna()
    def center_aileron(self):
        aileron_center()
    def reset_timer(self, event=None):
        self.last_active_time = time.time() #time goes back to normal

    def update_label(self):
        current_time = time.time()#most current time
        elapsed_time = current_time - self.last_active_time #start decrementating
        remaining_time = self.total_seconds - elapsed_time #how much time left
        if remaining_time <= 0:#if zero go to page 1
            self.show_page1()
        else:
            minutes, seconds = divmod(int(remaining_time), 60)
            # DELETE LATER
            self.label.configure(text="Time remaining: {:02d}:{:02d}".format(minutes, seconds))
            if elapsed_time > self.inactive_time:
                self.label.configure(foreground='red')
            else:
                self.label.configure(foreground='black')
            self.label.after(250, self.update_label)

    # Define the toggle switch function
    def fuelpump_on_off(self):
        if not self.Fuel_pump_en:
            self.Fuel_pump_en = True
            self.switch_button_fuel.config(image=self.switch_button_fuel_on)
            self.fuel_home.config(state=tk.DISABLED)
            pump_enable()
        else:
            self.Fuel_pump_en = False
            self.switch_button_fuel.config(image=self.switch_button_fuel_off)
            self.fuel_home.config(state=tk.NORMAL)
            pump_disable()
    def preload_images(self):
        # Create a dictionary of all image file paths
        self.images = {}
        image_paths = ["/home/pi/TEAM_MADA/images/home_page.png",
                       "/home/pi/TEAM_MADA/images/adminlogin_btn.png",
                       "/home/pi/TEAM_MADA/images/slideshow_btn.png",
                       "/home/pi/TEAM_MADA/btn_images/fuel_pump.png",
                       "/home/pi/TEAM_MADA/btn_images/directional_antenna.png",
                       "/home/pi/TEAM_MADA/btn_images/aileron.png",
                       "/home/pi/TEAM_MADA/btn_images/landing_gear.png",
                       "/home/pi/TEAM_MADA/btn_images/alternator.png",
                       "/home/pi/TEAM_MADA/btn_images/landing_gear.png",
                       "/home/pi/TEAM_MADA/btn_images/alternator.png",
                       "/home/pi/TEAM_MADA/images/homemenu_btn.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/1.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/2.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/3.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/4.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/5.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/6.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/7.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/8.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/9.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/0.png",
                       "/home/pi/TEAM_MADA/keypad_num_images/clear.png",
                       "/home/pi/TEAM_MADA/images/Enter_btn.png",
                       "/home/pi/TEAM_MADA/images/homemenu_btn.png",
                       "/home/pi/TEAM_MADA/btn_images/exit_btn.png",
                       "/home/pi/TEAM_MADA/btn_images/fuel_pump.png",
                       "/home/pi/TEAM_MADA/btn_images/Fuel_pump_on.png",
                       "/home/pi/TEAM_MADA/btn_images/Fuel_pump_off.png",
                       "/home/pi/TEAM_MADA/images/adminmenu_btn.png",
                       "/home/pi/TEAM_MADA/btn_images/alternator.png",
                       "/home/pi/TEAM_MADA/images/adminmenu_btn.png",
                       "/home/pi/TEAM_MADA/btn_images/landing_gear.png",
                       "/home/pi/TEAM_MADA/btn_images/steer_left.png",
                       "/home/pi/TEAM_MADA/btn_images/steer_right.png",
                       "/home/pi/TEAM_MADA/btn_images/center.png",
                       "/home/pi/TEAM_MADA/btn_images/retract_down.png",
                       "/home/pi/TEAM_MADA/btn_images/retract_up.png",
                       "/home/pi/TEAM_MADA/btn_images/aileron.png",
                       "/home/pi/TEAM_MADA/btn_images/center.png",
                       "/home/pi/TEAM_MADA/btn_images/aileron_down.png",
                       "/home/pi/TEAM_MADA/btn_images/aileron_up.png",
                       "/home/pi/TEAM_MADA/images/adminmenu_btn.png",
                       "/home/pi/TEAM_MADA/btn_images/directional_antenna.png",
                       "/home/pi/TEAM_MADA/btn_images/antenna_left.png",
                       "/home/pi/TEAM_MADA/btn_images/antenna_right.png",
                       "/home/pi/TEAM_MADA/images/adminmenu_btn.png",
                       "/home/pi/TEAM_MADA/btn_images/team_btn.png"
                       ]

        # Load each image and store it as an attribute of the class
        for path in image_paths:
            img = Image.open(path)
            self.images[path] = ImageTk.PhotoImage(img)

if __name__ == "__main__":
    app = GA()
    app.mainloop()