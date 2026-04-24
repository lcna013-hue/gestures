from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

vid = cv2.VideoCapture(0)
width, height = 800, 600

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def open_camera():
    _, frame = vid.read()

    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    captured_image = Image.fromarray(opencv_image)

    photo_image = ImageTk.PhotoImage(image=captured_image)
    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)
    label_widget.after(10, open_camera)

app = Tk()
app.bind("<Escape>", lambda e: app.quit())

label_widget = Label(app)
label_widget.pack()

open_camera()

app.mainloop()