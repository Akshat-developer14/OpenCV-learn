import cv2

image = cv2.imread("module-2/python_image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded")

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    angle = 90
    scale = 1.0

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

