import cv2

# Load the image file
img = cv2.imread('/home/pi/Downloads/kuytu')

# Flip the image vertically
flipped_img = cv2.flip(img, 1)

# Display the original and the flipped images
cv2.imshow('original image', img)
cv2.imshow('flipped image', flipped_img)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
