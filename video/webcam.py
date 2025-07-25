import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame")
        break

    # Define text parameters
    text = "Bonjour, OpenCV et Python!"
    position = (50, 50)  # x, y coordinates
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 100, 230)  # Green
    thickness = 2

    # Add text to the frame
    cv2.putText(frame, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

    cv2.rectangle(frame, (200, 80), (500, 400), (0, 255, 0), 2)

    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
