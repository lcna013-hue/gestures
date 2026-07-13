import tkinter as tk
h = "2"
root = tk.Tk()
root.title("Gesture Photo Capturer")
root.geometry('1500x800')

frame_title = tk.Frame(root)
frame_book_img = tk.Frame(root)
frame_books_added = tk.Frame(root)
frame_error = tk.Frame(root)
frame_add = tk.Frame(root)
frame_add_another = tk.Frame(root)
frame_hand_img = tk.Frame(root)

frame_title.place(anchor="n", relx=.5, rely=.025)
title = tk.Label(frame_title, text="BOOK SAVED", font=("Aptos", 40), fg="blue2")
title.pack()

frame_add.place(relx=.39, rely=.25)
add_lbl = tk.Label(frame_add, text=f"You have added {h} of these \n books into the database", font=("Aptos", 24), highlightthickness=4, highlightbackground="dodgerblue2")
add_lbl.pack(ipadx=10, ipady=30)

frame_error.place(relx=.4, rely=.55)
error_lbl = tk.Label(frame_error, text="If there was an error, \n please change details in \n the database within the \n next 30 minutes", font=("Aptos", 24), highlightthickness=4, highlightbackground="dodgerblue2")
error_lbl.pack(ipadx=15, ipady=12)

frame_add_another.place(relx=.7, rely=.4)
book_add=tk.Label(frame_add_another, highlightthickness=4, highlightbackground="dodgerblue2",  font=("Aptos", 24), text="If you would like to add \n another book, make an \n L shape with your hand")
book_add.pack(ipadx=12, ipady=8)

frame_hand_img.place(relx=.76, rely=.67)
hand_img=tk.Label(frame_hand_img, highlightthickness=4, highlightbackground="dodgerblue2", font=("Aptos", 24), text="**Add gesture \n img**" )
hand_img.pack(ipadx=8, ipady=18)

frame_book_img.place(relx=.04, rely=.2)
book_photo=tk.Label(frame_book_img, highlightthickness=4, highlightbackground="dodgerblue2", text="***ADD IMAGE HERE***")
book_photo.pack(ipadx=170, ipady=240)

root.mainloop()