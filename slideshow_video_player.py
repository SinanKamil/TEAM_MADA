import cv2


def play_video():
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture("/home/pi/Desktop/GA_Video.mp4")

    # Reduce the resolution to 720p
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

    # Reduce the frame rate to 30 fps
    cap.set(cv2.CAP_PROP_FPS, 30)

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error opening video file")

    # Create a window with full screen size
    cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Function to handle mouse click events
    def mouse_callback(event, x, y, flags, param):
        # Exit video playback if right mouse button is pressed on video window
        if event == cv2.EVENT_RBUTTONDOWN:
            cap.release()

    # Register mouse click event callback
    cv2.setMouseCallback('Frame', mouse_callback)

    # Read until video is completed
    while cap.isOpened():

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q or X on keyboard to exit
            key = cv2.waitKey(25)
            if key & 0xFF == ord('q') or key == 27 or key == ord('x'):
                break

        # If the video is finished, set the position to the beginning
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

