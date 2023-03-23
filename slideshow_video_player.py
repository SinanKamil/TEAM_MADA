import tkinter as tk
import cv2
from PIL import Image, ImageTk

class VideoPlayer(tk.Frame):

    def __init__(self):
        super().__init__()
        self.video_file = "/media/pi/SINAN'S USB/slideshow_video.mp4"
        self.playing = False
        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Create a canvas to hold the video frame
        self.canvas = tk.Canvas(self.master, width=screen_width, height=screen_height)
        self.canvas.pack()

        # Make the window full screen

    def bind_events(self):
        self.canvas.bind("<Button-1>", self.mouse_callback)
        self.canvas.bind("<Button>", self.mouse_callback)  # Stop video when any mouse button is clicked
        self.canvas.bind("<Motion>", self.mouse_callback)  # Stop video when mouse is moved

    def play_video(self):
        self.playing = True
        cap = cv2.VideoCapture(self.video_file)
        while self.playing:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Resize the frame to 1920x1080
            frame = cv2.resize(frame, (1920, 1080))
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo
            self.master.update()
        cap.release()
        # Destroy the VideoPlayer instance and its associated widgets
        self.destroy_video_page()

    def mouse_callback(self, event):
        self.playing = False

    def destroy_video_page(self):
        self.canvas.destroy()
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer()
    app.pack()
    app.play_video()
    root.mainloop()
