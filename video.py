import cv2
import subprocess

def play_video_vlc():
    video_file_path = "/media/pi/SINAN'S USB/GA_SLIDESHOW/1906_SkyGuardian_UK_Beauty_Reel_060719.mp4"
    # Define the command to launch VLC with the video file
    vlc_cmd = ["vlc", "-f", video_file_path]

    # Launch VLC with the video file
    vlc_process = subprocess.Popen(vlc_cmd)

    # Define the mouse/touch event callback function
    def mouse_callback(event, x, y, flags, param):
        # Exit video playback if right mouse button is pressed or touch event is detected
        if event == cv2.EVENT_RBUTTONDOWN or event == cv2.EVENT_LBUTTONDOWN:
            vlc_process.terminate()

    # Register the mouse/touch event callback function
    cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Video Player', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback('Video Player', mouse_callback)

    # Wait for VLC to finish playing the video
    vlc_process.wait()

    # Clean up OpenCV windows
    cv2.destroyAllWindows()

# Call the function with the path to the video file as an argument
