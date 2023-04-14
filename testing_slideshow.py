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
        self.player = VideoPlayer()
        self.player.play_video()


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI()
    app.pack()
    root.mainloop()

# sudo apt-get update
# sudo apt-get install libatlas-base-dev libjasper-dev libqtgui4 python3-pyqt5 libqt4-test
# pip3 install opencv-python