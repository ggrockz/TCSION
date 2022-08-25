#from transformers import pipeline
#from transformers import logging
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import  requests
import json
from tkinter import *


'''
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
emotion_text = emotion("i cried looking for u")
print(emotion_text)
logging.set_verbosity_warning()
'''
def textrun():
    logging.set_verbosity_warning()

    actualtext = textentry.get("1.0", "end-1c")
    emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
    emotion_text = emotion(actualtext)
    outputtxt.delete('1.0', END)
    outputtxt.insert(END, emotion_text)

def show():

    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    city_name = "bengaluru"
    api_key = "519f63ba255a98f7dac423aed65c8ccf"

    urls = base_url + "q=" + city_name + "&appid=" + api_key

    result = requests.get(urls)

    # checking the status
    if result.status_code == 200:
        data = result.json()
        # getting main block
        main = data['main']
        temperature = main['temp']
        report = data['weather']
        weath_label.insert(END, temperature)
        weath_label.insert(END, report)

        #print(f"Temperature: {temperature}")
        #print(f"Weather Report: {reportfl}")

    else:
        print("Error in HTTP")

def textmain():

    root = Tk()
    root.geometry("500x350")
    root.eval('tk::PlaceWindow . center')
    root.title("Text page")

    '''#for dropdown
    options = ["bengaluru", "delhi", "hyderabad", "calicut"]
    global clicked
    clicked = StringVar()
    clicked.set("bengaluru")
    global weath
    weath = OptionMenu(root, clicked, *options)
    weath.place(x=20, y=30)'''

    global weath_bt
    weath_bt = Button(root, text="Bengaluru", command= show)
    weath_bt.place(x=30, y=30)

    global weath_label
    weath_label = Text(root, height=2, width=40)
    weath_label.place(x=105, y=30)

    textlabel = Label(root, text='Enter your text below:', font= ('bold1', 11))
    textlabel.place(x=30, y=80)

    global textentry
    textentry = Text(root, height=5, width=50, bg="light cyan")
    textentry.place(x=50, y=110)

    subbt = Button(root, text="Submit", font=("italic", 10), bg="cyan", command=textrun)
    subbt.place(x=230, y=200)

    global outputtxt
    outputtxt = Text(root, height=3, width=50, bg="light yellow")
    outputtxt.place(x=50, y=240)



    root.mainloop()


textmain()
