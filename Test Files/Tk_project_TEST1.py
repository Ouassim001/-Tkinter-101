# from tkinter import *
import tkinter as Tk
import sys

def update():
    label1.config(fg="red")


window = Tk.Tk()
window.title("bomb")
window.geometry("500x500")

label1 = Tk.Label(window, text="black text")
label1.place(x=30,y=20)

button = Tk.Button(window, text="change color", command = lambda: window.after(1,update))
button.place(x=30,y=50)

# alle tkinter code komt hieronder


window.mainloop()