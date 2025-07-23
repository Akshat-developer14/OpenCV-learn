import cv2

image = cv2.imread("module-3/image1.jpeg")

if image is not None:
    center = (430, 350)
    radius = 150
    color = (0, 0, 255)
    thickness = 3
    cv2.circle(image, center, radius, color, thickness)
    cv2.circle(image, (850, 70), 40, (128, 224, 255), -1)

    cv2.imshow("Image with Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")