import cv2

image = cv2.imread("module-1\python_image.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")