import cv2
import numpy as np


def remove_whitespace(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold to get binary image
    bit = cv2.bitwise_not(gray)
    _, thresh = cv2.adaptiveThreshold(bit, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 35, 15)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    # Get bounding box of the largest contour
    x, y, w, h = cv2.boundingRect(max_contour)

    # Crop the image based on bounding box
    cropped_image = image[y:y + h, x:x + w]

    return cropped_image


# Read input image
input_image = cv2.imread('image3.png')

# Remove whitespace
cropped_image = remove_whitespace(input_image)

# Display cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
