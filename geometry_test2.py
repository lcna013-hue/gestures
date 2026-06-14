import tkinter
from tkinter import Image
from tkinter import Label
from tkinter import PhotoImage

import PIL
from PIL import Image, ImageTk

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


frame_title_home.place(anchor="n", relx=.5, rely=.025)
title = tkinter.Label(frame_title_home, text="HOME", font=("Aptos", 40))

#colour , fg="blue2

#  box:  highlightthickness = 4, highlightbackground = "blue2"

title.pack()

frame_fields.place(anchor="se", rely=.35, relx=.94)
start_date_lbl = tkinter.Label(frame_fields, text="""To take a photo, make a pinching 
gesutre with your hand, 
like seen below ⬇""", font=("Aptos", 24))
start_date_lbl.pack()

frame_text2.place(rely=.2, relx=.1)
text_2_lbl = tkinter.Label(frame_text2, text="""                                                                







*** CAMERA ***






""", font=("Aptos", 20), highlightthickness = 4, highlightbackground = "black")
text_2_lbl.pack()

label_img = Image

label = Label(image=img)
#label.pinching_img = img
#Image posistions 
label.place(anchor="e", relx=.9, rely=.7)

root.mainloop()
