import cv2

image = cv2.imread("module-2/python_image.png")

if image is not None:
    cropped = image[130:775, 125:765]

    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
