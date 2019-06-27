from tkinter import *
def speak(E1,root):
    text = E1.get()
    print(text)

    import pyttsx3
    tts = pyttsx3.init()
    tts.say(text)
    tts.runAndWait()

root = Tk()
root.title('Text to Speech')
root.geometry('900x300') #width X height
root.resizable(True,True)

L1 = Label(root,text='Text to Speech Conversion',
           font = ('Arial',20,'bold'),fg='Blue')
L1.place(x=120,y=50)

L2 = Label(root,text="Enter text:",
           font = ("Arial",15),fg='Blue')
L2.place(x=100,y=150)

E1 = Entry(root,font=("Arial",15,'bold'),fg="Blue")
E1.place(x=200,y=150)

B1 = Button(root,text="Speak Now",command=lambda:speak(E1,root),
            font=("Arial",15,'bold'),fg='Red')
B1.place(x=220,y=200)

volume = 1

def volume_minus():
    global volume,L3
    v = volume-0.1
    L2 = Label(root,text=str(volume),
               font = ("Arial",15),fg="Blue")
    L2.place(x=270,y=250)
    L2.destroy()

L2 = Label(root,text=str(volume),
           font = ('Arial',15),fg="Blue")
L2.place(x=270,y=250)

B2 = Button(root,text="-",command=volume_minus,
            font=('Arial',15),fg='Red')
B2.place(x=220,y=250)


root.mainloop()    
    
