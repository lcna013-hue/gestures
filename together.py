### IMPORTS HERE ###
from PIL.ImageFile import ImageFile
import tkinter as tk 
from PIL import Image, ImageTk

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision.gesture_recognizer import GestureRecognizer, GestureRecognizerOptions
from mediapipe.tasks.python.vision.hand_landmarker import HandLandmarker, HandLandmarkerOptions
from mediapipe.tasks.python.core.base_options import BaseOptions

import time
import math

from recognizers import count_fingers, recognize_victory, recognize_thumbs_up

 
# vid = cv2.VideoCapture(0)
# width, height = 800, 600

# vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)



# count = 0
# # placeholder for number of books
# h=2

# #*************
# # Functions:
# #*************

# def display_result(result: vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int, ):
   
#     if not result.gestures:
#         return
#     gesture = result.gestures[0][0]
#     # on = True
#     # off = False

#     # home_page_showing = on
#     # photo_taken_page_showing = off
#     # book_saved_page_showing = off
#     # photo_deleted_page_showing = off
#     # quantity_page_showing = off
#     # take_another_page_showing = off

#     global count
#     #print(gesture.category_name)
#     name = gesture.category_name.strip().lower()
#     print("Gesture:", name, "Count:", count)

#     if "thumb" in name and "up" in name and count == 0:
#         # home_page_showing == off
#         # photo_taken_page_showing == on
        
#         count = 1
#         screen_1_hide()
#         screen_2_show()
        

#         # print(result.gesture)
#         image = Image.fromarray(output_image.numpy_view())
#         image.save("file.jpg")
      
#         # print(gesture.name)
        
#     if "victory" in name and count == 1:
#         count = 3
#         screen_2_hide()
#         screen_3_show()

#     if "thumb" in name and "up" in name and count == 3:
#         screen_3_hide()





# base_options = python.BaseOptions(model_asset_path="gesture_recognizer.task")
# options = vision.GestureRecognizerOptions(
#     base_options=base_options,
#     running_mode=vision.RunningMode.LIVE_STREAM,
#     result_callback=display_result,
# )
# recognizer = vision.GestureRecognizer.create_from_options(options)

# def open_camera():
#     _, frame = vid.read()
#     opencv_image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
#     mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=opencv_image)
#     recognizer.recognize_async(mp_image, time.time_ns()//1000)

#     captured_image = Image.fromarray(opencv_image)

#     photo_image = ImageTk.PhotoImage(image=captured_image)
#     label_widget.photo_image = photo_image
#     label_widget.configure(image=photo_image)
#     label_widget.after(10, func=open_camera)



# GESTURE_RECOGNIZER_MODEL_PATH = "gesture_recognizer.task"
# HAND_LANDMARKER_MODEL_PATH = "hand_landmarker.task"

# def run():
#     base_options = BaseOptions(model_asset_path=GESTURE_RECOGNIZER_MODEL_PATH)
#     options = GestureRecognizerOptions(
#         base_options=base_options,
#         running_mode=vision.RunningMode.VIDEO,
#     )
#     gesture_recognizer = GestureRecognizer.create_from_options(options)

#     base_options = BaseOptions(
#         model_asset_path=HAND_LANDMARKER_MODEL_PATH
#     )
#     options = HandLandmarkerOptions(
#         base_options=base_options,
#         running_mode=vision.RunningMode.VIDEO,
#         num_hands=2,
#         min_hand_detection_confidence=0.5,
#         min_hand_presence_confidence=0.5,
#         min_tracking_confidence=0.5
#     )
#     hand_landmarker = HandLandmarker.create_from_options(options)

#     while True:
#         _, frame = vid.read()
#         opencv_image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#         mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=opencv_image)

#         gesture_result = gesture_recognizer.recognize_for_video(
#             mp_image,
#             time.time_ns()//1000
#         )
#         landmark_result = hand_landmarker.detect_for_video(
#             mp_image,
#             time.time_ns()//1000
#         )

#         finger_count = count_fingers(landmark_result)
#         is_victory = recognize_victory(gesture_result)
#         is_thumbs_up = recognize_thumbs_up(gesture_result)



