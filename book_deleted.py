
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk

def hide_label():
    # This will remove the widget
    frame_title.place_forget()
    frame_deleted.place_forget()
    frame_hand_img.place_forget()
    frame_take_another.place_forget()



h = "2"
root = tk.Tk()
root.title("Gesture Photo Capturer")
root.geometry('1500x800')

frame_title = tk.Frame(root)
frame_deleted = tk.Frame(root)
frame_hand_img = tk.Frame(root)
frame_take_another = tk.Frame(root)

frame_title.place(anchor="n", relx=.5, rely=.025)
title = tk.Label(frame_title, 
text="PHOTO DELTETED", 
font=("Aptos", 40), 
fg="blue2")
title.pack()

frame_deleted.place(relx=.30, rely=.2)
photo_deleted = tk.Label(frame_deleted, 
font=("Aptos", 24), text="Your photo has been deleted", 
highlightthickness=4, highlightbackground="dodgerblue2")
photo_deleted.pack(ipadx=80, ipady=30)

frame_take_another.place(anchor="n", relx=.48, rely=.4)
take_another = tk.Label(frame_take_another, 
font=("Aptos", 24), 
text="If you wish to take \n another photo, show an \n open palm to return \n to the home screen",
highlightthickness=4, highlightbackground="dodgerblue2")
take_another.pack(ipadx=15, ipady=15)

frame_hand_img.place(anchor="n", relx=.07) 
# Opens image
pinching_img = Image.open("L_shape_img.png")
# Resizes image
L_shape_img = pinching_img.resize((150, 200))
img = ImageTk.PhotoImage(L_shape_img)



forget_btn = Button(root, text="Click to clear screen", command=hide_label)
forget_btn.pack()


root.mainloop()