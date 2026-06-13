import tkinter

root = tkinter.Tk()
root.title('HOME')
root.geometry('700x500')

frame_title = tkinter.Frame(root)
frame_fields = tkinter.Frame(root)
frame_scan = tkinter.Frame(root)
frame_credentials = tkinter.Frame(root)
frame_site = tkinter.Frame(root)
frame_change = tkinter.Frame(root)


def passx():
    pass


frame_title.grid(row=0, column=0, padx=(50, 0))
title = tkinter.Label(frame_title, text="Bookings Scan", font=("Helvetica", 24))
title.grid(pady=(20, 10))
frame_fields.grid(row=1, column=0, padx=(30, 0), pady=(10, 0))
start_date_lbl = tkinter.Label(frame_fields, text="Enter the start date: ", font=("Helvetica", 16))
start_date_lbl.grid(column=0, row=0, pady=15)
start_date_unp = tkinter.Entry(frame_fields, width=11, font=("Helvetica", 16))
start_date_unp.grid(column=1, row=0)
start_date = start_date_unp.get()
end_date_lbl = tkinter.Label(frame_fields, text="Enter the end date: ", font=("Helvetica", 16))
end_date_lbl.grid(column=0, row=1)
end_date_unp = tkinter.Entry(frame_fields, width=11, font=("Helvetica", 16))
end_date_unp.grid(column=1, row=1)
end_date = end_date_unp.get()

root.mainloop()
