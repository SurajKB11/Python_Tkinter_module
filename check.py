from Tkinter import *
from PIL import ImageTk,Image


root=Tk()

var=StringVar() #can be IntVar()
c=Checkbutton(root,text="check this box",variable=var,onvalue="on",offvalue="off")
c.deselect() #to fix a glitch ... find out more
c.pack()

def checked():
    mylabel=Label(root,text=var.get()).pack()

b=Button(root,text="click",command=checked).pack()


root.mainloop()
