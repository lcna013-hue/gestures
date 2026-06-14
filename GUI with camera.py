import tkinter
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import time

#*****************
# CAMERA SET UP
#*****************

vid = cv2.VideoCapture(0)
width, height = 800, 600

vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


# Functions:

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

    captured_image = Image.fromarray(opencv_image)

    photo_image = ImageTk.PhotoImage(image=captured_image)
    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)
    label_widget.after(10, open_camera)




#****************************
#***** REST OF THE CODE******
#****************************



root = tkinter.Tk()

root.title('Gesture Photo Capturer ')
root.geometry('1500x800')

frame_title_home = tkinter.Frame(root)
frame_pinch_img = tkinter.Frame(root)
frame_fields = tkinter.Frame(root)
frame_text2 = tkinter.Frame(root)


def passx():
    pass

#
frame_pinch_img.place(anchor="n", relx=.07)
# Opens image
pinching_img = Image.open("pinch_gesutre_img.png")
# Resizes image
pinch_img = pinching_img.resize((300, 400))
img = ImageTk.PhotoImage(pinch_img)

# HOME title placed in the center 
frame_title_home.place(anchor="n", relx=.5, rely=.025)
title = tkinter.Label(frame_title_home, text="HOME", font=("Aptos", 40), fg="blue2")
title.pack()

frame_fields.place(anchor="se", rely=.35, relx=.94)
start_date_lbl = tkinter.Label(frame_fields, text="""To take a photo, make a pinching 
gesutre with your hand, 
like seen below ⬇""", font=("Aptos", 24), highlightthickness = 4, highlightbackground = "dodgerblue2")
start_date_lbl.pack(ipadx=15, ipady=15)



label_img = Image

label = Label(image=img, highlightthickness = 4, highlightbackground = "limegreen")
#label.pinching_img = img
#Image posistions 
label.place(anchor="e", relx=.9, rely=.7)


#**********************************
# ***** NEW CODE STARTS HERE *****
#**********************************


root.bind("<Escape>", lambda e: root.quit())

label_widget = Label(root)
label_widget.place(rely=.2, relx=.1)

open_camera()

root.mainloop()
