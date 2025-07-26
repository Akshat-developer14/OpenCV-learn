"""
1- cv2.bitwise_and(image1, image2)
2- cv2.bitwise_or(image1, image2)
3- cv2.bitwise_not(image)


* img1, img2 should be of same size.
* use only black and white images.
"""

import cv2
import numpy as np

image1 = np.zeros((300, 300), dtype="uint8")
image2 = np.zeros((300, 300), dtype="uint8")

cv2.circle(image1, (150, 150), 100, 255, -1)

cv2.rectangle(image2, (100, 100), (250, 250), 255, -1)

bitwise_and = cv2.bitwise_and(image1, image2)
bitwise_or = cv2.bitwise_or(image1, image2)
bitwise_not = cv2.bitwise_not(image1)

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()