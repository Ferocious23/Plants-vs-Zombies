import sys
sys.path.append(r'C:\Users\bibym\AppData\Local\Programs\Python\Python311\lib\site-packages')
import cv2
import os
import numpy as np

# Load the field image and the template image of the tile
field_image = cv2.imread('AI_pictures\grass.png')
template_image = cv2.imread('AI_pictures\grassrect.png')

if field_image is None:
    print(f"Error loading field image: {field_image}")
    exit()

if template_image is None:
    print(f"Error loading template image: {template_image}")
    exit()


# Convert the template image to grayscale
template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

# Match the template using cv2.matchTemplate
result = cv2.matchTemplate(field_image, template_gray, cv2.TM_CCOEFF_NORMED)
threshold = 0.8  # You can adjust this threshold value

# Find locations where the template match exceeds the threshold
loc = np.where(result >= threshold)

# Highlight the matched tiles in the field image
for pt in zip(*loc[::-1]):
    bottom_right = (pt[0] + template_image.shape[1], pt[1] + template_image.shape[0])
    cv2.rectangle(field_image, pt, bottom_right, (0, 255, 0), 2)  # Green rectangle

# Save or display the image with highlighted tiles
cv2.imwrite('highlighted_image.png', field_image)
cv2.imshow('Highlighted Image', field_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
