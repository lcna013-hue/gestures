import tkinter
from tkinter import Image
from tkinter import Label
from tkinter import PhotoImage
root = tkinter.Tk()
root.title('Gesture Photo Capturer ')
root.geometry('1500x800')

frame_title_home = tkinter.Frame(root)
frame_fields = tkinter.Frame(root)
frame_scan = tkinter.Frame(root)
frame_credentials = tkinter.Frame(root)
frame_site = tkinter.Frame(root)
frame_change = tkinter.Frame(root)


def passx():
    pass

pinch_img = PhotoImage(file="pinch_gesutre_img.png")
pinch_lbl = tkinter.Label(root, image=pinch_img).grid()


frame_title_home.grid(row=0, column=0, padx=(750, 0))
title = tkinter.Label(frame_title_home, text="HOME", font=("Helvetica", 30))
title.grid(pady=(20, 10))
frame_fields.grid(row=3, column=1, padx=(80, 10), pady=(40, 10))
start_date_lbl = tkinter.Label(frame_fields, text="""To take a photo, make a pinching 
gesutre with your hand.""", font=("Helvetica", 20))
start_date_lbl.grid(column=0, row=0, pady=15)
end_date_lbl = tkinter.Label(frame_fields, text="text 2", font=("Helvetica", 20))
end_date_lbl.grid(column=0, row=1)

label_img = Image

root.mainloop()
