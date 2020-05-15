from tkinter import *
from tkinter import ttk
root=Tk()
button =ttk.Button(root,text="click me")
button.pack()

def callback():
    print("Clicked")
button.config(command=callback)


logo= PhotoImage(file ="C:\my file\Pictures\3D-Box-HD-Wallpaper.jpg")
button.config(image = logo, compund=left)
