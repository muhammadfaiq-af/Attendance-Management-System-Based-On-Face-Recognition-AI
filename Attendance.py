from random import paretovariate
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
import csv
from tkinter import filedialog

mydata = []
class attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance System Using AI Technique Face Recognition")
        self.root.wm_iconbitmap("E:\FYP\Icon.png")

        # Variables
        self.varattid = StringVar()
        self.varroll = StringVar()
        self.varname = StringVar()
        self.vardep = StringVar()
        self.vartime = StringVar()
        self.vardate = StringVar()
        self.varattstatus = StringVar()

          # First Image 
        img = Image.open(r"E:\FYP\smart-attendance.jpg")
        img = img.resize((800,200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        flbl = Label(self.root, image = self.photoimg)
        flbl.place(x = 200, y = 0, width = 1000, height = 300)
        label = Label(self.root, text = "ATTENDANCE MANAGMENT SYSTEM", font = ("times new roman", 30, "bold"))
        label.place(x = 20, y = 250, width = 1366, height = 45)


        main_frame = Frame(self.root, bd = 4, bg = "white")
        main_frame.place(x = 8, y = 290, width = 1345, height =  630)

        # Left Frame

        leftframe = LabelFrame(main_frame, bd = 4, bg = "white", relief = RIDGE, text = "Student Attendance Details", font =("times new roman", 12, "bold"))
        leftframe.place(x = 20, y = 20, width = 600, height = 380)

        left_inside_frame = Frame(leftframe, bd = 4, relief = RIDGE, bg = "white")
        left_inside_frame.place(x = 10, y = 15, width = 570, height =  320)



        # Student ID label
        attendanceidlbl = Label(left_inside_frame, text = "Attendance ID * :", font = ("times new roman", 12, "bold"), bg = "white")
        attendanceidlbl.grid(row = 0, column = 0, padx = 10, sticky=W)

        attendanceidentry = ttk.Entry(left_inside_frame, width = 15,textvariable = self.varattid, font =("times new roman", 12, "bold"))
        attendanceidentry.grid(row = 0, column = 1, padx = 5, pady = 5, sticky=W)

        rolllbl = Label(left_inside_frame, text = "Roll no * :", font = ("times new roman", 12, "bold"), bg = "white")
        rolllbl.grid(row = 0, column = 2, padx = 5, sticky=W)

        rollentry = ttk.Entry(left_inside_frame, width = 15, textvariable = self.varroll, font =("times new roman", 12, "bold"))
        rollentry.grid(row = 0, column = 3, padx = 1, pady = 5, sticky=W)

        namelbl = Label(left_inside_frame, text = "Name * :", font = ("times new roman", 12, "bold"), bg = "white")
        namelbl.grid(row = 1, column = 0, padx = 10, sticky=W)

        nameentry = ttk.Entry(left_inside_frame, width = 15, textvariable = self.varname, font =("times new roman", 12, "bold"))
        nameentry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky=W)

        deplbl = Label(left_inside_frame, text = "Department * :", font = ("times new roman", 12, "bold"), bg = "white")
        deplbl.grid(row = 1, column = 2, padx = 5, sticky=W)

        depentry = ttk.Entry(left_inside_frame, width = 15, textvariable = self.vardep, font =("times new roman", 12, "bold"))
        depentry.grid(row = 1, column = 3, padx = 0, pady = 5, sticky=W)

        datelbl = Label(left_inside_frame, text = "Date * :", font = ("times new roman", 12, "bold"), bg = "white")
        datelbl.grid(row = 2, column = 0, padx = 9, sticky=W)

        dateentry = ttk.Entry(left_inside_frame, width = 15, textvariable = self.vardate, font =("times new roman", 12, "bold"))
        dateentry.grid(row = 2, column = 1, padx = 5, pady = 5, sticky=W)

        timelbl = Label(left_inside_frame, text = "Time * :", font = ("times new roman", 12, "bold"), bg = "white")
        timelbl.grid(row = 2, column = 2, padx = 8, sticky=W)

        timeentry = ttk.Entry(left_inside_frame, width = 15,textvariable = self.vartime, font =("times new roman", 12, "bold"))
        timeentry.grid(row = 2, column = 3, padx = 1, pady = 5, sticky=W)

        attstatuslbl = Label(left_inside_frame, text = "Attendance Status * :", font = ("times new roman", 12, "bold"), bg = "white")
        attstatuslbl.grid(row = 5, column = 1, padx = 6, sticky=W)

        self.attstatus = ttk.Combobox(left_inside_frame, width = 12, textvariable = self.varattstatus, font = ("times new roman", 12, "bold"), state = "readonly")
        self.attstatus["values"] = ("Status", "Present", "Absent")
        self.attstatus.grid(row = 5, column = 2)
        self.attstatus.current(0)

        # button frame

        btnframe = Frame(left_inside_frame, bd  = 0, relief=RIDGE, bg = "white")
        btnframe.place(x = 5, y = 220, width = 550, height = 40)

        btnexport = Button(btnframe, text = "Emport csv", command = self.exportcsv, font =("times new roman", 12, "bold"), bg = "blue", fg = "white", width = 14, cursor = "hand2" )
        btnexport.grid(row = 0, column = 0)

        btnimport = Button(btnframe, text = "Import csv", command = self.importcsv, font =("times new roman", 12, "bold"), bg = "blue", fg = "white", width = 14, cursor = "hand2" )
        btnimport.grid(row = 0, column = 1)

        # btnupdate = Button(btnframe, text = "Update",  font =("times new roman", 12, "bold"), bg = "blue", fg = "white", width = 14, cursor = "hand2" )
        # btnupdate.grid(row = 0, column = 2)

        btnreset = Button(btnframe, text = "Reset",command = self.reset, font =("times new roman", 12, "bold"), bg = "blue", fg = "white", width = 15, cursor = "hand2" )
        btnreset.grid(row = 0, column = 2)

        


        # Right Frame

        rightframe = LabelFrame(main_frame, bd = 4, bg = "white", relief = RIDGE, text = "Attendance Details", font =("times new roman", 12, "bold"))
        rightframe.place(x = 650, y = 20, width = 650, height = 380)

        right_inside_frame = Frame(rightframe, bd  = 4, relief=RIDGE, bg = "white")
        right_inside_frame.place(x = 10, y = 15, width = 620, height = 320)

        scrollx = ttk.Scrollbar(right_inside_frame, orient = HORIZONTAL)
        scrolly = ttk.Scrollbar(right_inside_frame, orient = VERTICAL)

        self.attreport = ttk.Treeview(right_inside_frame, column=("ID",  "Name","Roll no", "Department", "Time", "Date", "Attendance"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set) 
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)

        scrollx.config(command = self.attreport.xview)
        scrolly.config(command = self.attreport.yview)

        self.attreport.heading("ID", text = "Attendance ID")
        self.attreport.heading("Name", text = "Name")
        self.attreport.heading("Roll no", text = "Roll No")
        self.attreport.heading("Department", text = "Department")
        self.attreport.heading("Date", text = "Date")
        self.attreport.heading("Time", text = "Time")
        self.attreport.heading("Attendance", text = "Attendance status")

        self.attreport["show"] = "headings"

        self.attreport.column("ID", width = 100)
        self.attreport.column("Name", width = 100)
        self.attreport.column("Roll no", width = 100) 
        self.attreport.column("Department", width = 100)
        self.attreport.column("Date", width = 100)
        self.attreport.column("Time", width = 100)
        self.attreport.column("Attendance", width = 100)

        self.attreport.pack(fill = BOTH, expand = 1)
        self.attreport.bind("<ButtonRelease>", self.getcursor)

        # Fetch Data

    def fetchdata(self, rows):
      self.attreport.delete(*self.attreport.get_children())
      for i in rows:
        self.attreport.insert("", END, values = i)
    

    def importcsv(self):
      global mydata
      mydata.clear()
      filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV File", "*.csv"), ("AlL File", "*.*")), parent = self.root)
      with open(filename) as myfile:
        csvread = csv.reader(myfile, delimiter = ",")
        for i in csvread:
          mydata.append(i)
        self.fetchdata(mydata)

    
    def exportcsv(self):
      try:
        if len(mydata) < 1:
          messagebox.showerror("Error", "No Data in The Tabel", parent = self.root)
          return False
        filename = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV File", "*.csv"), ("AlL File", "*.*")), parent = self.root)
        with open(filename, mode = "w", newline = "") as myfile:
          export = csv.writer(myfile, delimiter = ",")
          for i in mydata:
            export.writerow(i)
          messagebox.showinfo("Data Export", "Your Data Exported to " + os.path.basename(filename) + " successfully")

      except Exception as es:
        messagebox.showerror("Error", f"Due To : {str(es)}", parent = self.root)


    def getcursor(self, event = ""):
      cursorrow = self.attreport.focus()
      content = self.attreport.item(cursorrow)
      rows = content['values']
      self.varattid.set(rows[0])
      self.varname.set(rows[1])
      self.varroll.set(rows[2])
      self.vardep.set(rows[3])
      self.vardate.set(rows[4])
      self.vartime.set(rows[5])
      self.varattstatus.set(rows[6])

    def reset(self):
      self.varattid.set("")
      self.varname.set("")
      self.varroll.set("")
      self.vardep.set("")
      self.vardate.set("")
      self.vartime.set("")
      self.varattstatus.set("")











if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()