import cv2
import numpy as np

# Load the image file
img = cv2.imread('/home/pi/Downloads/kuytu')

# Define the lower and upper ranges for green color
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

# Define the lower and upper ranges for blue color
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create binary masks for green and blue colors
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# Combine the masks using bitwise OR operation
mask = cv2.bitwise_or(mask_green, mask_blue)

# Apply the mask to the original image
filtered_img = cv2.bitwise_and(img, img, mask=mask)

# Display the original and filtered images
cv2.imshow('original image', img)
cv2.imshow('filtered image', filtered_img)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
