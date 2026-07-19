### IMPORTS HERE ###
import tkinter as tk 
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



count = 0
# placeholder for number of books
h=2

#*************
# Functions:
#*************

def display_result(result: vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int, ):
   
    if not result.gestures:
        return
    gesture = result.gestures[0][0]
    # on = True
    # off = False

    # home_page_showing = on
    # photo_taken_page_showing = off
    # book_saved_page_showing = off
    # photo_deleted_page_showing = off
    # quantity_page_showing = off
    # take_another_page_showing = off

    global count
    #print(gesture.category_name)
    name = gesture.category_name.strip().lower()
    print("Gesture:", name, "Count:", count)

    if "thumb" in name and "up" in name and count == 0:
        # home_page_showing == off
        # photo_taken_page_showing == on
        
        count = 1
        screen_1_hide()
        screen_2_show()
        

        # print(result.gesture)
        image = Image.fromarray(output_image.numpy_view())
        image.save("file.jpg")
      
        # print(gesture.name)
        
    if "victory" in name and count == 1:
        screen_2_hide()
        screen_3_show()




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

def screen_1_show():
    title.pack()
    start_date_lbl.pack(ipadx=15, ipady=15)
    pinch_img3.pack()

def screen_1_hide():
    frame_title_home.place_forget()
    frame_pinch_img.place_forget()
    frame_instructions.place_forget()
    frame_text2.place_forget()


def screen_2_show():
    title_photo_taken.pack()
    photo_taken_img.pack(ipadx=10, ipady=15)
    or_lbl.pack()
    photo_delete.pack(ipadx=10, ipady=15)

def screen_2_hide():
    frame_title_photo_taken.place_forget()
    frame_photo_taken_img.place_forget()
    frame_save.place_forget()
    frame_or.place_forget()
    frame_delete.place_forget()


def screen_3_show():
    title_book_saved.pack()
    add_lbl.pack(ipadx=10, ipady=30)
    error_lbl.pack(ipadx=15, ipady=12)
    book_add.pack(ipadx=12, ipady=8)
    hand_img.pack(ipadx=8, ipady=18)
    book_photo.pack(ipadx=170, ipady=240)


### MAIN CODE ###

# ******************************************
#       START OF HOME SCREEN GUI
# ******************************************


root = tk.Tk()
root.title("Gesture Photo Capturer")
root.geometry('1500x800')

# How to know which page is on so the gesture can only do somtehing for the correct page
home_page_showing = True
photo_taken_page_showing = False
book_saved_page_showing = False
photo_deleted_page_showing = False
quantity_page_showing = False
take_another_page_showing = False

#***************************
# For home screen set up GUI
#***************************

# Frames for home screen
frame_title_home = tk.Frame(root)
frame_pinch_img = tk.Frame(root)
frame_instructions = tk.Frame(root)
frame_text2 = tk.Frame(root)


#Image resizing and positioning 
frame_pinch_img.place(anchor="n", relx=.7, rely=.4) 
# Opens image
pinching_img = Image.open("pinch_gesutre_img.png")
# # Resizes image
pinch_img = pinching_img.resize((300, 400))
pinch_img2 = ImageTk.PhotoImage(pinch_img)
pinch_img3 = tk.Label(frame_pinch_img, image=pinch_img2, highlightthickness=4, highlightbackground="limegreen")


# Title for home screen
frame_title_home.place(anchor="n", relx=.5, rely=.025)
title = tk.Label(frame_title_home, text="HOME", font=("Aptos", 40), fg="blue2")


#  text intuructions for home screen
frame_instructions.place(anchor="se", rely=.35, relx=.94)
start_date_lbl = tk.Label(frame_instructions, text="""To take a photo, make a pinching 
gesutre with your hand, 
like seen below ⬇""", font=("Aptos", 24), highlightthickness = 4, highlightbackground = "dodgerblue2")

# Call function at the start to begin by showing the home screen
screen_1_show()


# ******************************************
# END OF HOME SCREEN GUI (screen 1)
# ******************************************

# ******************************************
# START OF PHOTO GUI (screen 2)
# ******************************************
frame_title_photo_taken = tk.Frame(root)
frame_photo_taken_img = tk.Frame(root)
frame_save = tk.Frame(root)
frame_or = tk.Frame(root)
frame_delete = tk.Frame(root)


#lable geometry:
frame_title_photo_taken.place(anchor="n", relx=.5, rely=.025)
title_photo_taken = tk.Label(frame_title_photo_taken, text="PHOTO TAKEN", font=("Aptos", 40), fg="blue2")

frame_save.place(relx=.6, rely=.20)
photo_taken_img = tk.Label(frame_save, text="""If you wish to keep \n this photo and move \n on, show a thumbs \n upto the camera """, 
font=("Aptos", 24), highlightthickness = 4, highlightbackground = "limegreen")

frame_or.place(relx=.68, rely=.5)
or_lbl = tk.Label(frame_or, text = "OR", font=("Aptos", 35))

frame_delete.place(relx=.6, rely=.65)
photo_delete=tk.Label(frame_delete, text="""If you would like \n to delete this photo \n show a thumbs down \n to the camera""", 
font=("Aptos", 24),highlightthickness=4, highlightbackground="red2")


label_widget = tk.Label(root)
label_widget.place(rely=.2, relx=.1)

label_img = Image



# ******************************************
# END OF PHOTO GUI (screen 2)
# ******************************************

# ******************************************
# START OF PHOTO GUI (screen 3)
# ******************************************

frame_title = tk.Frame(root)
frame_book_img = tk.Frame(root)
frame_books_added = tk.Frame(root)
frame_error = tk.Frame(root)
frame_add = tk.Frame(root)
frame_add_another = tk.Frame(root)
frame_hand_img = tk.Frame(root)



frame_title.place(anchor="n", relx=.5, rely=.025)
title_book_saved = tk.Label(frame_title, text="BOOK SAVED", font=("Aptos", 40), fg="blue2")


frame_add.place(relx=.39, rely=.25)
add_lbl = tk.Label(frame_add, text=f"You have added {h} of these \n books into the database", font=("Aptos", 24), highlightthickness=4, highlightbackground="dodgerblue2")


frame_error.place(relx=.4, rely=.55)
error_lbl = tk.Label(frame_error, text="If there was an error, \n please change details in \n the database within the \n next 30 minutes", font=("Aptos", 24), highlightthickness=4, highlightbackground="dodgerblue2")


frame_add_another.place(relx=.7, rely=.4)
book_add=tk.Label(frame_add_another, highlightthickness=4, highlightbackground="dodgerblue2",  font=("Aptos", 24), text="If you would like to add \n another book, make an \n L shape with your hand")


frame_hand_img.place(relx=.76, rely=.67)
hand_img=tk.Label(frame_hand_img, highlightthickness=4, highlightbackground="dodgerblue2", font=("Aptos", 24), text="**Add gesture \n img**" )


frame_book_img.place(relx=.04, rely=.2)
book_photo=tk.Label(frame_book_img, highlightthickness=4, highlightbackground="dodgerblue2", text="***ADD IMAGE HERE***")


open_camera()

### Rest of the code ###
home_page = False
photo_take_page = False
quantity_page = False
book_saved_page = False
photo_deleted_page = False

root.mainloop()
