<<<<<<< HEAD
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from time import sleep
from tkinter import messagebox as mb
import time
#from slideshow_video_player import VideoPlayer

#from Alternator_LED_DCMotor import DC_LED_function
#from Directional_antenna import antenna
import threading

#from Button_control_steering import forward_accelerate, disable_steering, reverse_accelerate
#from steering_code import motors, MAX_SPEED
#from centering_steering import center
#from admin_antenna import left_antenna, right_antenna, disable_antenna
#from user_steering import user_steering_run

# import RPi.GPIO as GPIO

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(10, GPIO.OUT)
# pwm = GPIO.PWM(10, 100)
# pwm.start(0)


current_value = 0
aileron_speed_value = 0


class GA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Fuel_pump_en = False
        self.aileron_speed_value = 0
        self.numbers_clicked = []
        self.current_value = 0
        self.w1 = 0
        self.geometry("1920x1080")
        self.title('General Atomics')
        self.config(bg="white")
        self.attributes("-fullscreen", True)
        ico = Image.open('images/GA.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        self.minutes = 0.20
        self.inactive_time = 10
        self.total_seconds = self.minutes * 60
        self.last_active_time = time.time()
        self.preload_images()
        # page 1 here:
        # Create the first page
        self.page1 = tk.Frame(self)
        self.page1.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page1, "images/home_page.png")

        # Create the button to go to page 2
        self.adminlogin_btn = tk.Button(self.page1, image=self.images["images/adminlogin_btn.png"], activebackground='white',
                                        background='white', highlightthickness=0, command=self.show_page2, bd=0)
        self.adminlogin_btn.place(x=1432, y=882)

        # Create the button to go to slideshow
        self.next_button = tk.Button(self.page1, image=self.images["images/slideshow_btn.png"], activebackground='white',
                                     background='white', command=self.slideshow, highlightthickness=0,
                                     highlightbackground='#ffffff', borderwidth=None, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)

        # Create the switch button for fuel pump

        self.switch_button = tk.Button(self.page1, image=self.images["btn_images/fuel_pump.png"], command=self.fuel_toggle_switch,
                                       highlightthickness=0,
                                       activebackground='#092a81', background='#092a81', borderwidth=0,
                                       relief="flat", bd=0)
        self.switch_button.place(x=342, y=450)
        # This is for the directional antenna
        self.switch_button1 = tk.Button(self.page1, image=self.images["btn_images/directional_antenna.png"], command=self.dir_toggle_switch,
                                        highlightthickness=0,
                                        activebackground='#092a81', background='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button1.place(x=765, y=450)
        # This is for the aileron smart servo
        self.switch_button2 = tk.Button(self.page1, image=self.images["btn_images/aileron.png"],
                                        command=self.aileron_toggle_switch,
                                        highlightthickness=0,
                                        activebackground='#092a81', background='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button2.place(x=1188, y=450)

        # This is for the Steering and retract servo
        self.switch_button4 = tk.Button(self.page1, image=self.images["btn_images/landing_gear.png"],
                                        command=self.landing_gear_toggle_switch,
                                        highlightthickness=0,
                                        activebackground='#092a81', background='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button4.place(x=550, y=650)

        # This is for the alternator
        self.switch_button5 = tk.Button(self.page1, image=self.images["btn_images/alternator.png"],
                                        command=self.Alternator_toggle_switch,
                                        highlightthickness=0,
                                        activebackground='#092a81', background='#092a81', borderwidth=0,
                                        relief="flat", bd=0)
        self.switch_button5.place(x=973, y=650)
        # page 2 here:
        # Create the second page
        self.page2 = tk.Frame(self)
        self.page2.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page2, "images/admin_access.png")

        # Create the button to go back to page 1
        self.next_button = tk.Button(self.page2, image=self.images["images/homemenu_btn.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page1,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)

        self.label = tk.Label(self.page2, font=("Arial", 20))
        self.label.pack(expand=True)

        self.label.place(x=222, y=200)
        self.bind('<Any-KeyPress>', self.reset_timer)
        self.bind('<Any-Button>', self.reset_timer)
        self.bind('<Motion>', self.reset_timer)
        #self.update_label()

        # create a text box
        self.password_entry = tk.Entry(self.page2, font=('Rubik Medium', 38), background="#092a81", fg="white", width=3,
                                       show='*', bd=0, borderwidth=0)
        self.password_entry.place(x=1010, y=220)

        # create the number buttons
        # one
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/1.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store1, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=735, y=365)
        # two
        self.next_button_img4 = self.images["keypad_num_images/2.png"]
        self.next_button = tk.Button(self.page2, image=self.next_button_img4, highlightthickness=0,
                                     activebackground='white', background='white', command=self.store2, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=880, y=365)

        # three
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/3.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store3, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1025, y=365)
        # four
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/4.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store4, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=720, y=500)
        # five
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/5.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store5, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=878, y=500)

        # six
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/6.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store6, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1040, y=500)
        # seven
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/7.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store7, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=720, y=640)
        # eight
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/8.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store8, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=880, y=640)

        # nine"]
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/9.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store9, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=1040, y=640)

        # zero
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/0.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.store0, borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=732, y=780)

        # Clear
        self.next_button = tk.Button(self.page2, image=self.images["keypad_num_images/clear.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.clear_text,
                                     borderwidth=0,
                                     relief="flat", bd=0)
        self.next_button.place(x=870, y=795)

        # Enter button
        self.next_button = tk.Button(self.page2, image=self.images["images/Enter_btn.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.checkpasscode,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1432, y=882)

        # page 3
        self.page3 = tk.Frame(self)
        self.page3.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.page3, "images/admin_page.png")


        self.next_button = tk.Button(self.page3, image=self.images["images/homemenu_btn.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page1,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=222, y=882)

        self.next_button = tk.Button(self.page3, image=self.images["btn_images/exit_btn.png"], highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.exit,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1700, y=50)

        # page for fuel pump
        self.fuel_pump_page = tk.Frame(self)
        self.fuel_pump_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.fuel_pump_page, "images/fuel_pump_page.png")

        self.next_button = tk.Button(self.page3, image=self.images["btn_images/fuel_pump.png"], highlightthickness=0,
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

        self.next_button = tk.Button(self.fuel_pump_page, image=self.images["images/adminmenu_btn.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)

        # page for alternator
        self.alternator_page = tk.Frame(self)
        self.alternator_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.alternator_page, "images/alternator_page.png")

        self.alternator_btn = tk.Button(self.page3, image=self.images["btn_images/alternator.png"], highlightthickness=0,
                                        activebackground='#092a81', background='#092a81',
                                        command=self.show_alternator_page,
                                        borderwidth=0, relief="flat", bd=0)
        self.alternator_btn.place(x=973, y=650)

        self.w1 = Scale(self.alternator_page, from_=0, to=100, length=1000, orient=HORIZONTAL,
                        troughcolor='#0e3999', width=67, sliderrelief='groove', highlightbackground='#0e3999',
                        sliderlength=40, font=("Tactic Sans Extra Extended", 15), showvalue=0)
        self.w1.set(current_value)
        self.w1.pack()

        self.w1.bind("<B1-Motion>", self.show_values)
        self.w1.place(x=450, y=503)
        self.value_label = Label(self.alternator_page, text=self.current_value, font=("Tactic Sans Extra Extended", 25),
                                 fg='white', bg="#092a81")
        self.value_label.pack()
        self.value_label.place(x=935, y=450)

        self.next_button = tk.Button(self.alternator_page, image=self.images["images/adminmenu_btn.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)
        # page for landing gear
        self.landing_gear_page = tk.Frame(self)
        self.landing_gear_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.landing_gear_page, "images/landing_gear_page.png")

        self.landing_gear_btn_fun = tk.Button(self.page3, image=self.images["btn_images/landing_gear.png"], highlightthickness=0,
                                              activebackground='#092a81', background='#092a81',
                                              command=self.show_landing_gear_page,
                                              borderwidth=0, relief="flat", bd=0)
        self.landing_gear_btn_fun.place(x=550, y=650)

        self.next_button = tk.Button(self.landing_gear_page, image=self.images["images/adminmenu_btn.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=234, y=884)

        self.left_steering = tk.Button(self.landing_gear_page, image=self.images["btn_images/steer_left.png"], highlightthickness=0,
                                       activebackground='#092a81', background='#092a81',
                                       borderwidth=0, relief="flat", bd=0)
        self.left_steering.bind("<ButtonPress>", lambda event: self.reverse_steering())
        self.left_steering.bind("<ButtonRelease>", lambda event: self.disable_steering())
        self.left_steering.place(x=400, y=500)

        self.right_steering = tk.Button(self.landing_gear_page, image=self.images["btn_images/steer_right.png"], highlightthickness=0,
                                        activebackground='#092a81', background='#092a81',
                                        borderwidth=0, relief="flat", bd=0)
        self.right_steering.bind("<ButtonPress>", lambda event: self.forward_steering())
        self.right_steering.bind("<ButtonRelease>", lambda event: self.disable_steering())
        self.right_steering.place(x=1192, y=500)
        # center

        self.center_landing = tk.Button(self.landing_gear_page, image=self.images["btn_images/center.png"], highlightthickness=0,
                                        command=self.center_landing_gear,
                                        activebackground='#092a81', background='#092a81',
                                        borderwidth=0, relief="flat", bd=0)
        self.center_landing.place(x=800, y=500)

        self.next_button = tk.Button(self.landing_gear_page, image=self.images["btn_images/retract_down.png"], highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.reverse_retract,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=800, y=725)

        self.next_button = tk.Button(self.landing_gear_page, image=self.images["btn_images/retract_up.png"], highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.forward_retract,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=800, y=275)
        # page for Aileron Smart Servo
        # 10 slide show and five for inactive
        self.aileron_servo_page = tk.Frame(self)
        self.aileron_servo_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.aileron_servo_page, "images/aileron_page.png")

        self.next_button = tk.Button(self.page3, image=self.images["btn_images/aileron.png"], highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     command=self.show_aileron_servo_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=1188, y=450)

        self.aileron_speed = Scale(self.aileron_servo_page, from_=100, to=0, length=360, orient=VERTICAL,
                                   troughcolor='#0e3999', width=76, sliderrelief='groove',
                                   highlightbackground='#0e3999',
                                   sliderlength=40, font=("Tactic Sans Extra Extended", 15), showvalue=0)
        self.aileron_speed.set(aileron_speed_value)
        self.aileron_speed.pack()

        self.aileron_speed.bind("<B1-Motion>", self.aileron_show_values)
        self.aileron_speed.place(x=1259, y=385)
        self.aileron_value_label = Label(self.aileron_servo_page, text=self.aileron_speed_value,
                                         font=("Tactic Sans Extra Extended", 25),
                                         fg='white', bg="#092a81")
        self.aileron_value_label.pack()
        self.aileron_value_label.place(x=1280, y=840)

        # center
        self.next_button = tk.Button(self.aileron_servo_page, image=self.images["btn_images/center.png"], highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.center_aileron,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=800, y=500)

        self.next_button = tk.Button(self.aileron_servo_page, image=self.images["btn_images/aileron_down.png"], highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.down_aileron,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=800, y=725)

        self.next_button = tk.Button(self.aileron_servo_page, image=self.images["btn_images/aileron_up.png"], highlightthickness=0,
                                     activebackground='#092a81', background='#092a81', command=self.up_aileron,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=800, y=275)

        self.next_button = tk.Button(self.aileron_servo_page, image=self.images["images/adminmenu_btn.png"], highlightthickness=0,
                                     activebackground='white', background='white', command=self.show_page3,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=230, y=884)
        # page for Directional Antenna
        self.directional_antenna_page = tk.Frame(self)
        self.directional_antenna_page.pack(side="top", fill="both", expand=True)
        self.add_background_image(self.directional_antenna_page, "images/directional_antenna_page.png")
        self.show_page(self.page1)
        self.next_button = tk.Button(self.page3, image=self.images["btn_images/directional_antenna.png"], highlightthickness=0,
                                     activebackground='#092a81', background='#092a81',
                                     command=self.show_directional_antenna_page,
                                     borderwidth=0, relief="flat", bd=0)
        self.next_button.place(x=765, y=450)
=======
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QStackedWidget
from PyQt5.QtGui import QFont, QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt, QRect, QPropertyAnimation
from PyQt5.QtCore import QEasingCurve


class Page1(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("images/home_page.png").scaled(1920, 1080, Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
>>>>>>> 5cf5d871d94f81f033a11ba6b3dbd696f3b7a504


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("images/admin_page.png").scaled(1920, 1080, Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)


class Page3(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap("images/admin_access.png").scaled(1920, 1080, Qt.KeepAspectRatio)
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1920, 1080)
        self.setWindowTitle("3-Page GUI with Smooth Transitions")

        self.stacked_widget = QStackedWidget(self)
        self.page1 = Page1()
        self.page2 = Page2()
        self.page3 = Page3()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        button_layout = QHBoxLayout()
        self.button1 = QPushButton("Page 1")
        self.button2 = QPushButton("Page 2")
        self.button3 = QPushButton("Page 3")
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        layout.addLayout(button_layout)

        self.button1.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page1))
        self.button2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page2))
        self.button3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page3))

        self.show()

        self.animation = QPropertyAnimation(self.stacked_widget, b"geometry")
        self.animation.setDuration(500)
        easing_curve = QEasingCurve.InOutQuad

        # Set the easing curve of the animation
        self.animation.setEasingCurve(easing_curve)

    def animate(self, start, end):
        self.animation.setStartValue(start)
        self.animation.setEndValue(end)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
