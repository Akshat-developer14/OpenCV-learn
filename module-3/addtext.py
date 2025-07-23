import cv2

image = cv2.imread("module-3/image1.jpeg")

if image is not None:
    text = 'Bonjour, python et opencv!'
    org = (300, 450)
    font = cv2.FONT_ITALIC
    fontScale = 1
    color = (225, 255, 184)
    thickness = 2
    cv2.putText(image, text, org, font, fontScale, color, thickness)

    cv2.imshow("Adding text to image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")