# def screen_1_show():
#     title.pack()
#     start_date_lbl.pack(ipadx=15, ipady=15)
#     pinch_img3.pack()

# def screen_1_hide():
#     frame_title_home.place_forget()
#     frame_pinch_img.place_forget()
#     frame_instructions.place_forget()
#     frame_text2.place_forget()


# def screen_2_show():
#     title_photo_taken.pack()
#     photo_taken_img.pack(ipadx=10, ipady=15)
#     or_lbl.pack()
#     photo_delete.pack(ipadx=10, ipady=15)

# def screen_2_hide():
#     frame_title_photo_taken.place_forget()
#     frame_photo_taken_img.place_forget()
#     frame_save.place_forget()
#     frame_or.place_forget()
#     frame_delete.place_forget()


# def screen_3_show():
#     title_quantity.pack()
#     book_num.pack(ipadx=80, ipady=30)
#     num_fingers.pack(ipadx=15, ipady=15)

# def screen_3_hide():
#     frame_title_quantity.place_forget()
#     frame_how_many.place_forget()
#     frame_num_fingers.place_forget()
#     frame_hand_key_img.place_forget()
#     count_fingers()

# def calculate_distance(point1, point2):
#     #Distance between two points (MediaPipe landmarks) formula
#     return math.sqrt(
#         (point1.x - point2.x) ** 2 +
#         (point1.y - point2.y) ** 2 +
#         (point1.z - point2.z) ** 2
#     )


# def count_fingers_old():

# ##################################################
# # #all count fingers function show do it take in data and output num of fingers
# # # make seperate function to 
#     MODEL_PATH = "hand_landmarker.task"

#     base_options = python.BaseOptions(
#         model_asset_path=MODEL_PATH
#     )

#     options = vision.HandLandmarkerOptions(
#         base_options=base_options,
#         running_mode=vision.RunningMode.VIDEO,
#         num_hands=2,
#         min_hand_detection_confidence=0.5,
#         min_hand_presence_confidence=0.5,
#         min_tracking_confidence=0.5
#     )

#     hand_landmarker = vision.HandLandmarker.create_from_options(options)


#     #***************************
#     # Hand Landmark Connections
#     #***************************

#     HAND_CONNECTIONS = [
#         (0,1),(1,2),(2,3),(3,4),          # Thumb
#         (0,5),(5,6),(6,7),(7,8),          # Index
#         (5,9),(9,10),(10,11),(11,12),     # Middle
#         (9,13),(13,14),(14,15),(15,16),   # Ring
#         (13,17),(17,18),(18,19),(19,20),  # Pinky
#         (0,17)
#     ]
#     #***************************
#     # Landmark Indexes
#     #***************************

#     finger_tips = [8, 12, 16, 20]
#     finger_pips = [6, 10, 14, 18]

#     thumb_tip = 4
#     thumb_mcp = 2

#     #***************************
#     # Utility Functions
#     #***************************

#     def draw_hand(frame, landmarks):
#         """Draw hand landmarks using OpenCV
#         This is to replace 'mp.solutions.drawing_utils' becuase the newer versions of the mediapipe API do no include .solutions
#         """

#         height, width = frame.shape[:2]

#         # Draw bones
#         for start, end in HAND_CONNECTIONS:

#             x1 = int(landmarks[start].x * width)
#             y1 = int(landmarks[start].y * height)

#             x2 = int(landmarks[end].x * width)
#             y2 = int(landmarks[end].y * height)

#             cv2.line(
#                 frame,
#                 (x1, y1),
#                 (x2, y2),
#                 (255, 0, 0),
#                 2
#             )

#         # Draw joints
#         for landmark in landmarks:

#             x = int(landmark.x * width)
#             y = int(landmark.y * height)

#             cv2.circle(
#                 frame,
#                 (x, y),
#                 5,
#                 (0, 255, 0),
#                 -1
#             )

#     #***************************
#     # Open Webcam
#     #***************************

#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Error: Could not open webcam")
#         exit()

#     #***************************
#     # Main Loop
#     #***************************

#     while cap.isOpened():

#         success, frame = cap.read()

#         if not success:
#             break

#         # Mirror image
#         frame = cv2.flip(frame, 1)

