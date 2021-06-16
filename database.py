from Tkinter import *
from PIL import Image,ImageTk
import sqlite3

root=Tk()
root.title("databases")

conn=sqlite3.connect('address_book.db')
c=conn.cursor()
'''
c.execute("""CREATE TABLE addresses
       (
         first_name text,
         last_name text,
         address text,
         city text,
         state text,
         zipcode integer
        )
        """)
'''
def submit():
    f.delete(0,END)
    l.delete(0,END)
    a.delete(0,END)
    c.delete(0,END)
    s.delete(0,END)
    z.delete(0,END)
    return

f=Entry(root,width=30)
f.grid(row=0,column=1)
l=Entry(root,width=30)
l.grid(row=1,column=1)
a=Entry(root,width=30)
a.grid(row=2,column=1)
c=Entry(root,width=30)
c.grid(row=3,column=1)
s=Entry(root,width=30)
s.grid(row=4,column=1)
z=Entry(root,width=30)
z.grid(row=5,column=1)

Label(root,text="first name:").grid(row=0,column=0)
Label(root,text="last name :").grid(row=1,column=0)
Label(root,text="address   :").grid(row=2,column=0)
Label(root,text="city      :").grid(row=3,column=0)
Label(root,text="state     :").grid(row=4,column=0)
Label(root,text="zip code  :").grid(row=5,column=0)

Button(root,text="submit",command=submit).grid(row=6,column=0,columnspan=2)
conn.commit()
conn.close()

root.mainloop()
