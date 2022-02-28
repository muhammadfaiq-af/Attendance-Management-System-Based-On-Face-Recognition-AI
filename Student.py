import tkinter as tk
from tkinter import*
from tkinter import ttk
from weakref import finalize
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Attendance System Using AI Technique Face Recognition")
        self.root.wm_iconbitmap("E:\FYP\Icon.png")

        # Variables

        self.vardep = StringVar()
        self.varcourse = StringVar()
        self.varyear = StringVar()
        self.varsemester = StringVar()
        self.varid = StringVar()
        self.varname = StringVar()
        self.varrollno = StringVar()
        self.vargender = StringVar()
        self.varcontactno = StringVar()
        self.varcnic = StringVar()
        self.varaddress = StringVar()
        self.varemail = StringVar()
        self.varsearch = StringVar()
        self.varsearchcombo = StringVar()


        
        bglbl = Label(self.root, bg = "black")
        bglbl.place(x = 0, y = 0, width = 1366, height = 720)
        
        # Title
        
        title_lbl = Label(bglbl, text = "Student Details", font = ("times new roman", 35, "bold"), bg = "black", fg = "white")
        title_lbl.place(x = 500, y = 0)

        main_frame = Frame(bglbl, bd = 4, bg = "white")
        main_frame.place(x = 5, y = 55, width = 1345, height =  630)

        # Left Frame

        leftframe = LabelFrame(main_frame, bd = 4, bg = "white", relief = RIDGE, text = "Student Details", font =("times new roman", 12, "bold"))
        leftframe.place(x = 60, y = 65, width = 600, height = 550)

        # Label Current Information

        currentinformation = LabelFrame(leftframe, bd = 4, bg = "white", relief = RIDGE, text = "Current  Information", font =("times new roman", 12, "bold"))
        currentinformation.place(x = 5, y = 10, width = 580, height = 120)

        # department Combobox
        deplbl = Label(currentinformation, text = "Department", font =("times new roman", 12, "bold"), bg = "white")
        deplbl.grid(row = 0, column = 0)

        depcombo = ttk.Combobox(currentinformation,textvariable = self.vardep, font =("times new roman", 10, "bold"), state = "readonly")
        depcombo['values'] = ("Select Department", "Computer Science", "Mathematics", "Chemistry", "Physics", "Botny")
        depcombo.current(0)
        depcombo.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)

        # course Combobox
        courselbl = Label(currentinformation, text = "Course", font =("times new roman", 12, "bold"), bg = "white")
        courselbl.grid(row = 0, column = 2)

        coursecombo = ttk.Combobox(currentinformation, textvariable = self.varcourse, font =("times new roman", 10, "bold"), state = "readonly", width = 22)
        coursecombo['values'] = ("Select Course", "Advance Programming", "Advance Pyhton Programming", "Analysis of Algorithm", "Inorganic Chmistry", "Organic Chemistry")
        coursecombo.current(0)
        coursecombo.grid(row = 0, column = 3, padx = 2, pady = 10, sticky = W)


        # Year Combobox 
        yearlbl = Label(currentinformation, text = "Year", font =("times new roman", 12, "bold"), bg = "white")
        yearlbl.grid(row = 1, column = 0)

        yearcombo = ttk.Combobox(currentinformation ,textvariable = self.varyear, font =("times new roman", 10, "bold"), state = "readonly")
        yearcombo['values'] = ("Select Year", "2011 - 15", "2012 - 16", "2013 - 17", "2014 -18", "2015 -19", "2016 -20", "2017 -21", "2018 -22")
        yearcombo.current(0)
        yearcombo.grid(row = 1, column = 1, padx = 2, pady = 10, sticky = W)

        # Semester Combobox
        semesterlbl = Label(currentinformation, text = "Semester", font =("times new roman", 12, "bold"), bg = "white")
        semesterlbl.grid(row = 1, column = 2, padx = 2, pady=10)

        semestercombo = ttk.Combobox(currentinformation, textvariable = self.varsemester, font = ("times new roman", 10, "bold"), state = "readonly", width = 22)
        semestercombo['values'] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semestercombo.current(0)
        semestercombo.grid(row = 1, column = 3, padx = 2, pady = 10, sticky = W)


        # Label Students details

        studenddetails = LabelFrame(leftframe, bd = 4, bg = "white", relief = RIDGE, text = "Student Details", font =("times new roman", 12, "bold"))
        studenddetails.place(x = 5, y = 150, width = 580, height = 350)

        # Student ID label
        studentidlbl = Label(studenddetails , text = "Student ID * :", font =("times new roman", 12, "bold"), bg = "white")
        studentidlbl.grid(row = 0, column = 0, padx = 10, sticky=W)

        studententry = ttk.Entry(studenddetails, textvariable = self.varid, width = 15, font =("times new roman", 12, "bold"))
        studententry.grid(row = 0, column = 1, padx = 10, sticky=W)

        # Student Name label
        studentnamelbl = Label(studenddetails, text = "Name * :", font =("times new roman", 12, "bold"), bg = "white")
        studentnamelbl.grid(row = 0, column = 2, padx = 10, sticky=W)

        studentname = ttk.Entry(studenddetails,textvariable = self.varname, width = 17, font =("times new roman", 12, "bold"))
        studentname.grid(row = 0, column = 3, padx = 0, pady = 13, sticky=W)

        # Student Rollnumber label
        studentrolllbl = Label(studenddetails, text = "Roll No * :", font =("times new roman", 12, "bold"), bg = "white")
        studentrolllbl.grid(row = 1, column = 0, padx = 10, sticky=W)

        studentroll = ttk.Entry(studenddetails ,textvariable = self.varrollno, width = 15, font =("times new roman", 12, "bold"))
        studentroll.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=W)


        # Student Gender label
        studentgenderlbl = Label(studenddetails, text = "Gender :", font =("times new roman", 12, "bold"), bg = "white")
        studentgenderlbl.grid(row = 1, column = 2, padx = 10, sticky=W)


        gendercombo = ttk.Combobox(studenddetails, textvariable = self.vargender, font = ("times new roman", 10, "bold"), state = "readonly", width = 17)
        gendercombo['values'] = ("Select Gender", "Male", "Female", "Others")
        gendercombo.current(0)
        gendercombo.grid(row = 1, column = 3, padx = 0, pady = 13, sticky = W)

        # Student Email label
        studentemaillbl = Label(studenddetails, text = "Email :", font =("times new roman", 12, "bold"), bg = "white")
        studentemaillbl.grid(row = 2, column = 0, padx = 10, sticky=W)

        studentemail = ttk.Entry(studenddetails ,textvariable = self.varemail, width = 15, font =("times new roman", 12, "bold"))
        studentemail.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=W)


        # Student Contact no label
        studentcontactlbl = Label(studenddetails, text = "Contact No :", font =("times new roman", 12, "bold"), bg = "white")
        studentcontactlbl.grid(row = 2, column = 2, padx = 10, sticky=W)

        studentcontact = ttk.Entry(studenddetails ,textvariable = self.varcontactno, width = 17, font =("times new roman", 12, "bold"))
        studentcontact.grid(row = 2, column = 3, padx = 1, pady = 10, sticky=W)

        # Student cnic label
        studentcniclbl = Label(studenddetails, text = "CNIC * :", font =("times new roman", 12, "bold"), bg = "white")
        studentcniclbl.grid(row = 3, column = 0, padx = 10, sticky=W)

        studentcnic = ttk.Entry(studenddetails ,textvariable = self.varcnic, width = 15, font =("times new roman", 12, "bold"))
        studentcnic.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=W)

        # Student address no label
        studentaddresslbl = Label(studenddetails, text = "Address :", font =("times new roman", 12, "bold"), bg = "white")
        studentaddresslbl.grid(row = 3, column = 2, padx = 10, sticky=W)

        studentaddress = ttk.Entry(studenddetails ,textvariable = self.varaddress, width = 17, font =("times new roman", 12, "bold"))
        studentaddress.grid(row = 3, column = 3, padx = 1, pady = 10, sticky=W)

        # Radio Buttons
        self.varradio1 = StringVar()
        radio1 = ttk.Radiobutton(studenddetails, variable = self.varradio1, text = "Take a Photo Sample", value = "Yes")
        radio1.grid(row = 5, column = 0 )

        radio2 = ttk.Radiobutton(studenddetails, variable = self.varradio1, text = "No Photo Sample", value = "No")
        radio2.grid(row = 5, column = 1)

        # button frame

        btnframe = Frame(studenddetails, bd  = 4, relief=RIDGE)
        btnframe.place(x = 5, y = 220, width = 560, height = 100)

        btnsave = Button(btnframe, text = "Save", command = self.adddata,  font =("times new roman", 12, "bold"), bg = "red", fg = "white", width = 14, cursor = "hand2" )
        btnsave.grid(row = 0, column = 0)

        btnupdate = Button(btnframe, text = "Update",command = self.updatedata, font =("times new roman", 12, "bold"), bg = "red", fg = "white", width = 14, cursor = "hand2" )
        btnupdate.grid(row = 0, column = 1)

        btndelete = Button(btnframe, text = "Delete", command = self.deletedata, font =("times new roman", 12, "bold"), bg = "red", fg = "white", width = 14, cursor = "hand2" )
        btndelete.grid(row = 0, column = 2)

        btnreset = Button(btnframe, text = "Reset", command = self.resetdata, font =("times new roman", 12, "bold"), bg = "red", fg = "white", width = 15, cursor = "hand2" )
        btnreset.grid(row = 0, column = 3)

        btntakephoto = Button(btnframe, command = self.photodataset, text = "Take Photo Sample", font =("times new roman", 12, "bold"), bg = "red", fg = "white", width = 15, cursor = "hand2" )
        btntakephoto.grid(row = 1, column = 1, pady = 10)

        btnupdatephoto = Button(btnframe, text = "Update Photo Sample", font =("times new roman", 12, "bold"), bg = "red", fg = "white", width = 15, cursor = "hand2" )
        btnupdatephoto.grid(row = 1, column = 2, pady =10)




        # Right Frame

        rightframe = LabelFrame(main_frame, bd = 4, bg = "white", relief = RIDGE, text = "Student Details", font =("times new roman", 12, "bold"))
        rightframe.place(x = 670, y = 65, width = 600, height = 550)

        # Search System frame

        searchframe = LabelFrame(rightframe, bd = 4, bg = "white", relief = RIDGE, text = "Search System", font =("times new roman", 12, "bold"))
        searchframe.place(x = 5, y = 5  , width = 580, height = 70)

        searchlbl = Label(searchframe, text = "Search By :", font =("times new roman", 12, "bold"), bg = "white")
        searchlbl.grid(row = 0, column = 0, padx = 10, sticky=W)

        searchcombo = ttk.Combobox(searchframe, textvariable = self.varsearchcombo, font =("times new roman", 10, "bold"), state = "readonly")
        searchcombo['values'] = ("Search By", "ID", "Roll No", "CNIC")
        searchcombo.current(0)
        searchcombo.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)

        searchentry = ttk.Entry(searchframe, textvariable = self.varsearch, width = 15, font =("times new roman", 10))
        searchentry.grid(row = 0, column = 2, padx = 10, sticky=W)

        btnsearch = Button(searchframe, text = "Search", command =self.search, font =("times new roman", 10, "bold"), bg = "black", fg = "white", width = 10, cursor = "hand2" )
        btnsearch.grid(row = 0, column = 3, padx = 4)

        btnshowall = Button(searchframe, text = "Show All", command = self.showdata, font =("times new roman", 10, "bold"), bg = "black", fg = "white", width = 10, cursor = "hand2" )
        btnshowall.grid(row = 0, column = 4, padx = 4)


        # Table Frame

        tableframe = LabelFrame(rightframe, bd = 4, bg = "white", relief = RIDGE)
        tableframe.place(x = 5, y = 80, width = 580, height = 350)

        scrollx = ttk.Scrollbar(tableframe, orient = HORIZONTAL)
        scrolly = ttk.Scrollbar(tableframe, orient = VERTICAL)

        self.table = ttk.Treeview(tableframe, columns = ("Dep", "Course", "Year", "Semester", "ID", "Name", "Roll No", "Gender", "Email",  "Contact No", "CNIC", "Address", "photo"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)

        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)

        scrollx.config(command = self.table.xview)
        scrolly.config(command = self.table.yview)

        self.table.heading("Dep", text = "Department")
        self.table.heading("Course", text = "Course")
        self.table.heading("Year", text = "Year")
        self.table.heading("Semester", text = "Semester")
        self.table.heading("ID", text = "ID")
        self.table.heading("Name", text = "Name")
        self.table.heading("Roll No", text = "Roll No")
        self.table.heading("Gender", text = "Gender")
        self.table.heading("Email", text = "Email")
        self.table.heading("Contact No", text = "Contact No")
        self.table.heading("CNIC", text = "CNIC")
        self.table.heading("Address", text = "Address")
        self.table.heading("photo", text = "Photo Sample")

        self.table["show"] = "headings"

        self.table.column("Dep", width = 100)
        self.table.column("Course",  width = 100)
        self.table.column("Year", width = 100)
        self.table.column("Semester", width = 100)
        self.table.column("ID", width = 100)
        self.table.column("Name", width = 100)
        self.table.column("Roll No", width = 100)
        self.table.column("Gender", width = 100)
        self.table.column("Email", width = 100)
        self.table.column("Contact No", width = 100)
        self.table.column("CNIC", width = 100)
        self.table.column("Address", width = 100)
        self.table.column("photo", width = 100)
        

        self.table.pack(fill = BOTH, expand = 1)
        self.table.bind("<ButtonRelease>", self.getdata)
        self.showdata()


    # Data add Functions

    def adddata(self):
        if self.vardep.get() == "Select Department": # or self.varname.get() == "" or self.varid.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent = self.root)
        else:
            try:
                print('inside else')
                conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
                mycursor = conn.cursor()
                mycursor.execute("insert into student_details values(%s, %s,%s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s )", (
                                                                                                            self.vardep.get(),
                                                                                                            self.varcourse.get(),
                                                                                                            self.varyear.get(), 
                                                                                                            self.varsemester.get(),
                                                                                                            self.varid.get(),
                                                                                                            self.varname.get(),
                                                                                                            self.varrollno.get(),
                                                                                                            self.vargender.get(),
                                                                                                            self.varcontactno.get(),
                                                                                                            self.varcnic.get(),
                                                                                                            self.varaddress.get(),
                                                                                                            self.varemail.get(),
                                                                                                            self.varradio1.get()                                                                                                    
                                                                                                                ))
                                                                                                    
                conn.commit()
                self.showdata()
                conn.close()
                messagebox.showinfo("Success", "Data have been Successfully Added", parent = self.root)
            except Exception as es:
                messagebox.show("Error", f"Due to :{str(es)}", parent = self.root)

    # Showing Data into the Table


    def showdata(self):
        conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
        mycursor = conn.cursor()
        mycursor.execute("select * from student_details")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("", END, values = i)
            conn.commit()
        conn.close()


    # Get Data in to the text feidls to update  it

    def getdata(self, event = ""):
        focuscursor = self.table.focus()
        content = self.table.item(focuscursor)
        data = content["values"] 

        self.vardep.set(data[0]),
        self.varcourse.set(data[1]),
        self.varyear.set(data[2]), 
        self.varsemester.set(data[3]),
        self.varid.set(data[4]),
        self.varname.set(data[5]),
        self.varrollno.set(data[6]),
        self.vargender.set(data[7]),
        self.varemail.set(data[8]),
        self.varcontactno.set(data[9]),
        self.varcnic.set(data[10]),
        self.varaddress.set(data[11]),
        self.varradio1.set(data[12]) 

    # Update Function

    def updatedata(self):
        if self.vardep.get() == "Select Department":
            messagebox.showerror("Error", "All Fields are Required", parent = self.root)

        else:
            try:
                update = messagebox.askyesno("Update", "Do you wnat to update the Student Details", parent = self.root)
                if update > 0:
                    conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
                    mycursor = conn.cursor() 
                    print("LALA")
                    mycursor.execute("update student_details set Department = %s, Course = %s, Year = %s, Semester = %s, Name = %s, Roll_No = %s, Gender = %s, Contact_No = %s, Cnic = %s, Address = %s, Email = %s, PhotoSample = %s where Student_ID = %s",(
                                                                                                                                                                                                                                    self.vardep.get(),
                                                                                                                                                                                                                                    self.varcourse.get(),
                                                                                                                                                                                                                                    self.varyear.get(), 
                                                                                                                                                                                                                                    self.varsemester.get(),
                                                                                                                                                                                                                                    self.varname.get(),
                                                                                                                                                                                                                                    self.varrollno.get(),
                                                                                                                                                                                                                                    self.vargender.get(),
                                                                                                                                                                                                                                    self.varemail.get(),
                                                                                                                                                                                                                                    self.varcontactno.get(),
                                                                                                                                                                                                                                    self.varcnic.get(),
                                                                                                                                                                                                                                    self.varaddress.get(),
                                                                                                                                                                                                                                    self.varradio1.get(),
                                                                                                                                                                                                                                    self.varid.get()))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student Details Updated Successfully", parent = self.root)
                conn.commit()
                self.showdata()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent = self.root)
                 

    # Delete Function
    
    def deletedata(self):
        if self.varid.get() == "":
            messagebox.showerror("Error", "Student ID Must be require", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you Want to Delete Student Details", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
                    mycursor = conn.cursor()
                    sql = "delete from student_details where Student_ID = %s"
                    val = (self.varid.get(),)
                    mycursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.showdata()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted Student Details", parent = self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent = self.root)
                    


    # Reset Data
    def resetdata(self):

        self.vardep.set("Select Department")
        self.varcourse.set("Select Course")
        self.varyear.set("Select Year")
        self.varsemester.set("Select Semester")
        self.varid.set("")
        self.varname.set("")
        self.varrollno.set("")
        self.vargender.set("Select gender")
        self.varcontactno.set("")
        self.varcnic.set("")
        self.varaddress.set("")
        self.varemail.set("")
        self.varradio1.set("")
        self.varsearchcombo.set("Search By")
        self.varsearch.set("")

    # Update Dataset
    def updatedataset(self):
        pass
    # Generate Data With Photo Sample

    def photodataset(self):
        if self.vardep.get() == "Select Department":
            messagebox.showerror("Error", "All Fields are Required", parent = self.root)

        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
                mycursor = conn.cursor() 
                mycursor.execute("Select * from student_details")
                myresult = mycursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                mycursor.execute("update student_details set Department = %s, Course = %s, Year = %s, Semester = %s, Name = %s, Roll_No = %s, Gender = %s, Contact_No = %s, Cnic = %s, Address = %s, Email = %s, PhotoSample = %s where Student_ID = %s",(
                                                                                                                                                                                                                                    self.vardep.get(),
                                                                                                                                                                                                                                    self.varcourse.get(),
                                                                                                                                                                                                                                    self.varyear.get(), 
                                                                                                                                                                                                                                    self.varsemester.get(),
                                                                                                                                                                                                                                    self.varname.get(),
                                                                                                                                                                                                                                    self.varrollno.get(),
                                                                                                                                                                                                                                    self.vargender.get(),
                                                                                                                                                                                                                                    self.varemail.get(),
                                                                                                                                                                                                                                    self.varcontactno.get(),
                                                                                                                                                                                                                                    self.varcnic.get(),
                                                                                                                                                                                                                                    self.varaddress.get(),
                                                                                                                                                                                                                                    self.varradio1.get(),
                                                                                                                                                                                                                                    self.varid.get() == id + 1))

                conn.commit()
                self.showdata()
                # self.resetdata()
                conn.close()

                # Load Harcascade File For using Face Reconition
                
                faceclassifier = cv.CascadeClassifier("E:\FYP\haarcascade_frontalface_default.xml")
                
                def crop(img):
                    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                    faces = faceclassifier.detectMultiScale(grey, 1.3, 5)
                    # sacling factor = 1.3
                    # minimum neighbour = 5

                    for (x,y,w,h) in faces:
                        crop = img[y:y+h, x:x+h]
                        return crop

                cap = cv.VideoCapture(0)
                imgid = 0
                while True:
                    ret, myframe = cap.read()
                    if crop(myframe) is not None:
                        imgid += 1
                        face = cv.resize(crop(myframe), (450,450))
                        face = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
                        file_name = "Photo_Sample/user-" + self.varid.get() + "-" + str(imgid) + ".jpg"
                        cv.imwrite(file_name, face)
                        cv.putText(face, str(imgid), (50,50), cv.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                        cv.imshow("Detecting Face", face)

                    if cv.waitKey(1) == 13 or int(imgid) == 100:
                        break
                

                cap.release()
                cv. destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data Set Completed", parent = self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent = self.root)

    
    
    
    def search(self):
        print(self.varsearch.get())
        conn = mysql.connector.connect(host = 'localhost', username = "root", password = "Muhammadfaiq@123", database = "attendancesystem")
        mycursor = conn.cursor()
        
        if self.varsearchcombo.get() == "ID":
            mycursor.execute("select * from student_details where Student_ID =" + self.varsearch.get())

        elif self.varsearchcombo.get() == "CNIC":
            mycursor.execute("select * from student_details where Cnic =" + self.varsearch.get())

        elif self.varsearchcombo.get() == "Roll No":
            mycursor.execute("select * from student_details where Roll_No =" + self.varsearch.get())

        else:
            messagebox.showerror("Error", "Select Search Parameter")
            
        
        data = mycursor.fetchall()
        if len(data) != 0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("", END, values = i)
            conn.commit()
        conn.close()
            



                 








if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()