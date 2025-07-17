import cv2

image = cv2.imread("module-1\python_image.png")

if image is not None:
    cv2.imshow("Image", image) # open's the window
    cv2.waitKey(0) # wait for a key to press
    cv2.destroyAllWindows() # close the window
else:
    print("Image not loaded.")