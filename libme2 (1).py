from tkinter import *
from tkinter import messagebox
import pymysql
def insertrecord():
    conn = pymysql.connect(host='localhost',user='root',password='',database="aniket")
    cursor = conn.cursor()
    name=e_name.get()
    member=e_member.get()
    book=e_book.get()
    author=e_author.get()
    price=e_price.get()
    q="insert into library(Name,member_id,book,author,price)values(%s, %s, %s, %s, %s)"
    val=(name,member,book,author,price)
    cursor.execute(q,val)
    conn.commit()
    messagebox.showinfo('library',"successful!!")

def displayrecord():
    conn = pymysql.connect(host='localhost',user='root',password='',database="aniket")
    cursor = conn.cursor()
    name=e_name.get()
    member=e_member.get()
    book=e_book.get()
    author=e_author.get()
    price=e_price.get()
    q="select * from library"
    cursor.execute(q)        
    records=cursor.fetchall()
    for row in records:
        print("member_id = ",row[1])
        print("Book name = ",row[2])
        print("author name = ",row[3])
        print("price =",row[4])
       
def searchrecord():
    conn = pymysql.connect(host='localhost',user='root',password='',database="aniket")
    cursor = conn.cursor()
    name=e_name.get()
    member=e_member.get()
    book=e_book.get()
    author=e_author.get()
    price=e_price.get()
    q="select * from library where book=%s"
    cursor.execute(q,book)
    records=cursor.fetchall()
    for row in records:
        print("Member Name = ",row[0])
        print("member_id = ",row[1])
        print("Book name = ",row[2])
        print("author name = ",row[3])
        print("price =",row[4])
        messagebox.showinfo("library",'book issue')
        break
    else:
        messagebox.showinfo('library',"book does not exist")

def deleterecord():
    conn = pymysql.connect(host='localhost',user='root',password='',database="aniket")
    cursor = conn.cursor()
    name=e_name.get()
    member=e_member.get()
    book=e_book.get()
    author=e_author.get()
    price=e_price.get()
    q="delete from Library where book=%s"
    cursor.execute(q,book)
    conn.commit()
    messagebox.showinfo('library',"record delete successfully")

def updaterecord():
    conn = pymysql.connect(host='localhost',user='root',password='',database="aniket")
    cursor = conn.cursor()
    name=e_name.get()
    member=e_member.get()
    book=e_book.get()
    author=e_author.get()
    price=e_price.get()
    q="update Library set price=%s where book=%s"
    val=(price,book)
    cursor.execute(q,val)
    conn.commit()
    messagebox.showinfo('library',"record updated successfully")

def returnbook():
    conn = pymysql.connect(host='localhost',user='root',password='',database="aniket")
    cursor = conn.cursor()
    name=e_name.get()
    member=e_member.get()
    book=e_book.get()
    author=e_author.get()
    price=e_price.get()
    q="update Library set price=%s where book=%s"
    val=(price,book)
    cursor.execute(q,val)
    conn.commit()
    messagebox.showinfo('library',"book return sucessfully")
    


#main program
window=Tk()
window.title('Library From')
window.geometry('900x800')

l_name=Label(window,text="Member_name :",fg="black")
l_name.grid(row=0,column=1)
e_name=Entry(window,fg="red")
e_name.grid(row=0,column=2)

l_member=Label(window,text="member_id : ",fg="black")
l_member.grid(row=0,column=3)
e_member=Entry(window,fg="black")
e_member.grid(row=0,column=4)

l_book=Label(window,text="book name :",fg="black")
l_book.grid(row=1,column=1)
e_book=Entry(window,fg="black")
e_book.grid(row=1,column=2)

l_author=Label(window,text="author_name :",fg="black")
l_author.grid(row=1,column=3)
e_author=Entry(window,fg="black")
e_author.grid(row=1,column=4)

l_price=Label(window,text="price :",fg="black")
l_price.grid(row=2,column=1)
e_price=Entry(window,fg="black")
e_price.grid(row=2,column=2)

b1=Button(window,text="Insert Record",fg="blue", font=("Arial",15),command=insertrecord)
b1.grid(row=3,column=2)

b2=Button(window,text="Display Record",fg="blue", font=("Arial",15),command=displayrecord)
b2.grid(row=3,column=4)

b3=Button(window,text="Issue Book",fg="blue", font=("Arial",15),command=searchrecord)
b3.grid(row=4,column=2)

b4=Button(window,text="Delete Record",fg="blue", font=("Arial",15),command=deleterecord)
b4.grid(row=4,column=4)

b5=Button(window,text="Update Record",fg="blue", font=("Arial",15),command=updaterecord)
b5.grid(row=5,column=2)

b6=Button(window,text="return",fg="blue", font=("Arial",15),command=returnbook)
b6.grid(row=5,column=4)

window.mainloop()
