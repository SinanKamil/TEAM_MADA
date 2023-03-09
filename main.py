import tkinter as tk

def exit_gui():
    root.destroy()

root = tk.Tk()

# create some widgets...

exit_button = tk.Button(root, text="Exit", command=exit_gui)
exit_button.pack()

root.mainloop()
