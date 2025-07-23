import cv2

image = cv2.imread("module-3/image1.jpeg")

if image is not None:
    pt1 = (300, 600)
    pt2 = (600, 600)
    color = (0, 255, 0)
    thickness = 5
    cv2.line(image, pt1, pt2, color, thickness)
    cv2.imshow("Image with Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
