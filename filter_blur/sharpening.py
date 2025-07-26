import cv2
import numpy as np

image = cv2.imread("filter_blur/image.jpg")

if image is not None:
    sharpening_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
        ])
    
    ddepth = -1

    sharpened = cv2.filter2D(image, ddepth, sharpening_kernel)

    cv2.imshow("Original Image", image)
    cv2.imshow("Sharpened Image", sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")