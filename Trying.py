import tkinter as tk
from time import sleep
def on_button_press():
    for s in range(3):
        print("Button pressed and held", s)



def Disable():
    print("Disable")


root = tk.Tk()

button = tk.Button(root, text="Hold Button")
button.pack()

# Bind the ButtonPress and ButtonRelease events to the button
button.bind("<ButtonPress>", lambda event: on_button_press())
button.bind("<ButtonRelease>", lambda event: Disable())

root.mainloop()