import mysql.connector

import tkinter as tk
from tkinter import messagebox
from tkinter import *
m=Tk()

m.title("Registration Form")

connection= mysql.connector.connect(host='localhost', user='root',password='',port='3306',database='sbi_bank')
c=connection.cursor()



frame=tk.Frame(m)


head=tk.Label(frame,text="REGISTRATION FORM",font=(20))

#full name
lfname=tk.Label(frame,text="Full Name: ")
fname=tk.Entry(frame)

#password
lpas=tk.Label(frame,text="Password: ")
pas=tk.Entry(frame)

#Date of birth
ldob=tk.Label(frame,text="Date Of Birth: ")
dob=tk.Entry(frame)

#phone number
lphone=tk.Label(frame,text="Phone Number: ")
phone=tk.Entry(frame)

#adhaar number
ladhaar=tk.Label(frame,text="Adhaar Number: ")
adhaar=tk.Entry(frame)

lpan=tk.Label(frame,text="Pan No: ")
pan=tk.Entry(frame)


# balance

lbalance=tk.Label(frame,text="Balance: ")
balance=tk.Entry(frame)

def home():
    import homepage.py

re=tk.Button(frame,text="Return to Home page",command=lambda:[home()])
re.grid(row=15,column=2)

label=tk.Label(frame,fg="green")

    
    
def insertData():
    firstname = fname.get()
    password= pas.get()
    dateofbirth = dob.get()
    phoneno = phone.get()
    adhaarno = adhaar.get()
    pancard=pan.get()
    abalance=balance.get()

    
        

    if(len(phoneno)<10):
        messagebox.showerror("Error","Please enter 10 digit mobile no.")
    
    elif(len(adhaarno)<12):
        messagebox.showerror("Error","Please enter 12 digit adhaar no.")

    elif(len(pancard)<10):
        messagebox.showerror("Error","Please enter 10 digit pancard no.")

    else:
        label.config(text="Data Saved Successfully",font=('bold',15))
        
        insert_query = "INSERT INTO `customerinfo`(`Name`, `Password`, `DOB`, `Phone`, `Adhaar`, `Pan No`, `Balance`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        t = (firstname,password,dateofbirth,phoneno,adhaarno,pancard,abalance)
        c.execute(insert_query,t)
        connection.commit()

  
    

    
#if (len(phone)==10):
myButton=tk.Button(frame,text="  Register ",width="25",bg="yellow", command= lambda:[insertData()])

#positing

head.grid(row=0,column=2)

lfname.grid(row=1,column=1)
fname.grid(row=1,column=2,pady=10, padx=10)

lpas.grid(row=2,column=1)
pas.grid(row=2,column=2,pady=10, padx=10)

ldob.grid(row=3,column=1)
dob.grid(row=3,column=2,pady=10, padx=10)

lphone.grid(row=4,column=1)
phone.grid(row=4,column=2,pady=10, padx=10)

ladhaar.grid(row=5,column=1)
adhaar.grid(row=5,column=2,pady=10, padx=10)

lpan.grid(row=6,column=1)
pan.grid(row=6,column=2,pady=10, padx=10)

lbalance.grid(row=7,column=1)
balance.grid(row=7,column=2,pady=10, padx=10)

label.grid(row=9,column=2)

myButton.grid(row=8,column=2,columnspan=2,pady=2, padx=4)

frame.grid(row=0,column=0)

m.mainloop()

