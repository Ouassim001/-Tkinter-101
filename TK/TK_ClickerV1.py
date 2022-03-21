from tkinter import *

window = Tk()
window.title("ClickerV1")
window.geometry("400x400")


count = 0
def clickUp():
    global count
    count+=1
    counter.config(text=count)
    if count >0:
        window.config(bg="#00e832")

def clickDown():
    global count
    count-=1
    counter.config(text=count)
    if count <0:
        window.config(bg="#eb0000")



button = Button(text="UP",
                font=("helvetica"),
                state=ACTIVE,
                padx=10,
                pady=10,
                relief="solid",
                command="UP")
button.pack(side=TOP, padx=10, pady=10)

button2 = Button(text="DOWN",
                state=ACTIVE,
                padx=10,
                pady=10,
                relief="solid",
                command="DOWN",)
button2.pack(side=BOTTOM, padx=10, pady=10)

button.config(command=clickUp)
button2.config(command=clickDown)


counter = Label(window,
                text=count)
counter.pack()

if count == 0:
    window.config(bg="#454545")



window.mainloop()