import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox

m=Tk()

frame=tk.Frame(m)

m.title("Withdraw Cash")

heading=tk.Label(frame,text="Sbi Bank",font=("italic",20))

lamount=tk.Label(frame,text="Enter Amount: ")
lamount.grid(row=5,column=2,padx=10,pady=10)

amount=tk.Entry(frame)
amount.grid(row=5,column=4,padx=10,pady=10)




lpin=tk.Label(frame,text="Enter Password : ")
lpin.grid(row=6,column=2,padx=10,pady=10)

pin=tk.Entry(frame)
pin.grid(row=6,column=4,padx=10,pady=10)

label=tk.Label(frame,fg="green",font=("bold",15))

def pmatch():
    
    connection= mysql.connector.connect(host='localhost', user='root',password='',port='3306',database='sbi_bank')
    c=connection.cursor()
    password=pin.get()
    abalance=amount.get()
    
    pas="select * from customerinfo where Password= %s"
    udate="UPDATE customerinfo SET Balance = Balance - %s where Password= %s"
    
    c.execute(pas,[(password)])
    pinno=c.fetchall()

    if pinno:
        
        c.execute(udate,[(abalance),(password)])
        connection.commit()
        label.config(text="Amount Debited")
        
    else:
        messagebox.showerror("Error","Incorrect Password")
        return False






loButton=tk.Button(frame,text="Withdraw Cash" ,width="18", bg="yellow",command=lambda:[pmatch()])


loButton.grid(row=9,column=3,padx=10,pady=10)

heading.grid(row=0,column=2)
label.grid(row=10,column=3)
frame.grid(row=0,column=0)
m.mainloop()
