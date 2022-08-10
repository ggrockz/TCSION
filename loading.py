from tkinter import *
from homepage import main_home
from PIL import ImageTk, Image
import time
import os


def main_load():
    root.destroy()
    main_home()

root = Tk()
root.geometry("576x323")
root.overrideredirect(True) #hide title bar
root.eval('tk::PlaceWindow . center')#place the tkinter window center

'''
bg = ImageTk.PhotoImage(Image.open("D:/tcs/tenor1.gif"))

#creating canva
my_canva = Canvas(root, width=498, height=280)
my_canva.pack(fill="both", expand=True)

#setting image in canva
my_canva.create_image(0,0, image=bg, anchor="nw")
#my_canva.create_text(400, 250, text="Automate detection of different emotions \nfrom textual comments and feedback", font=("italic", 40), anchor="sw" , justify="center") #fill color
'''


#gif

frameCnt = 13
frames = [PhotoImage(file='D:/tcs/tenor1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
#end gif

root.after(2000, main_load)

mainloop()