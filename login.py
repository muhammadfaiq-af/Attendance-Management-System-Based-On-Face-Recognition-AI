import tkinter as tk
from tkinter import*
from tkinter import ttk
from weakref import finalize
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
import numpy as np
import pandas as pd
from time import strftime
from datetime import date, datetime
from Main import face_Recognition

def main():
    win = Tk()
    app = Login(win)
    win.mainloop()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Login Page")
        self.root.wm_iconbitmap("E:\FYP\Icon.png")

        self.sec1 = StringVar()
        self.sec2 = StringVar()

        img = Image.open(r"E:\FYP\Login.jpg")
        img = img.resize((1366,768), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_bg = Label(self.root, image = self.photoimg)
        lbl_bg.place(x=0, y=0, width = 1366, height = 768)

        frame = Frame(self.root, bg = "black")
        frame.place(x = 530, y = 150, width = 340, height =  450)

        img1 = Image.open(r"E:\FYP\login.png")
        img1 = img1.resize((100,100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl1 = Label(frame, image = self.photoimg1, bg = "black", borderwidth=0)
        lbl1.place(x = 120, y = 5, width=100, height=100)

        lbl_t = Label(frame, text = "Get Started", font=("times new roman", 20, "bold"), fg="white", bg = "black")
        lbl_t.place(x = 100, y = 110)

        emaillbl = Label(frame, text = "Email", font = ("times new roman", 15, "bold"), fg="white", bg = "black")
        emaillbl.place(x = 30, y  =155)

        self.emailentry = ttk.Entry(frame, width = 15, font =("times new roman", 12, "bold"))
        self.emailentry.place(x = 130, y = 155, width=150)

        passlbl = Label(frame, text = "Password", font = ("times new roman", 15, "bold"), fg="white", bg = "black")
        passlbl.place(x = 30, y = 188)

        self.passentry = ttk.Entry(frame, width = 15, font =("times new roman", 12, "bold"))
        self.passentry.place(x = 130, y = 188, width=150)

        img2 = Image.open(r"E:\FYP\user.png")
        img2 = img2.resize((25,25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(frame, image = self.photoimg2, bg = "black", borderwidth=0)
        lblimg2.place(x = 5, y = 155)

        img3 = Image.open(r"E:\FYP\password.png")
        img3 = img3.resize((25,25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(frame, image = self.photoimg3, bg = "black", borderwidth=0)
        lblimg3.place(x = 5, y = 188)

        # LOGIN BUTTON
        btnlogin = Button(frame, command=self.login, text = "Login", font = ("times new roman", 15, "bold"), bd = 0, relief=RIDGE, fg = "white", bg = "Red", activeforeground="white", activebackground="red")
        btnlogin.place(x = 120, y = 230, width=120, height=30)

        # Register Button
        btnreg = Button(frame, text = "New User Register",command=self.regwin, font = ("times new roman", 10, "bold"), bd = 0, relief=RIDGE, fg = "white", bg = "black", activeforeground="white", activebackground="red")
        btnreg.place(x = 30, y = 270, width=120)

        #Forgot password
        btnpass = Button(frame, text = "Forgot password",command=self.forgot, font = ("times new roman", 10, "bold"), bd = 0, relief=RIDGE, fg = "white", bg = "black", activeforeground="white", activebackground="red")
        btnpass.place(x = 24, y = 290, width=120)


    def regwin(self):
        self.newwin = Toplevel(self.root)
        self.app = register(self.newwin)


    def login(self):
        if self.emailentry.get() == "" or self.passentry.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")

        elif self.emailentry.get() == "faiq" and self.passentry.get() == "anamfaiq":
            messagebox.showinfo("Success", "Welcome to The Attendance System Based on AI")
        else:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
            mycursor = con.cursor()
            mycursor.execute("select * from Register where Email=%s and Password=%s",(
                                                                                        self.emailentry.get(),
                                                                                        self.passentry.get()

            ))   
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Email and Password")
            else:
                openmain = messagebox.askyesno("YesNo", "Access only Admin")
                if openmain > 0:
                    self.newwin = Toplevel(self.root)
                    self.app = face_Recognition(self.newwin)
                else:
                    if not openmain:
                        return
            con.commit()
            con.close()


    def reset(self):
        if self.sec1entry.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question", parent = self.root2)
        elif self.sec2entry.get() == "":
            messagebox.showerror("Error", "Please Enter The Answer", parent = self.root2)
        elif self.newpassentry.get() == "":
            messagebox.showerror("error", "Please Enter the Password", parent = self.root2)
        else:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
            mycursor = con.cursor()
            query = ("select * from Register where Email=%s and SecurityQuestion=%s and SecurityAnswer=%s")
            value = (self.emailentry.get(), self.sec1entry.get(), self.sec2entry.get(),)
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            print(row)
            if row==None:
                messagebox.showerror("Error", "Please Enter the Correct Answer",parent = self.root2)

            else:
                query1 = ("update Register set Password=%s where Email=%s")
                value1 = (self.newpassentry.get(), self.emailentry.get())
                mycursor.execute(query1,value1)
                print(row)
                con.commit()
                con.close()
                messagebox.showinfo("Info", "Your Password has been Reset, please Login with New Password", parent = self.root2) 
                self.root2.destroy()



    def forgot(self):
        if self.emailentry.get() == "":
            messagebox.showerror("Error", "Please Enter Email address to reset password")
        else:
            con = mysql.connector.connect(host = "localhost", user = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
            mycursor = con.cursor() 
            query = ("select * from Register where Email=%s")
            value = (self.emailentry.get(),)
            mycursor.execute(query,value)
            row = mycursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error", "Please Enter the Valid Email")
            else:
                con.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.configure(background = 'black')
                self.root2.geometry("340x450+530+150")

                l = Label(self.root2, text = "Forgot Password",  font = ("times new roman", 20, "bold"), fg = "White", bg = "black")
                l.place(x = 5, y = 5, relwidth=1)

                self.sec1lbl = Label(self.root2, text = "Select Security Question", font = ("times new roman", 15, "bold"), fg = "Red", bg = "black")
                self.sec1lbl.place(x = 5, y = 75, relwidth=1)
                
                self.sec1entry = ttk.Combobox(self.root2, font = ("times new roman", 10, "bold"), state="readonly")
                self.sec1entry["values"] = ("Select", "Your Birth place", "Your Friend Name", "Your Father Name", "Your Pet Name")
                self.sec1entry.place(x = 80, y = 113, width = 170, height=30)
                self.sec1entry.current(0)


                self.sec2lbl = Label(self.root2, text = "Security Answer", font = ("times new roman", 15, "bold"), fg = "Red", bg = "black")
                self.sec2lbl.place(x = 5, y = 150, relwidth=1)
                
                self.sec2entry = ttk.Entry(self.root2, font = ("times new roman", 15, "bold"))
                self.sec2entry.place(x = 80, y = 190, width=170)

                self.newpass = Label(self.root2, text = "New Password", font = ("times new roman", 15, "bold"), fg = "Red", bg = "black")
                self.newpass.place(x = 5, y = 230, relwidth=1)
                
                self.newpassentry = ttk.Entry(self.root2, font = ("times new roman", 15, "bold"))
                self.newpassentry.place(x = 80, y = 270, width=170)

                btn = Button(self.root2, text = "Reset", command=self.reset, font = ("times new roman", 15, "bold"), fg = "black", bg = "Red",cursor="hand2")
                btn.place(x = 100, y = 330, width=120, height=30)







 #Register Class           
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
        b1 = Button(frame, image = self.photoimg1,command=self.reglogin, borderwidth=0, cursor="hand2")
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
        
    def reglogin(self):
        self.root.destroy()




if __name__ == "__main__":
    main()
         
