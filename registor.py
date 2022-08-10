from tkinter import *
import tkinter.messagebox as messagebox
from database import *


def hbt():
    from homepage import main_home
    root.destroy()
    main_home()

def submit():
    username = e_username.get()
    password = e_password.get()
    mobileno = e_mobileno.get()
    emailid = e_mail.get()

    if (username == "" or password == "" or mobileno == "" or emailid == ""):
        messagebox.showinfo("Error", "Please enter all values")
    else:
        mycursor.execute("insert into new_user (username, password, mobileno, gmailid) values('"+ username +"','"+ password +"', '"+ mobileno +"','"+ emailid +"')")
        mycursor.execute("commit")

        messagebox.showinfo("Status", "Submitted successfully")

        from sendmail import send_message
        global address_info
        address_info = emailid
        send_message()

def clear():
    e_username.delete(0, 'end')
    e_password.delete(0, 'end')
    e_mobileno.delete(0, 'end')
    e_mail.delete(0, 'end')

def regis():

    global e_username
    global e_password
    global e_mobileno
    global e_mail

    global root
    root = Tk()
    root.geometry("350x350")
    root.eval('tk::PlaceWindow . center')
    root.title("TCS AI")

    username = Label(root, text='Enter the username', font=('bold', 10))
    username.place(x=20, y=60)

    password = Label(root, text='Enter the password', font=('bold', 10))
    password.place(x=20, y=90)

    mobileno = Label(root, text='Enter the mobileno', font=('bold', 10))
    mobileno.place(x=20, y=120)

    mail = Label(root, text='Enter your mail id', font=('bold', 10))
    mail.place(x=20, y=150)

    e_username = Entry()
    e_username.place(x=150, y=60)

    e_password = Entry()
    e_password.place(x=150, y=90)
    e_password.config(show="*")

    e_mobileno = Entry()
    e_mobileno.place(x=150, y=120)

    e_mail = Entry()
    e_mail.place(x=150, y=150)

    submit1 = Button(root, text="Submit", font=("italic", 10), bg="white", command=submit)
    submit1.place(x=100, y=210)

    clear1 = Button(root, text="Clear", font=("italic", 10), bg="white", command=clear)
    clear1.place(x=200, y=210)

    homebt = Button(root, text="Home", font=("italic", 10), bg="cyan", command=hbt)
    homebt.place(x=10, y=10)

    root.mainloop()

