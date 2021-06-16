from Tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("frames")
f=LabelFrame(root,text="this is my frame",padx=10,pady=10)
f.pack(padx=100,pady=100)
b=Button(f,text="don't click here")
b.pack()
root.mainloop()
