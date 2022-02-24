# from tkinter import *
from operator import truediv
import tkinter as Tk

def change1():
    window.config(bg="#ff0000")
    window.geometry("300x300")

def change2():
    window.config(bg="#f75200")
    window.geometry("350x350")

def change3():
    window.config(bg="#ddff00")
    window.geometry("400x400")

def change4():
    window.config(bg="#590600")
    window.geometry("450x450")

window = Tk.Tk()
window.title("bomb")
window.geometry("250x250")

window.after(1000, change1)
window.after(2000, change2)
window.after(3000, change3)
window.after(4000, change4)




window.mainloop()