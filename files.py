from Tkinter import *
from PIL import Image,ImageTk
import tkFileDialog as filedialog

root=Tk()
root.title("files")
def sfile():
    global img
    root.filename=filedialog.askopenfilename(initialdir="/home/suraj/Desktop/INTERNSHIP/py",title="select a file",filetypes=(("jpeg files",".jpeg"),("all files","*.*")))
    #Label(root,text=root.filename).pack()
    img=ImageTk.PhotoImage(Image.open(root.filename))
    Label(root,image=img).pack()
    
Button(root,text="Select File",command=sfile).pack()


root.mainloop()
