import cv2

cap = cv2.VideoCapture(0)  # THIS IS MY WEBCAM

while cap.isOpened():
    ret, back = cap.read()  # READING FROM MY WEBCAM

    if ret:
        # ret is reading of webcam successful or not
        # back is what the camera is reading
        cv2.imshow('image', back)
        if cv2.waitKey(5) == ord('q'):
            # SAVE THE IMAGE
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
