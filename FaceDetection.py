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


class facerecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance System Using AI Technique Face Recognition")
        self.root.wm_iconbitmap("E:\FYP\Icon.png")

        title_lbl = Label(self.root, text = "Face Detection", font = ("times new roman", 35, "bold"), bg = "blue", fg = "red")
        title_lbl.place(x = 500, y = 0)

        image_top = Image.open("E:\FYP\Face detection.jpg")
        image_top = image_top.resize((1366, 680), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x = 0, y = 55, width = 1366, height = 680)

        btnfacedetection = Button(f_lbl, text = "Detect Face", command = self.recognition, font =("times new roman", 22, "bold"), bg = "red", fg = "white", width = 15, cursor = "hand2" )
        btnfacedetection.place(x = 580, y = 600, width = 200, height = 50)


    # Attendance 
    def attendance(self, st, name, rollno, dep):
        with open(r"E:\FYP\CSV\ATTENDANCE.csv", "r+", newline="\n") as f:
            mydatalist = f.readlines()
            namelist = []
            for line in mydatalist:
                entry = line.split((","))
                namelist.append(entry[0])
            if ((st not in namelist) and (name not in namelist) and (rollno not in namelist) and (dep not in namelist)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt = now.strftime("%H:%M:%S")
                f.writelines(f"\n{st}, {name}, {rollno}, {dep}, {dt}, {d1}, Present")



        # Face Detection

    def recognition(self):
        def drawboundary(image, classifier, scalefactor, minneighbour, color, text, clf):
            greyimage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            feature = classifier.detectMultiScale(greyimage, scalefactor, minneighbour)

            cord = []

            for (x,y,w,h) in feature:
                cv.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 3)
                id, predict = clf.predict(greyimage[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
                mycursor = conn.cursor()

                mycursor.execute("select Student_ID from student_details where Student_ID=" + str(id))
                st = mycursor.fetchone()
                st = "+".join(st)
                    
                mycursor.execute("select Name from student_details where Student_ID=" + str(id))
                name = mycursor.fetchone()
                name = "+".join(name)

                mycursor.execute("select Roll_No from student_details where Student_ID=" + str(id))
                rollno = mycursor.fetchone()
                rollno = "+".join(rollno)

                mycursor.execute("select Department from student_details where Student_ID=" + str(id))
                dep = mycursor.fetchone()
                dep = "+".join(dep)

                if confidence > 75:
                    cv.putText(image, f"ID:{st}", (x, y-75), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv.putText(image, f"Rollno:{rollno}", (x, y-55), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv.putText(image, f"Name:{name}", (x, y-30), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv.putText(image, f"Department:{dep}", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    self.attendance(st, name, rollno, dep)
                else:
                    cv.rectangle(image, (x,y), (x+w,y+h), (0,0,0), 3)
                    cv.putText(greyimage, "Unknown face", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                cord = [x,y,w,h]  
            return cord


        def recognize(image, clf, facecascade):
            cord = drawboundary(image, facecascade, 1.1,7, (255,255,255), "Face", clf)
            return image
            
        facecascade = cv.CascadeClassifier("E:\FYP\haarcascade_frontalface_default.xml")
        clf = cv.face.LBPHFaceRecognizer_create()
        clf.read("E:\FYP\Classifier.xml")

        videocap = cv.VideoCapture(0)
        while True:
            ret, image = videocap.read()
            image = recognize(image, clf, facecascade)
            cv.imshow("Welcome To Face Detection", image)
            if cv.waitKey(1) == 13:
                break
                    
        videocap.release()
        cv.destroyAllWindows()

         

if __name__ == "__main__":
    root = Tk()
    obj = facerecognition(root)
    root.mainloop()