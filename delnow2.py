import sqlite3

def delrec(r):
    global records
    co=sqlite3.connect('products.db')
    c=co.cursor()
    for i in records:
        if i[0]==r:
            c.execute("DELETE FROM incart WHERE oid="+str(i[4]))
    c.execute("SELECT * FROM incart")
    rec=c.fetchall()
    print(rec)
    co.commit()
    co.close()
  
co=sqlite3.connect('products.db')
c=co.cursor()
c.execute("SELECT *,oid FROM incart")
records=c.fetchall()
print(records)
co.commit()
co.close()
#delrec("hi")
