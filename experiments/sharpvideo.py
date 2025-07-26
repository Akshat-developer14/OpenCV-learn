import cv2
import numpy as np
import time
import datetime

# Initialize video capture
cap = cv2.VideoCapture(0)

# Static sharpening kernel
sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

ddepth = -1
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Apply sharpening filter
    sharpened_frame = cv2.filter2D(frame, ddepth, sharpening_kernel)

    # Calculate FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Get timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Overlay diagnostics on the frame
    cv2.putText(sharpened_frame, f"Time: {timestamp}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(sharpened_frame, f"FPS: {fps:.2f}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    # Display the sharpened frame
    cv2.imshow("Webcam", sharpened_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Exiting...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
