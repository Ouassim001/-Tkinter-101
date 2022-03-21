import sys
import time
import sys
from tkinter import *

window = Tk()
window.title("Digital Clock")


def get_time():
    timeVar = time.strftime("%H:%M:%S")
    clock.config(text=timeVar)
    clock.after(200,get_time)

clock = Label(window, font=("Helvetica 20 bold", 90), bg="#191a19", fg="#d5d5db")
clock.pack()


get_time()

window.mainloop()