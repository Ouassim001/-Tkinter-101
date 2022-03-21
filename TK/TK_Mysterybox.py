from tkinter import *
from tkinter import messagebox
import random

window = Tk()  
window.title("MysteryBox")
window.geometry("200x200") 
window.config(bg="#005a9e") 


def showMsg(): 
    prizes = ["PS5", "5 Million dollars", "Lambo keys"]
    messagebox.showinfo('message', "Congratulations you won a prize. click to claim prize")
    messagebox.showinfo("prizes", print(random.choice(prizes)))

button = Button(window,text ="Claim",
	    command = showMsg)
button.config(font=("helvetica",20,"bold"))
button.pack()  
  


window.mainloop()