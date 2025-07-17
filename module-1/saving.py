import cv2

image = cv2.imread("module-1\python_image.png")

if image is not None:
    success = cv2.imwrite("output_image.png", image)
    if success:
        print("Image saved successfully.")
    else:
        print("Failed to save image.")
else:
    print("Error: Image not loaded.")
