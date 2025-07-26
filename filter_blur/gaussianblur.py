import cv2

image = cv2.imread("filter_blur/image.jpg")

if image is not None:
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")