import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox
m=Tk()

m.title("Login Page" )

frame=tk.Frame(m)



lfname=tk.Label(frame,text="Full Name: ")
fname=tk.Entry(frame)

lpas=tk.Label(frame,text="Password: ")
pas=tk.Entry(frame)

lfname.grid(row=1,column=1)
fname.grid(row=1,column=3,pady=10, padx=10)

lpas.grid(row=2,column=1)
pas.grid(row=2,column=3,pady=10, padx=10)

label=tk.Label(frame,fg="green")


    
    
def match():
    connection= mysql.connector.connect(host='localhost', user='root',password='',port='3306',database='sbi_bank')
    c=connection.cursor()
    firstname=fname.get()
    password=pas.get()

    login="select * from customerinfo where Name =%s and Password= %s"
    
    c.execute(login,[(firstname),(password)])
    result=c.fetchall()

    
    
    if result:
        label.config(text="Login Successful",font=('bold',20))
        import mainpage.py
        
        
        

    else:
        messagebox.showerror("Error","Incorrect Login Credentials")

        return False
     
    


loButton=tk.Button(frame,text=" Login" ,width="25", bg="yellow",command=lambda:[match()])
loButton.grid(row=5,column=2,padx=10,pady=10)
label.grid(row=9,column=2)
frame.grid(row=0,column=0)
m.mainloop()
