import tkinter as tk
from tkinter import*
from tkinter import ttk
from weakref import finalize
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
from PIL import Image, ImageDraw

class help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance System Using AI Technique Face Recognition")
        self.root.wm_iconbitmap("E:\FYP\Icon.png")

        title_lbl = Label(self.root, text = "Help Desk", font = ("times new roman", 35, "bold"), bg = "black", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1366, height = 55)

        image_top = Image.open("E:\FYP\Help.jpg")
        image_top = image_top.resize((1366, 680), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x = 0, y = 55, width = 1366, height = 680)

        devlbl = Label(f_lbl, text = "Please Conatct On My Official Email:faiqqadri83@gmail.com", font =("times new roman", 25, "bold"),bg = "black", fg = "white")
        devlbl.place(x=250, y=600)

        


if __name__ == "__main__":
    root = Tk()
    obj = help(root)
    root.mainloop()