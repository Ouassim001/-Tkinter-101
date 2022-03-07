from tkinter import *

window = Tk()
window.title("Hello")
window.geometry("300x300")

canvas= Canvas(width= 1000, height= 750, bg="#e30000")

canvas.create_text(150, 150, text="HELLO TKINTER", fill="#111211", font=('Helvetica 20 bold'))
canvas.pack()




window.mainloop()