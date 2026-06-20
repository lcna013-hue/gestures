
import tkinter as tk
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import time
root = tk.Tk()

root.title('Gesture Photo Capturer')
root.geometry('1500x800')

# Frames For All Elements
frame_title_photo_taken = tk.Frame(root)
frame_photo_taken_img = tk.Frame(root)
frame_save = tk.Frame(root)
frame_or = tk.Frame(root)
frame_delete = tk.Frame(root)

# HOME title placed in the upper center of the screen
frame_title_photo_taken.place(anchor="n", relx=.5, rely=.025)
title = tk.Label(frame_title_photo_taken, text="PHOTO TAKEN", font=("Aptos", 40), fg="blue2")
title.pack()

#Text asking user if they would like to save the photo that will be displayed to the left of the text
frame_save.place(relx=.6, rely=.20)
photo_taken_img = tk.Label(frame_save, text="""If you wish to keep 
this photo and move
on, show a thumbs 
upto the camera """, font=("Aptos", 24), highlightthickness = 4, highlightbackground = "limegreen")
photo_taken_img.pack(ipadx=10, ipady=15)

frame_or.place(relx=.68, rely=.50)
or_lbl = tk.Label(frame_or, text = "OR", font=("Aptos", 35))
or_lbl.pack()


frame_delete.place(relx=.6, rely=.65)
photo_delete=tk.Label(frame_delete, text="""If you would like
 to delete this photo 
 show a thumbs down 
 to the camera""", font=("Aptos", 24),highlightthickness=4, highlightbackground="red2")
photo_delete.pack(ipadx=10, ipady=15)




root.mainloop()