import tkinter as tk

class DialogueBox(tk.Tk):

    def __init__(self, prompt_password, start_video):
        super().__init__()
        self.title("Face and Password Verification")
        self.geometry("300x200")
        password_button = tk.Button(self, text="Enter Password", command=prompt_password)
        password_button.pack(pady=20)

        video_button = tk.Button(self, text="Start Video Verification", command=start_video)
        video_button.pack(pady=20)

        self.mainloop()

    def close_window(self):
        self.destroy()