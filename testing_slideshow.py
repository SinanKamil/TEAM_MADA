import tkinter as tk
from slideshow_video_player import VideoPlayer


class GUI(tk.Frame):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        # Create button to start video player
        self.button = tk.Button(self.master, text="Start Video Player", command=self.start_video_player)
        self.button.pack()

    def start_video_player(self):
        self.button.pack_forget()  # Hide the button during video playback
        self.player = VideoPlayer()
        self.player.play_video()
        self.button.pack()  # Show the button again when video playback is finished


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI()
    app.pack()
    root.mainloop()
