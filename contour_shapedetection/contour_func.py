import cv2

image_path = "contour_shapedetection/shapes.png"

image = cv2.imread(image_path)

if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        corners = len(approx)

        if corners == 3:
            shape = "Triangle"
        elif corners == 4:
            shape = "Rectangle"
        elif corners == 5:
            shape = "Pentagon"
        elif corners == 6:
            shape = "Hexagon"
        elif corners > 6:
            shape = "Circle"
        else:
            shape = "Unknown"

        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 10

        cv2.putText(image, shape, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 200), 1)

    cv2.imshow("Contours", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
