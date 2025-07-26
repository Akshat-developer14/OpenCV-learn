import cv2

image = cv2.imread("edgedetection_thresholding/flower.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:
    edges = cv2.Canny(image, 50, 150)

    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Detection", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")

