import cv2
import threading
import tkinter as tk
from deepface import DeepFace
from deepface.basemodels import VGGFace
from tkinter import simpledialog, messagebox

# Load facial recognition model
vgg_model = VGGFace.load_model()

# Start the screen capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set passwords and references
correct_password = "123"
reference_img = cv2.imread("assetss\\reference.jpg")

# Global variable to track if access is granted
access_granted = False
counter = 0

# Function to check for face match
def check_face(frame):
    global access_granted
    try:
        result = DeepFace.verify(frame, reference_img, model_name="VGG-Face")
        if result['verified']:
            access_granted = True
    except ValueError:
        pass

# Function to prompt for password
def prompt_password():
    global access_granted
    while not access_granted:
        entered_password = simpledialog.askstring("Password Required", "Enter the password to unlock:", show='*')
        if entered_password == correct_password:
            access_granted = True
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Try again.")

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
    root.withdraw()  # Hide the root window

    # Start the password prompt in a separate thread
    password_thread = threading.Thread(target=prompt_password)
    password_thread.start()

    while not access_granted:
        ret, frame = cap.read()
        if ret:
            if counter % 30 == 0:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            counter += 1

            if access_granted:
                cv2.putText(frame, "Access Granted", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, "Access Denied", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

            cv2.imshow('Video Feed', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    root.destroy()
    messagebox.showinfo("Access Granted", "You have unlocked the system.")
