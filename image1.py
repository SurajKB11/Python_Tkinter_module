from Tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("root_tkinter")

img1=ImageTk.PhotoImage(Image.open("index.png"))
img2=ImageTk.PhotoImage(Image.open("index.jpeg"))
img3=ImageTk.PhotoImage(Image.open("index.png"))
img4=ImageTk.PhotoImage(Image.open("index.jpeg"))
img5=ImageTk.PhotoImage(Image.open("index.png"))

img_list=[img1, img2, img3, img4, img5]

def before(n):
    global label
    global bb
    global bf
    global status
    label.grid_forget()
    label=Label(image=img_list[n])
    status=Label(root,text="Image "+str(n+1)+" of "+str(len(img_list)),pady=10,bd=10)
    status.grid(row=3,column=1,columnspan=3,sticky="e")
    bf=Button(root,text=">>",command=lambda: after(n+1))
    bb=Button(root,text="<<",command=lambda: before(n-1))
    if n<=1:
        bb=Button(root,text="<<",state=DISABLED)
    bb.grid(row=1,column=0)
    bf.grid(row=1,column=2)
    label.grid(row=0,column=0,columnspan=3)

def after(n):
    global label
    global bb
    global bf
    global status
    label.grid_forget()
    label=Label(image=img_list[n-1])
    status=Label(root,text="Image "+str(n+1)+" of "+str(len(img_list)),pady=10,bd=10)
    status.grid(row=3,column=1,columnspan=3,sticky="e")
    bf=Button(root,text=">>",command=lambda: after(n+1))
    bb=Button(root,text="<<",command=lambda: before(n-1))
    if n == 4:
        bf=Button(root,text=">>",state=DISABLED)
    bb.grid(row=1,column=0)
    bf.grid(row=1,column=2)
    label.grid(row=0,column=0,columnspan=3)

label=Label(image=img_list[0])
label.grid(row=0,column=0,columnspan=3)

bb=Button(root,text="<<",command=lambda: before(0),state=DISABLED)
be=Button(root,text="exit",command=root.quit)
bf=Button(root,text=">>",command=lambda: after(2))

status=Label(root,text="Image 1 of "+str(len(img_list)),pady=10,bd=10)
status.grid(row=3,column=1,columnspan=3,sticky="e")

bb.grid(row=1,column=0)
be.grid(row=1,column=1)
bf.grid(row=1,column=2)

root.mainloop()

















