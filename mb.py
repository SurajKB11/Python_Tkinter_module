from tkinter import *
from PIL import *
#import tkMessageBox
from tkinter import messagebox

root=Tk()
root.title("message")

def popup():
    #tkMessageBox.askyesno("this is my popup!","hello world!")
    response=messagebox.askyesno("yes/no messagebox","respond?")
    Label(root,text=response).pack()
    #from above code, we know clicking "yes" returns 1 otherwise 0
    #note: check the same for askquestion, etc...
    if response==1:
        Label(root,text="you clicked yes!").pack()
    else:
        Label(root,text="you clicked no!").pack()

Button(root,text="pop-up",command=popup).pack()
    
root.mainloop()

#showwarning
#showerror
#askquestion
#askokcancel
#askyesno
