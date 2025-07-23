import cv2

image = cv2.imread("module-3/image1.jpeg")

if image is not None:
    pt1 = (350, 200)
    pt2 = (500, 500)
    color = (200, 200, 200)
    thickness = 3
    cv2.rectangle(image, pt1, pt2, color, thickness)
    cv2.imshow("Image with Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")