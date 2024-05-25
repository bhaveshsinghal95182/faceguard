import tkinter as tk
from tkinter import simpledialog, messagebox
import getpass

# Set the correct password
correct_password = "123"

def prompt_password():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    while True:
        entered_password = simpledialog.askstring("Password Required", "Enter the password to unlock:", show='*')
        if entered_password == correct_password:
            break
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Try again.")

    root.destroy()  # Close the password prompt window

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
    root.update()
    prompt_password()
    root.destroy()
