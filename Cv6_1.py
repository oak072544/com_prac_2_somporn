import cv2
import numpy as np

# Load the image file
img = cv2.imread('/home/pi/Downloads/kuytu')

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the lower and upper ranges for red color
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

# Create a binary mask for red color
mask = cv2.inRange(hsv, lower_red, upper_red) + cv2.inRange(hsv, lower_red2, upper_red2)

# Apply the mask to the original image
filtered_img = cv2.bitwise_and(img, img, mask=mask)

# Display the original and filtered images
cv2.imshow('original image', img)
cv2.imshow('filtered image', filtered_img)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
