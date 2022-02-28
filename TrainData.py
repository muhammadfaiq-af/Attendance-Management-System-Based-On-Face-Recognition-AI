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


class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance System Using AI Technique Face Recognition")
        self.root.wm_iconbitmap("E:\FYP\Icon.png")


        title_lbl = Label(self.root, text = "Train Data Set", font = ("times new roman", 35, "bold"), bg = "black", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1366, height = 55)

        image_top = Image.open("E:\FYP\Trainning.jpg")
        image_top = image_top.resize((1366, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x = 0, y = 55, width = 1366, height = 325)



        btntraindata = Button(self.root, text = "TRAIN DATA SET", command =self.trainclassifier, font =("times new roman", 22, "bold"), bg = "black", fg = "white", width = 15, cursor = "hand2" )
        btntraindata.place(x = 0, y = 380, width = 1366, height = 60)





        image_bottom = Image.open("E:\FYP\Trainning.jpg")
        image_bottom = image_bottom.resize((1366, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(image_bottom)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x = 0, y = 440, width = 1366, height = 325)

       
    def trainclassifier(self):
        datadir = ("E:\FYP\Photo_Sample")
        path = [os.path.join(datadir, file) for file in os.listdir(datadir)]  # yeh List Comprehensive hai
        
        faces = []
        id = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale Image Converted
            imagenp = np.array(img, 'uint8')
            idnp = int(os.path.split(image)[1].split('-')[1])

            faces.append(imagenp)
            id.append(idnp)

            cv.imshow("Trainning", imagenp)
            cv.waitKey(1) == 13
        
        id = np.array(id)


        # Train Classifier

        clf = cv.face.LBPHFaceRecognizer_create()
        clf.train(faces, id)
        clf.write("Classifier.xml")
        cv.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data sets Completed ")





if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()