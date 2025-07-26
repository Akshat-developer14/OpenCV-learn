import cv2

image = cv2.imread("edgedetection_thresholding/man.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:
    ret, thresh_img = cv2.threshold(image, 110, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original Image", image)
    cv2.imshow("Threshold Image", thresh_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")

