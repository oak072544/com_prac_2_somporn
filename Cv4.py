import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('/home/pi/Downloads/SUs.mp4')

# Loop over frames in the video
while cap.isOpened():
    # Read the current frame
    ret, frame = cap.read()
    
    # Check if the frame was successfully read
    if not ret:
        break
    
    # Display the frame
    cv2.imshow('frame', frame)
    
    # Wait for a key press and then exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
