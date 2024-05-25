import cv2
import threading
import tkinter as tk
from deepface import DeepFace
from dialoguebox import DialogueBox
from deepface.basemodels import VGGFace
from tkinter import simpledialog, messagebox

# Load facial recognition model
vgg_model = VGGFace.load_model()

# Set passwords and references
correct_password = "123"
reference_img = cv2.imread("assetss\\reference.jpg")

# Flags for verification
face_match = False
password_correct = False

# Function to check the face against the reference image
def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, reference_img, model_name="VGG-Face")
        face_match = result['verified']
    except ValueError:
        face_match = False

# Function to start and capture video
def start_video():
    global face_match
    counter = 0
    loop = True
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while loop:
        ret, frame = cap.read()
        if ret:
            if counter % 30 == 0:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            counter += 1

            if face_match:
                cv2.putText(frame, "Access Granted", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                loop = False
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Access Granted", "Face verification successful.")
                return True
            else:
                cv2.putText(frame, "Access Denied", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

            cv2.imshow('captured video', frame)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

# Function to prompt for password
def prompt_password():
    global password_correct
    while not password_correct:
        entered_password = simpledialog.askstring("Password Required", "Enter the password to unlock:", show='*')
        if entered_password == correct_password:
            messagebox.showinfo("Access Granted", "Password verification successful.")
            password_correct = True
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Try again.")

# Function to show the main dialog box
# def dialog_box():
#     root = tk.Tk()
#     root.title("Face and Password Verification")
#     root.geometry("300x200")

#     password_button = tk.Button(root, text="Enter Password", command=prompt_password)
#     password_button.pack(pady=20)

#     video_button = tk.Button(root, text="Start Video Verification", command=start_video)
#     video_button.pack(pady=20)

#     root.update()


# Main entry point of the application
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
    dialogue_box = DialogueBox(prompt_password, start_video)
    if face_match or password_correct:
        dialogue_box.close_window()
    root.destroy()
