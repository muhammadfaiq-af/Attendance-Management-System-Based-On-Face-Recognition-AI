import tkinter as tk
from tkinter import*
from tkinter import ttk
from weakref import finalize
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os


class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance System Using AI Technique Face Recognition")
        self.root.wm_iconbitmap("E:\FYP\Icon.png")

        title_lbl = Label(self.root, text = "Developer's Information", font = ("times new roman", 35, "bold"), bg = "black", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1366, height = 55)

        image_top = Image.open("E:\FYP\Developer.jpg")
        image_top = image_top.resize((1366, 680), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x = 0, y = 55, width = 1366, height = 680)

        # Frame

        mainframe = Frame(f_lbl, bd = 2, bg = "white")
        mainframe.place(x=850, y=0, width= 500, height=600)

        image_top1 = Image.open("E:\FYP\IMG_0384.jpg")
        image_top1 = image_top1.resize((200,250), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(image_top1)

        f_lbl1 = Label(mainframe, image = self.photoimg_top1)
        f_lbl1.place(x = 300, y = 0, width = 200, height = 250)

         # deve label
        devlbl = Label(mainframe, text = "Muhammad Faiq", font =("times new roman", 12, "bold"), bg = "white")
        devlbl.place(x=0, y=5)

        devlbl1 = Label(mainframe, text = "BS Computer Science", font =("times new roman", 12, "bold"), bg = "white")
        devlbl1.place(x=0, y=40)

        devlbl2 = Label(mainframe, text = "Batch 2017-21", font =("times new roman", 12, "bold"), bg = "white")
        devlbl2.place(x=0, y=75)

        devlbl2 = Label(mainframe, text = "Final Year Project", font =("times new roman", 12, "bold"), bg = "white")
        devlbl2.place(x=60, y=110)

        devlbl3 = Label(mainframe, text = "Real Time Attendance System Based on AI", font =("times new roman", 12, "bold"), bg = "white")
        devlbl3.place(x=0, y=145)

        devlbl4 = Label(mainframe, text = "SUPERVISOR", font =("times new roman", 12, "bold"), bg = "white")
        devlbl4.place(x=60, y=180)

        devlbl4 = Label(mainframe, text = "Sir Dr NAVEED ISLAM", font =("times new roman", 12, "bold"), bg = "white")
        devlbl4.place(x=30, y=215)

        devlbl5 = Label(mainframe, text = "Islamia College University Peshawar", font =("times new roman", 12, "bold"), bg = "white")
        devlbl5.place(x=0, y=250)





if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()