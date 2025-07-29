import cv2

face_cascade = cv2.CascadeClassifier("faceandobjectdetection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("faceandobjectdetection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("faceandobjectdetection/haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    roi_gray = gray[y:y + h, x:x + w]
    roi_color = frame[y:y + h, x:x + w]
    # roi = region of interest

    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(eyes) > 0:
        cv2.putText(frame, "Eyes detected", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(smiles) > 0:
        cv2.putText(frame, "Smile detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