#         # Convert OpenCV image -> MediaPipe Image

#         rgb_frame = cv2.cvtColor(
#             frame,
#             cv2.COLOR_BGR2RGB
#         )

#         mp_image = mp.Image(
#             image_format=mp.ImageFormat.SRGB,
#             data=rgb_frame
#         )

#         timestamp = int(time.time() * 1000)

#         # Run MediaPipe Tasks inference

#         results = hand_landmarker.detect_for_video(
#             mp_image,
#             timestamp
#         )

#         left_finger_count = 0
#         right_finger_count = 0

       
#         #***************************
#         # Process detected hands
#         #***************************

#         if results.hand_landmarks:

#             for landmarks, handedness in zip(
#                 results.hand_landmarks,
#                 results.handedness
#             ):

#                 # Get Left / Right label
#                 label = handedness[0].category_name

#                 is_left = label == "Left"

#                 # Draw hand skeleton
#                 draw_hand(frame, landmarks)

#                 #***************************
#                 # Finger counting
#                 #***************************

#                 finger_count = 0

#                 # Thumb detection
#                 if is_left:

#                     thumb_up = (
#                         landmarks[thumb_tip].x >
#                         landmarks[thumb_mcp].x
#                     )

#                 else:

#                     thumb_up = (
#                         landmarks[thumb_tip].x <
#                         landmarks[thumb_mcp].x
#                     )


#                 if thumb_up:
#                     finger_count += 1


#                 # Other four fingers
#                 for tip, pip in zip(
#                     finger_tips,
#                     finger_pips
#                 ):

#                     if landmarks[tip].y < landmarks[pip].y:
#                         finger_count += 1



#                 if is_left:

#                     left_finger_count = finger_count

#                 else:

#                     right_finger_count = finger_count
                    


#         #***************************
#         # Display Results
#         #***************************
#         total_count = left_finger_count + right_finger_count
#         cv2.putText(
#             frame,
#             f"Total Book:{total_count}",
#             (10, 35),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.7,
#             (0,255,0),
#             2
#         )


#         window_name = "MediaPipe Tasks Hand Tracking"

#         #***************************
#         # Show Camera Feed
#         #***************************

#         cv2.imshow(
#             "MediaPipe Tasks Hand Tracking",
#             frame
#         )
#         count_finger_lbl=

#         # Click the x to close window
#         if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
#             break


#     cap.release()

#     cv2.destroyAllWindows()

#     hand_landmarker.close()


# def screen_4_show():
#     title_book_saved.pack()
#     add_lbl.pack(ipadx=10, ipady=30)
#     error_lbl.pack(ipadx=15, ipady=12)
#     book_add.pack(ipadx=12, ipady=8)
#     hand_img.pack(ipadx=8, ipady=18)
#     book_photo.pack(ipadx=170, ipady=240)


# ### MAIN CODE ###

# # ******************************************
# #       START OF HOME SCREEN GUI
# # ******************************************

