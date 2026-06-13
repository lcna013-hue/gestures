# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2

# Create an instance of TKinter Window or frame
win = Tk()
win.title("Webcam Display")

# Set the size of the window
win.geometry("700x350")

# Create a Label to capture the Video frames
label = Label(win)
label.grid(row=0, column=0)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define function to show frame
def show_frames():
    # Get the latest frame and convert into Image
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    # Repeat after an interval to capture continuously
    label.after(20, show_frames)

# Function to release resources when window is closed
def on_closing():
    cap.release()
    win.destroy()

# Bind the closing event
win.protocol("WM_DELETE_WINDOW", on_closing)

# Start capturing frames
show_frames()
win.mainloop()