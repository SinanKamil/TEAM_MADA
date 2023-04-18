import subprocess

def play_video_vlc(video_file_path):
    # Define the command to launch VLC with the video file
    vlc_cmd = ["vlc", "-f", video_file_path]

    # Launch VLC with the video file
    vlc_process = subprocess.Popen(vlc_cmd)

    # Wait for VLC to finish playing the video
    vlc_process.wait()

# Call the function with the path to the video file as an argument
video_file_path = "/path/to/video/file.mp4"
play_video_vlc(video_file_path)
