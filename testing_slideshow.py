import tkinter as tk
from slideshow_video_player import VideoPlayer


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create button to start video player
        self.button = tk.Button(self.master, text="Start Video Player", command=self.start_video_player)
        self.button.pack()

    def start_video_player(self):
        self.player = VideoPlayer(self.master)
        self.player.play_video()


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    app.pack()
    root.mainloop()
