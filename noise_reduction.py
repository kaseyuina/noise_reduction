import cv2

# Reading image file
image = cv2.imread('.\images\image.jpg')

# Converts to gray scalse
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying median filter
median = cv2.medianBlur(gray, 5)

# Displaying the output image
cv2.imshow('Median Image', median)
cv2.waitKey(0)
cv2.destroyAllWindows()