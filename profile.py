from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import PIL
import cv2
from database import *
from text import textmain
#import pygame
#import pygame.camera


def submit():
    mycursor.execute("insert into new_user (profpic) values('" + img + "')")
    #mycursor.execute("commit")
    mycursor.commit()

    print("")

def text():
    root.destroy()
    textmain()

def camera2():
    width, height = 800, 600
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    global img
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    print(type(img))
    #lmain.after(10, show_frame)

    #cam = VideoCapture(cam_port)
    #result, image = cam.read()

def camera():
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    vid.release()
    cv2.imwrite("img.jpg", frame)
    img = PIL.Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    print(type(img))


def browse():
    global img, filename
    ftypes =[('png files','*.png'),('jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=ftypes)
    img = ImageTk.PhotoImage(file=filename)
    b2 = Tk.Button(my_w, image=img)
    b2.grid(row=4, column=1, columnspan=2)

def profmain():

    global lmain
    global root
    root = Tk()
    root.title("Profile page")
    root.geometry("500x400")
    root.eval('tk::PlaceWindow . center')
    lmain = Label(root)
    lmain.pack()

    welmes = Label(root, text='Welcome! gg', font=('bold', 10))
    welmes.place(x=20, y=30)


    cambt = Button(root, text="Camera", font=("italic", 10), command=camera)
    cambt.place(x=370, y=80)

    browsebt = Button(root, text="Browse", font=("italic", 10), command=browse)
    browsebt.place(x=370, y=130)

    textbt = Button(root, text="Text", font=("italic", 10), command=text)
    textbt.place(x=370, y=180)

    submitbt = Button(root, text="Submit", font=("italic", 10), command=submit)
    submitbt.place(x=270, y=240)



    root.mainloop()

profmain()