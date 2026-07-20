from tkinter import Tk, Label
from PIL import Image, ImageTk

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import time

vid = cv2.VideoCapture(0)
width, height = 800, 600

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def display_result(
    result: vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int
):
    print(result.gestures)
    image = Image.fromarray(output_image.numpy_view())
    image.save("file.jpg")


base_options = python.BaseOptions(model_asset_path="gesture_recognizer.task")
options = vision.GestureRecognizerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.LIVE_STREAM,
    result_callback=display_result,
)
recognizer = vision.GestureRecognizer.create_from_options(options)

def open_camera():
    _, frame = vid.read()
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=opencv_image)
    recognizer.recognize_async(mp_image, time.time_ns()//1000)

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