import cv2
import threading
from deepface import DeepFace
from deepface.basemodels import VGGFace

vgg_model = VGGFace.load_model()

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

reference_img = cv2.imread("assetss\\reference.jpg")

def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, reference_img, model_name="VGG-Face")
        face_match = result['verified']
    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()
    
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "Access Granted", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "Access Denied", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow('captured video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
