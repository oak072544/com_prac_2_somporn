import cv2

# Load the image file
img = cv2.imread('/home/pi/Downloads/kuytu')

# Get the original dimensions of the image
height, width = img.shape[:2]

# Shrink the image by a factor of 2
new_width = int(width / 2)
new_height = int(height / 2)
shrunk_img = cv2.resize(img, (new_width, new_height))

# Display the original and the shrunk images
cv2.imshow('original image', img)
cv2.imshow('shrunk image', shrunk_img)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
