import cv2

image = cv2.imread("02.jpg")

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inverted_image = cv2.bitwise_not(grey_image)

blurred_image = cv2.GaussianBlur(inverted_image, (55, 55), 0)

inverted_blurred_image = cv2.bitwise_not(blurred_image)

sketch = cv2.divide(grey_image, inverted_blurred_image, scale=256.0)

cv2.imshow("Sketch", sketch)
cv2.imwrite("sketch.png", sketch)

cv2.waitKey(0)
