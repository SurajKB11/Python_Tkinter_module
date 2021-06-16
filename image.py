from Tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("this is tkinter")

img=ImageTk.PhotoImage(Image.open("index.png"))
label=Label(image=img)
label.pack()

root.mainloop()
