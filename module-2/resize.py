import cv2

image = cv2.imread("module-2/python_image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded")

    resized = cv2.resize(image, (300, 300))

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized)

    cv2.imwrite("module-2/resized_image.png", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
