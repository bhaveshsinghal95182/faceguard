import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    frame = cv2.resize(frame, (1800,800))

    img = cv2.line(frame, (0, 0), (width, height), (0,0,255), 10)
    img = cv2.line(img, (0, height), (width, 0), (0,0,255), 10)
    img = cv2.rectangle(frame, (width//2 + 100, height//2 + 100), (width//2 - 100, height//2 -100), (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'The great Bhavesh', (10, height-10), font, 2, color=(0,0,0), thickness=1, lineType=cv2.LINE_AA)

    cv2.imshow('captured video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()