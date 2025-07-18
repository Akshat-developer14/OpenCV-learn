import cv2

image = cv2.imread("module-2/python_logo.png")

if image is not None:
    flipped_horizontally = cv2.flip(image, 1)
    flipped_vertically = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Flipped Horizontally Image", flipped_horizontally)
    cv2.imshow("Flipped Vertically Image", flipped_vertically)
    cv2.imshow("Flipped Both Image", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
