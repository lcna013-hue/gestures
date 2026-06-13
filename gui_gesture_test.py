import tkinter as tk

root = tk.Tk()
root.geometry("740x590")


# Displays text
title_home = tk.Label(root, text="HOME", font=("aptos", 25))
title_home.pack()

# Bok for camera
button2 = tk.Button(root, text="Camera", highlightthickness=2,
 highlightbackground = "dodgerblue2").pack()


# Displays text
text = tk.Label(root, text="text", highlightthickness=2, highlightbackground = "dodgerblue2")
text.pack()

# Button, when pressed closed root
button = tk.Button(root, text="Stop", width=15, command=root.destroy)
button.pack()


entry = tk.Entry(root)
entry.pack()

label = tk.Label(root, text='')
label.pack()


def get_entry_value():
    value = entry.get()
    print(value)
    label.config(text=value)


button3 = tk.Button(root, text="Get Entry Value", command=get_entry_value)
button3.pack()

root.mainloop()


root.mainloop()