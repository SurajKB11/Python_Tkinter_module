from Tkinter import *
root=Tk()
root.geometry("300x200")
root.title("insert text")
w1=Entry(root,width=50,borderwidth=5)
w1.pack()
w1.insert(0,"enter name")
w=Label(root)
def clicked():
    w.configure(text="Welcome "+w1.get())
    w.pack()
w2=Button(root,text="click me!!",command=clicked)
w2.pack()              
root.mainloop()
