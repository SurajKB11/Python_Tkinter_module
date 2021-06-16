from Tkinter import *
from PIL import ImageTk,Image

root=Tk()
clicked=StringVar()
clicked.set("select an option")
drop=OptionMenu(root,clicked,"select an option","monday","tuesday","wednesday","thursday","friday")
drop.pack()
def show():
    Label(root,text=clicked.get()).pack()
b=Button(root,text="selected",command=show).pack()
root.mainloop()
