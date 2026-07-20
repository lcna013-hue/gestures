import tkinter as tk

from PIL import Image

def screen_3_show():
    frame_title_quantity.place(anchor="n", relx=.5, rely=.025)
    frame_how_many.place(relx=.5, rely=.2)
    frame_num_fingers.place(anchor="n", relx=.7, rely=.4)
    frame_hand_key_img.place(anchor="n", relx=.5, rely=.6)


    title_quantity.pack()
    book_num.pack(ipadx=80, ipady=30)
    num_fingers.pack(ipadx=15, ipady=15)


def screen_3_hide():
    # This will remove the widget
    frame_title_quantity.place_forget()
    frame_how_many.place_forget()
    frame_num_fingers.place_forget()
    frame_hand_key_img.place_forget()



root = tk.Tk()
root.title("Gesture Photo Capturer")
root.geometry('1500x800')

frame_title_quantity = tk.Frame(root)
frame_how_many = tk.Frame(root)
frame_num_fingers = tk.Frame(root)
frame_hand_key_img = tk.Frame(root)




title_quantity = tk.Label(frame_title_quantity, 
text="ADD QUANTITY", 
font=("Aptos", 40), 
fg="blue2")


book_num = tk.Label(frame_how_many, 
font=("Aptos", 24), text="How many books are there?", 
highlightthickness=4, highlightbackground="dodgerblue2")


num_fingers = tk.Label(frame_num_fingers, 
font=("Aptos", 24), 
text="Have the back of \n your hands facing \n the camera, then hold \n up the number of fingers \n for how many  of \n these books there are.",
highlightthickness=4, highlightbackground="dodgerblue2")


add_btn = tk.Button(root, text="Click to show screen", command=screen_3_show)
add_btn.pack()

forget_btn = tk.Button(root, text="Click to clear screen", command=screen_3_hide)
forget_btn.pack(pady=300)

screen_3_show() 

root.mainloop()