class HomePage(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(parent)

        pinching_image_file = Image.open("pinch_gesutre_img.png")
        pinching_image_file.resize((300, 400))
        pinching_image = ImageTk.PhotoImage(pinching_image_file)
        pinching_image_label = tk.Label(self, image=pinching_image, highlightthickness=4, highlightbackground="limegreen")
        pinching_image_label.pack()

        title_label = tk.Label(self, text="HOME", font=("Aptos", 40), fg="blue2")
        title_label.pack()

        instructions_label = tk.Label(self, text=
        """To take a photo, make a pinching 
        gesutre with your hand, 
        like seen below ⬇""",
        font=("Aptos", 24), highlightthickness = 4, highlightbackground = "dodgerblue2")
        instructions_label.pack()

        camera_label = tk.Label(self)
        camera_label.pack()

        # add clickable buttons


class PhotoPage(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(parent)

        title_label = tk.Label(self, text="PHOTO TAKEN", font=("Aptos", 40), fg="blue2")
        title_label.pack()

        keep_instructions_label = tk.Label(self, text="""If you wish to keep \n this photo and move \n on, show a thumbs \n upto the camera """, 
        font=("Aptos", 24), highlightthickness = 4, highlightbackground = "limegreen")
        keep_instructions_label.pack()

        or_label = tk.Label(self, text = "OR", font=("Aptos", 35))
        or_label.pack()

        delete_instructions_label=tk.Label(self, text="""If you would like \n to delete this photo \n show a thumbs down \n to the camera""", 
        font=("Aptos", 24),highlightthickness=4, highlightbackground="red2")
        delete_instructions_label.pack()

        photo_label = tk.Label(self)
        photo_label.pack()

        # add clickable buttons


class SavedPage(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(parent)
        
        title_label = tk.Label(self, 
        text="ADD QUANTITY", 
        font=("Aptos", 40), 
        fg="blue2")
        title_label.pack()


        subtitle_label = tk.Label(self, 
        font=("Aptos", 24), text="How many books are there?", 
        highlightthickness=4, highlightbackground="dodgerblue2")
        subtitle_label.pack()

        instructions_label = tk.Label(self, 
        font=("Aptos", 24), 
        text="Have the back of \n your hands facing \n the camera, then hold \n up the number of fingers \n for how many  of \n these books there are.",
        highlightthickness=4, highlightbackground="dodgerblue2")
        instructions_label.pack()

        # add entry widget
        # add clickable buttons




class DeletedPage(tk.Frame):
    def __init__(self, parent: tk.Misc):
        super().__init__(parent)

        title_label = tk.Label(self, text="BOOK SAVED", font=("Aptos", 40), fg="blue2")

        quantity_label = tk.Label(self, text=f"You have added {h} of these \n books into the database", font=("Aptos", 24), highlightthickness=4, highlightbackground="dodgerblue2")

        error_instruction_label = tk.Label(self, text="If there was an error, \n please change details in \n the database within the \n next 30 minutes", font=("Aptos", 24), highlightthickness=4, highlightbackground="dodgerblue2")

        home_instruction_label=tk.Label(self, highlightthickness=4, highlightbackground="dodgerblue2",  font=("Aptos", 24), text="If you would like to add \n another book, make an \n L shape with your hand")

        hand_img=tk.Label(self, highlightthickness=4, highlightbackground="dodgerblue2", font=("Aptos", 24), text="**Add gesture \n img**" )

        book_photo=tk.Label(self, highlightthickness=4, highlightbackground="dodgerblue2", text="***ADD IMAGE HERE***")



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gesture Photo Capturer")
        self.geometry('1500x800')

        home_page = HomePage(self)
        home_page.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()

# root.title("Gesture Photo Capturer")
# root.geometry('1500x800')

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
frame_gesture_camera = tk.Frame(root)
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

frame_gesture_camera.place(rely=.2, relx=.1)
label_widget = tk.Label(frame_gesture_camera)
label_widget.pack()

label_img = Image



# ******************************************
# END OF PHOTO GUI (screen 2)
# ******************************************



# ******************************************
# START OF PHOTO GUI (screen 3)
# ******************************************
frame_title_quantity = tk.Frame(root)
frame_how_many = tk.Frame(root)
frame_num_fingers = tk.Frame(root)
frame_hand_key_img = tk.Frame(root)



frame_title_quantity.place(anchor="n", relx=.5, rely=.025)
title_quantity = tk.Label(frame_title_quantity, 
text="ADD QUANTITY", 
font=("Aptos", 40), 
fg="blue2")


frame_how_many.place(relx=.5, rely=.2)
book_num = tk.Label(frame_how_many, 
font=("Aptos", 24), text="How many books are there?", 
highlightthickness=4, highlightbackground="dodgerblue2")


frame_num_fingers.place(anchor="n", relx=.7, rely=.4)
num_fingers = tk.Label(frame_num_fingers, 
font=("Aptos", 24), 
text="Have the back of \n your hands facing \n the camera, then hold \n up the number of fingers \n for how many  of \n these books there are.",
highlightthickness=4, highlightbackground="dodgerblue2")


# Uncomment when image file is added
# frame_hand_key_img.place(anchor="n", relx=.5, rely=.6)





# ******************************************
# END OF PHOTO GUI (screen 3)
# ******************************************





# ******************************************
# START OF PHOTO GUI (screen 4)
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

root.mainloop()
