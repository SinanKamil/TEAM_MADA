import tkinter as tk
from tkinter import messagebox
import time

class Timer:
    def __init__(self, minutes, inactive_time, action):
        self.total_seconds = minutes * 60
        self.inactive_time = inactive_time
        self.action = action
        self.last_active_time = time.time()
        self.root = tk.Tk()
        self.root.title("Timer")
        self.root.geometry("250x100")
        self.label = tk.Label(self.root, font=("Arial", 20))
        self.label.pack(expand=True)
        self.root.bind('<Any-KeyPress>', self.reset_timer)
        self.root.bind('<Any-Button>', self.reset_timer)
        self.update_label()

    def reset_timer(self, event=None):
        self.last_active_time = time.time()

    def update_label(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_active_time
        remaining_time = self.total_seconds - elapsed_time
        if remaining_time <= 0:
            self.action()
            self.root.destroy()
        else:
            minutes, seconds = divmod(int(remaining_time), 60)
            self.label.configure(text="Time remaining: {:02d}:{:02d}".format(minutes, seconds))
            if elapsed_time > self.inactive_time:
                self.label.configure(foreground='red')
            else:
                self.label.configure(foreground='black')
            self.label.after(250, self.update_label)

    def start(self):
        self.update_label()
        self.root.mainloop()

# Example usage
def action():
    messagebox.showinfo("Timer", "Time's up!")

timer = Timer(minutes=2, inactive_time=10, action=action)
timer.start()
