import tkinter as tk
from tkinter import*
from tkinter import ttk
from weakref import finalize
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
from mysql.connector.errors import DatabaseError
import numpy as np
import pandas as pd
from time import strftime
from datetime import date, datetime
import mysql.connector

class register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Registration Form")

        self.fname = StringVar()
        self.lname = StringVar()
        self.con = StringVar()
        self.email = StringVar()
        self.sec1 = StringVar()
        self.sec2 = StringVar()
        self.pass1 = StringVar()
        self.pass2 = StringVar()

        img = Image.open(r"E:\FYP\Login.jpg")
        img = img.resize((1366,768), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_bg = Label(self.root, image = self.photoimg)
        lbl_bg.place(x=0, y=0, width = 1366, height = 768)

        frame = Frame(self.root, bg="white")
        frame.place(x = 350, y = 130, width = 700, height =  500)

        reglbl = Label(frame, text = "Regiter Here", font = ("times new roman", 20, "bold"), fg = "blue", bg = "white")
        reglbl.place(x = 5, y = 5)

        flbl = Label(frame, text = "First Name", font = ("times new roman", 15, "bold"), fg = "black", bg = "white")
        flbl.place(x = 15, y = 60)
        
        fentry = ttk.Entry(frame,textvariable= self.fname, font = ("times new roman", 15, "bold"))
        fentry.place(x = 170, y = 60, width=120)

        llbl = Label(frame, text = "Last Name", font = ("times new roman", 15, "bold"), fg = "black", bg = "white")
        llbl.place(x = 300, y = 60)
        
        lentry = ttk.Entry(frame,textvariable=self.lname, font = ("times new roman", 15, "bold"))
        lentry.place(x = 450, y = 60, width=120)

        clbl = Label(frame, text = "Contact No", font = ("times new roman", 15, "bold"), fg = "black", bg = "white")
        clbl.place(x = 15, y = 100)
        
        centry = ttk.Entry(frame,textvariable=self.con, font = ("times new roman", 15, "bold"))
        centry.place(x = 170, y = 100, width=120)

        elbl = Label(frame, text = "Email", font = ("times new roman", 15, "bold"), fg = "black", bg = "white")
        elbl.place(x = 300, y = 100)
        
        eentry = ttk.Entry(frame,textvariable=self.email, font = ("times new roman", 15, "bold"))
        eentry.place(x = 450, y = 100, width=120)

        sec1lbl = Label(frame, text = "Select Security Question", font = ("times new roman", 10, "bold"), fg = "black", bg = "white")
        sec1lbl.place(x = 15, y = 140)
        
        sec1entry = ttk.Combobox(frame,textvariable=self.sec1, font = ("times new roman", 10, "bold"), state="readonly")
        sec1entry["values"] = ("Select", "Your Birth place", "Your Friend Name", "Your Father Name", "Your Pet Name")
        sec1entry.place(x = 170, y = 140, width = 170, height=30)
        sec1entry.current(0)


        sec2lbl = Label(frame, text = "Security Answer", font = ("times new roman", 10, "bold"), fg = "black", bg = "white")
        sec2lbl.place(x = 340, y = 140)
        
        sec2entry = ttk.Entry(frame,textvariable=self.sec2, font = ("times new roman", 15, "bold"))
        sec2entry.place(x = 450, y = 140, width=160)

        pass1lbl = Label(frame, text = "Enter Password", font = ("times new roman", 13, "bold"), fg = "black", bg = "white")
        pass1lbl.place(x = 15, y = 180)
        
        pass1entry = ttk.Entry(frame,textvariable=self.pass1, font = ("times new roman", 15, "bold"))
        pass1entry.place(x = 170, y = 180, width=120)

        pass2lbl = Label(frame, text = "Confirm Password", font = ("times new roman", 13, "bold"), fg = "black", bg = "white")
        pass2lbl.place(x = 300, y = 180)
        
        pass2entry = ttk.Entry(frame,textvariable=self.pass2, font = ("times new roman", 15, "bold"))
        pass2entry.place(x = 450, y = 180, width=120)

        self.check = IntVar()
        chbtn = Checkbutton(frame,variable=self.check, text = "I Agree To the Terms and Conditions", font = ("times new roman", 14, "bold"), bg = "white", onvalue=1, offvalue=0)
        chbtn.place(x = 170, y = 240)

        img2 = Image.open(r"E:\FYP\Register-Now-button-red-removebg-preview.png")
        img2 = img2.resize((130, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(frame, image = self.photoimg2,command=self.reg, borderwidth=0, cursor="hand2")
        b1.place(x = 200, y = 290, width = 130)


        img1 = Image.open(r"E:\FYP\images-removebg-preview.png")
        img1 = img1.resize((130, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image = self.photoimg1, borderwidth=0, cursor="hand2")
        b1.place(x = 380, y = 290, width = 130)

    #Function dec

    def reg(self):
        if self.fname.get() == "" or self.lname.get()== "" or self.con.get() == "" or self.email.get() == "" or self.pass1.get() == "" or self.pass2.get() == ""  or self.sec1.get() == "Select" or self.sec2.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        elif self.pass1.get() != self.pass2.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same")
        elif self.check.get() == 0:
            messagebox.showerror("Error", "Please Agree to our Terms and Condition")
        else:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
            mycursor = con.cursor()
            query = ("select * from Register where email=%s")
            value = (self.email.get(),)
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "Email Already Exist, Please Try Another Email")
            else:
                mycursor.execute("insert into Register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.fname.get(),
                                                                                        self.lname.get(),
                                                                                        self.con.get(),
                                                                                        self.email.get(),
                                                                                        self.sec1.get(),
                                                                                        self.sec2.get(),
                                                                                        self.pass1.get()
                                                                                                        ))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Register Successfully")
            


if __name__ == "__main__":
    root = Tk()
    obj = register(root)
    root.mainloop()