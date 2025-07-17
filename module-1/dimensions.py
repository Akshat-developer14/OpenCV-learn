import cv2

image = cv2.imread("module-1/python_image.png")

if image is not None:
    h, w, c = image.shape
    print(f"Image loaded: \n Height: {h} \n Width: {w} \n Channels: {c}")
else:
    print("Image not found")