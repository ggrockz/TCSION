from tkinter import *
import tkinter.messagebox as messagebox
from database import *
from profile import profmain

def hbt():
    from homepage import main_home
    root.destroy()
    main_home()

def login():
    userid = e_userid.get()
    userpass = e_userpass.get()
    query = "select * from new_user where username = %s and password = %s"
    mycursor.execute(query, [(userid), (userpass)])
    result = mycursor.fetchall()

    if result:
        messagebox.showinfo("status", "Login Success")
        root.destroy()
        profmain()

    else:
        messagebox.showinfo("status", "Invalid login ceredentials")

def loginmain():

    global e_userid
    global e_userpass
    global root

    root = Tk()
    root.title("Login page")
    root.geometry("400x250")
    root.eval('tk::PlaceWindow . center')

    userid = Label(root, text='Enter your user id', font=('bold', 10))
    userid.place(x=20, y=60)

    userpass = Label(root, text='Enter your password', font=('bold', 10))
    userpass.place(x=20, y=90)

    e_userid = Entry()
    e_userid.place(x=200, y=60)

    e_userpass = Entry()
    e_userpass.place(x=200, y=90)
    e_userpass.config(show="*")

    login1 = Button(root, text="Login", font=("italic", 10), bg="blue", command=login, height=3, width=10)
    login1.place(x=135, y=160)

    homebt = Button(root, text="Home", font=("italic", 10), bg="cyan", command=hbt)
    homebt.place(x=10, y=10)

    root.mainloop()