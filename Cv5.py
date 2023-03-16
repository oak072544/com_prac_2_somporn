import cv2

# Open the video file
cap = cv2.VideoCapture('/home/pi/Downloads/SUs.mp4')

# Set the current position of the video to 7 seconds
cap.set(cv2.CAP_PROP_POS_MSEC, 5000)

# Read the current frame
ret, frame = cap.read()

# Check if the frame was successfully read
if ret:
    # Display the frame
    cv2.imshow('frame', frame)

    # Save the frame as an image file
    cv2.imwrite('captured_image.jpg', frame)

    # Wait for a key press and then exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Release the VideoCapture object
cap.release()