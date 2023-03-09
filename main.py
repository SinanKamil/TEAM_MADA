import tkinter as tk

class ExampleApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create the button image
        self.switch_button_img = tk.PhotoImage(file="btn_images/Alternator.png")

        # Create the button widget
        self.switch_button = tk.Button(self, image=self.switch_button_img, command=self.toggle_switch)
        self.switch_button.pack()

    def toggle_switch(self):
        # Toggle the button state between normal and disabled
        if self.switch_button.config('state')[-1] == "normal":
            self.switch_button.config(state="disabled")
            print("OFFFF")
        else:
            self.switch_button.config(state="normal")

root = tk.Tk()
app = ExampleApp(master=root)
app.mainloop()
