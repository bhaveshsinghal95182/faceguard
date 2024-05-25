import cv2
import threading
import tkinter as tk
from deepface import DeepFace
from deepface.basemodels import VGGFace
from tkinter import simpledialog, messagebox

# Load facial recognition model
vgg_model = VGGFace.load_model()

# start the screen capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# set passwords and references
correct_password = "123"
reference_img = cv2.imread("assetss\\reference.jpg")

counter = 0
face_match = False

# Checking for face
def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, reference_img, model_name="VGG-Face")
        face_match = result['verified']
    except ValueError:
        face_match = False

# Check for correct password
# def prompt_password():
    # root = tk.Tk()
    # root.withdraw()  # Hide the root window
    # password_correct = True
    # loop = True
    # while loop:
    #     entered_password = simpledialog.askstring("Password Required", "Enter the password to unlock:", show='*')
    #     if entered_password == correct_password:
    #         loop = False
    #         return password_correct
        
    #     else:
    #         messagebox.showerror("Access Denied", "Incorrect password. Try again.")

    # root.destroy()  # Close the password prompt window


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
    root.update()

    root = tk.Tk()
    root.withdraw()  # Hide the root window
    password_correct = False

    while True:
        ret, frame = cap.read()
        
        cv2.imshow('captured video', frame)
        
        if ret:
            if counter % 30 == 0:
                try:
                    threading.Thread(target=check_face, args=(frame.copy(),)).start()
                except ValueError:
                    pass
            counter += 1

            entered_password = simpledialog.askstring("Password Required", "Enter the password to unlock:", show='*')
            if entered_password == correct_password:
                password_correct = True
        
            else:
                messagebox.showerror("Access Denied", "Incorrect password. Try again.")

            
            if face_match or correct_password:
                cv2.putText(frame, "Access Granted", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                break
            else:
                cv2.putText(frame, "Access Denied", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cap.release()
    cv2.destroyAllWindows()
    root.destroy()