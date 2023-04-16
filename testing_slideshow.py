import cv2

# Open the video file
cap = cv2.VideoCapture("/media/pi/SINAN'S USB/slideshow_video.mp4")

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Loop through the frames of the video
while cap.isOpened():
    # Read the next frame of the video
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Wait for a key press to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video file and close all windows
cap.release()
cv2.destroyAllWindows()
