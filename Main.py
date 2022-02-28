import tkinter as tk
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from Student import student
from TrainData import train
from FaceDetection import facerecognition
from Attendance import attendance
from Developer import developer
from Help import help
import os
from time import strftime
from datetime import date, datetime


class face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance System Using AI Technique Face Recognition")
        self.root.wm_iconbitmap("E:\FYP\Icon.png")
        
        #  # First Image 
        # img = Image.open(r"C:\Users\Muhammad Faiq\Images\download (1).png")
        # img = img.resize((500,200), Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img)
        
        # lbl1 = Label(self.root, image = self.photoimg)
        # lbl1.place(x = 0, y = 0, width = 500, height = 150)

        # # Second Image
        
        # img1 = Image.open("C:/Users/Muhammad Faiq/Images/FACE-RECOGNITION_blog_800x400@1x.png")
        # img1 = img1.resize((500,200), Image.ANTIALIAS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # lbl1 = Label(self.root, image = self.photoimg1)
        # lbl1.place(x = 500, y = 0, width = 500, height = 150)

        
        # # 3rd Image
        
        # img2 = Image.open(r"C:\Users\Muhammad Faiq\Images\download.png")
        # img2 = img2.resize((500,200), Image.ANTIALIAS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        
        # lbl1 = Label(self.root, image = self.photoimg2)
        # lbl1.place(x = 1000, y = 0, width = 500, height = 150)

        
        # Background Image
        
        img3 = Image.open(r"E:\FYP\bg2.png")
        img3 = img3.resize((1366,720), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bglbl = Label(self.root, image = self.photoimg3)
        bglbl.place(x = 0, y = 0, width = 1366, height = 720)
        
        # Title
        
        title_lbl = Label(bglbl, text = "Attendance System Using AI Technique Face Recognition", font = ("times new roman", 35, "bold"), bg = "black", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1366, height = 60)
        #Time

        def time():
            string = strftime('%H:%M:%S %p')
            lbltime.config(text = string)
            lbltime.after(1000,time)

        lbltime = Label(bglbl, font = ("times new roman", 14, 'bold'), background='white', foreground='black')
        lbltime.place(x=0, y=600, width=110, height = 30)
        time()


        # Student Details Button
        
        btnstdetails = Image.open(r"E:\FYP\1.png")
        btnstdetails = btnstdetails.resize((150,150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(btnstdetails)
        
        b1 = tk.Button(bglbl, image = self.photoimg4, command = self.studentdetails, cursor = "hand2")
        b1.place(x = 65, y = 100, width  = 150, height = 150)

        b1_lbl = tk.Button(bglbl, text = "Student Details", command = self.studentdetails, cursor = "hand2", font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        b1_lbl.place(x = 65, y = 250, width  = 150, height = 40)


        # Face detection Button
        
        btnfacedetect = Image.open(r"E:\FYP\2.png")
        btnfacedetect = btnfacedetect.resize((150,150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(btnfacedetect)
        
        b1 = tk.Button(bglbl, image = self.photoimg5, cursor = "hand2", command = self.facedetection)
        b1.place(x = 400, y = 100, width  = 150, height = 150)

        b1_lbl = tk.Button(bglbl, text = "Face Detector", cursor = "hand2", command = self.facedetection, font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        b1_lbl.place(x = 400, y = 250, width  = 150, height = 40)


        # Attendance Button
        
        btnattendance = Image.open(r"E:\FYP\attendant-list.png")
        btnattendance = btnattendance.resize((150,150), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(btnattendance)
        
        b1 = tk.Button(bglbl, image = self.photoimg6, cursor = "hand2", command = self.attendance)
        b1.place(x = 800, y = 100, width  = 150, height = 150)

        b1_lbl = tk.Button(bglbl, text = "Attendance", cursor = "hand2", command = self.attendance, font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        b1_lbl.place(x = 800, y = 250, width  = 150, height = 40)


        # Help Button
        
        btnhelp = Image.open(r"E:\FYP\info-147927_1280.png")
        btnhelp = btnhelp.resize((150,150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(btnhelp)
        
        b1 = tk.Button(bglbl, image = self.photoimg7, cursor = "hand2",command=self.help)
        b1.place(x = 1150, y = 100, width  = 150, height = 150)

        b1_lbl = tk.Button(bglbl, text = "Help!", cursor = "hand2",command=self.help, font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        b1_lbl.place(x = 1150, y = 250, width  = 150, height = 40)


        # Train Data Button
        
        btntrain = Image.open(r"E:\FYP\Setting.png")
        btntrain = btntrain.resize((150,150), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(btntrain)
        
        b1 = tk.Button(bglbl, image = self.photoimg8, cursor = "hand2",command = self.traindata )
        b1.place(x = 65, y = 350, width  = 150, height = 150)

        b1_lbl = tk.Button(bglbl, text = "Training Images", cursor = "hand2", command = self.traindata, font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        b1_lbl.place(x = 65, y = 500, width  = 150, height = 40)


        # Image Button
        
        btnimage = Image.open(r"E:\FYP\3.png")
        btnimage = btnimage.resize((150,150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(btnimage)
        
        b1 = tk.Button(bglbl, image = self.photoimg9, cursor = "hand2", command = self.openimages)
        b1.place(x = 400, y = 350, width  = 150, height = 150)

        b1_lbl = tk.Button(bglbl, text = "Sample Images", cursor = "hand2", command = self.openimages, font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        b1_lbl.place(x = 400, y = 500, width  = 150, height = 40)


        # Developer Button
        
        btndeveloper = Image.open(r"E:\FYP\coding.png")
        btndeveloper = btndeveloper.resize((150,150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(btndeveloper)
        
        b1 = tk.Button(bglbl, image = self.photoimg10, cursor = "hand2", command = self.developer)
        b1.place(x = 800, y = 350, width  = 150, height = 150)

        b1_lbl = tk.Button(bglbl, text = "Developer Info", cursor = "hand2", command = self.developer,  font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        b1_lbl.place(x = 800, y = 500, width  = 150, height = 40)

        # Exit Button
        
        btnExit = Image.open(r"E:\FYP\4.png")
        btnExit = btnExit.resize((150,150), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(btnExit)
        
        b1 = tk.Button(bglbl, image = self.photoimg11, cursor = "hand2",command=self.exit)
        b1.place(x = 1150, y = 350, width  = 150, height = 150)

        b1_lbl = tk.Button(bglbl, text = "Exit", cursor = "hand2",command=self.exit, font = ("times new roman", 15, "bold"), bg = "white", fg = "black")
        b1_lbl.place(x = 1150, y = 500, width  = 150, height = 40)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition", "Are you Sure to exit This Project?", parent = self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return
    def openimages(self):
        os.startfile("E:\FYP\Photo_Sample")

        # Functions on button
    def studentdetails(self):
        self.newwindow = Toplevel(self.root)
        self.st= student(self.newwindow) 

    def traindata(self):
        self.newwindow = Toplevel(self.root)
        self.st= train(self.newwindow) 

    def facedetection(self):
        self.newwindow = Toplevel(self.root)
        self.st= facerecognition(self.newwindow) 

    def attendance(self):
        self.newwindow = Toplevel(self.root)
        self.st = attendance(self.newwindow)

    def developer(self):
        self.newwindow = Toplevel(self.root)
        self.st = developer(self.newwindow)

    def help(self):
        self.newwindow = Toplevel(self.root)
        self.st = help(self.newwindow)


           



if __name__ == "__main__":
    root = Tk()
    obj = face_Recognition(root)
    root.mainloop()