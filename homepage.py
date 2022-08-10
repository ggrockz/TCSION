from tkinter import *
import tkinter.messagebox as messagebox
from registor import regis
from login import loginmain


def registorfn():
    root.destroy()
    regis()

def loginfn():
    root.destroy()
    loginmain()

def main_home():
    global root
    root = Tk()
    root.title("Home page")
    root.geometry("350x200")
    root.eval('tk::PlaceWindow . center')

    text = Label(root, text='Welcome!!', font=('bold', 10))
    text.pack(pady=50)

    loginbt = Button(root, text="Login", font=("italic", 10), bg="white", command=loginfn, height=3, width=10)
    loginbt.place(x=190, y=110)

    registorbt = Button(root, text="Registor", font=("italic", 10), bg="white", command=registorfn, height=3, width=10)
    registorbt.place(x=80, y=110)

    root.mainloop()