from tkinter import * #For designing of front end
from PIL import ImageTk, Image #For loading images
from tkinter import font as tkFont
import cv2
import PIL
import pyscreenshot as ImageGrab
import Database as db
from HelperFunctions import *
from inception_blocks_v2 import *
from keras.models import Sequential
from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
from keras.models import Model
from keras.layers.normalization import BatchNormalization
from keras.layers.pooling import MaxPooling2D, AveragePooling2D
from keras.layers.merge import Concatenate
from keras.layers.core import Lambda, Flatten, Dense
from keras.initializers import glorot_uniform
from keras.engine.topology import Layer
from keras import backend as K
K.set_image_data_format('channels_first')
import os
import numpy as np
from numpy import genfromtxt
import pandas as pd


#Add more libraries here

class AttendanceManager(object):

    def __init__(self):
        self.root = Tk()   #root widget for the app window
        self.root.geometry("1200x800")
        self.root.title("Attendance Manager")
        self.root.resizable(0,0)  #to disable resizing of root window to avoid distortion
        self.BackgroundImage(self.root)
        self.ButtonFont = tkFont.Font(family="Playbill", size=20, weight="bold")
        self.TextFont = tkFont.Font(family="Courier New", size=15, weight="bold")
        self.InfoFont = tkFont.Font(family="Courier New", size=25, weight="bold")
        self.FirstPage()
        self.root.mainloop()

    #################################################################################################################
    ############################################### 1st Page ########################################################
    #################################################################################################################

    def FirstPage(self):
        self.create_MainFrame("First")
        self.content_frame = Frame(self.main_frame,height=300,width=700,bg="Black")
        self.content_frame.place(x=500,y=550)  #Place below heading
        self.ProceedButton = Button(self.content_frame,text="Proceed",activebackground="grey",bd=3,bg="White",fg="Black",
                                    command=self.ProceedPage,font=self.ButtonFont,justify=CENTER,height=1,width=7)
        self.ProceedButton.place(x=0,y=25)
        self.AboutButton = Button(self.content_frame, text="About", activebackground="grey", bd=3, bg="White",fg="Black",
                                    command=self.AboutPage, font=self.ButtonFont, justify=CENTER, height=1, width=7)
        self.AboutButton.place(x=200, y=25)
        self.ExitButton = Button(self.content_frame, text="Exit", activebackground="grey", bd=3, bg="White",fg="Black",
                                 command=exit, font=self.ButtonFont, justify=CENTER, height=1, width=7)
        self.ExitButton.place(x=400, y=25)

    ######################################################################################################################
    ################################################ Proceed Page ########################################################
    ######################################################################################################################

    def ProceedPage(self):
        self.main_frame.destroy()  #Destroy the entire main frame and create a new page
        self.create_MainFrame()
        self.NameLabel = Label(self.main_frame, text="Name     :",bg="black", fg="white", font=self.TextFont)
        self.NameLabel.place(x=600, y=170)

        self.EnterName = Entry(self.main_frame, bd=3,width=30, bg="black", fg="white")
        self.EnterName.place(x=790, y=170)

        self.EnrollmentNoLabel = Label(self.main_frame, text="Enrollment No :", bg="black", fg="white",
                                       font=self.TextFont)
        self.EnrollmentNoLabel.place(x=600, y=240)

        self.EnterEnrollmentNo = Entry(self.main_frame, bd=3,width=30, bg="black", fg="white")
        self.EnterEnrollmentNo.place(x=790, y=240)

        self.CourseLabel = Label(self.main_frame, text="Course     :", bg="black", fg="white", font=self.TextFont)
        self.CourseLabel.place(x=600, y=300)

        self.clicked = StringVar(self.main_frame)
        self.clicked.set("Select")
        self.CourseEnter = OptionMenu(self.main_frame, self.clicked, "BCA", "B.Tech")
        self.CourseEnter.config(bg="Black", fg="White",activebackground="grey",font=self.TextFont)
        self.CourseEnter.place(x=790, y=300)

        self.SemesterLabel = Label(self.main_frame, text="Semester   :", bg="black", fg="white", font=self.TextFont)
        self.SemesterLabel.place(x=600, y=360)

        self.SelectSemester = StringVar(self.main_frame)
        self.SelectSemester.set("Select")
        self.EnterSemester = OptionMenu(self.main_frame,self.SelectSemester , "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        self.EnterSemester.config(bg="Black", fg="White",activebackground="grey",font=self.TextFont)
        self.EnterSemester.place(x=790, y=360)

        self.ResetButton = Button(self.main_frame, text="Reset", activebackground="grey", bd=3, bg="White",
                                  fg="Black", font=self.ButtonFont, justify=RIGHT, height=1, width=7,
                                  command=self.ProceedPage)
        self.ResetButton.place(x=650, y=470)

        self.ContinueButton = Button(self.main_frame, text="Continue", activebackground="grey", bd=3, bg="White",
                                     fg="Black", font=self.ButtonFont, justify=RIGHT, height=1, width=7,
                                     command=self.ContinuePage)
        self.ContinueButton.place(x=850, y=470)

        self.BackButton = Button(self.main_frame, text="Back", activebackground="grey", bd=3, bg="White",command=self.FirstPage,
                                         fg="Black", font=self.ButtonFont, justify=RIGHT, height=1, width=7)
        self.BackButton.place(x=750, y=550)

    ##############################################################################################################
    ####################################### Continue  Page ########################################################
    ###############################################################################################################

    def ContinuePage(self):
        self.Name = self.EnterName.get()
        self.RollNo = self.EnterEnrollmentNo.get()
        self.Course = self.clicked.get()
        self.Semester = self.SelectSemester.get()
        self.Name = self.Name.replace(" ", "")
        if self.RollNo.isdigit() and int(len(self.RollNo)) == 11 and self.Name.isalpha() and self.Semester != "Select" and self.Course != "Select":
            if self.Course == "BCA" and (self.Semester == "VII" or self.Semester == "VIII"):
                self.Alert_1 = Label(self.main_frame, text="There are only I TO VI \n Semester in BCA ",
                                     bg="black", fg="white", font=self.TextFont)
                self.Alert_1.place(x=860, y=360)
            else:
                self.main_frame.destroy()
                self.create_MainFrame()
                self.Check_Your_AttendanceButton = Button(self.main_frame, text="Check your attendance",
                                                          activebackground="grey", bd=3, bg="White",
                                                          fg="Black", font=self.ButtonFont, justify=RIGHT, height=1,
                                                          width=25, command=self.Check_AttendancePage)
                self.Check_Your_AttendanceButton.place(x=650, y=210)

                self.Mark_Your_AttendanceButton = Button(self.main_frame, text="Mark your attendance",
                                                         activebackground="grey", bd=3, bg="White",
                                                         fg="Black", font=self.ButtonFont, justify=RIGHT, height=1,
                                                         width=25, command=self.MarkAttendancePage)
                self.Mark_Your_AttendanceButton.place(x=650, y=310)

                self.BackButton_Check = Button(self.main_frame, text="Back", activebackground="grey", bd=3,
                                               bg="White",
                                               fg="Black", font=self.ButtonFont, justify=RIGHT, height=1, width=8,
                                               command=self.ProceedPage)
                self.BackButton_Check.place(x=650, y=410)
        else:
            self.ProceedPage()
            self.Alert = Label(self.main_frame,
                               text="Your name should be name \n\n Enrollment number should be 11 digits only:",
                               bg="black", fg="white", font=self.TextFont)
            self.Alert.place(x=590, y=70)

    ##############################################################################################################
    ########################################## 6th Page ############################################################
    ##############################################################################################################

    def ShowAttendance(self):
        self.subject = self.ClickedSubject.get()
        if self.subject == "Select":
            self.alert = Label(self.main_frame, text="!Select subject", bg="black", fg="white", font=self.TextFont)
            self.alert.place(x=600, y=100)
        else:
            # self.alert.destroy()
            self.ShowSubjectAttendance = Label(self.main_frame, text="Your attendance of " + self.subject + " is ",
                                               bg="black", fg="white", font=self.TextFont)
            self.ShowSubjectAttendance.place(x=600, y=350)

    ############################################ 7th Page #########################################################

    def MarkAttendancePage(self):
        self.main_frame.destroy()
        self.create_MainFrame()
        self.CameraFrame = Frame(self.main_frame,height=700,width=1150)
        self.CameraFrame.place(x=25,y=10)
        self.CameraLabel = Label(self.CameraFrame,height=700,width=1150)
        self.CameraLabel.place(x=0,y=0)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,700)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,1150)
        self.ShowFrame()
        self.ContentFrame = Frame(self.main_frame,height=70,width=1050,bg="black")
        self.ContentFrame.place(x=100,y=720)
        self.Info = Message(self.ContentFrame,text="Please try to adjust you entire face in the video frame and then press the Click Button",
                            font=self.TextFont,fg="white",width=750,justify=LEFT,bg="black")
        self.Info.place(x=0,y=0)
        self.ClickButton = Button(self.ContentFrame,text="Click",fg="black",bg="white",bd=3,activebackground="grey",font=self.ButtonFont,
                                  height=1,width=8,command=self.ClickImage,justify=CENTER)
        self.ClickButton.place(x=850,y=0)

    def ShowFrame(self):
        ret, frame = self.cap.read()
        if ret:
            self.frame = cv2.flip(frame, 1)
            self.frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGBA)
            self.img = PIL.Image.fromarray(self.frame)
            self.imgtk = ImageTk.PhotoImage(image=self.img)
            self.CameraLabel.img = self.imgtk
            self.CameraLabel.configure(image=self.imgtk)
            self.CameraLabel.after(10, self.ShowFrame)

    def ClickImage(self):
        self.SaveImage()
        self.main_frame.destroy()
        self.create_MainFrame()
        self.WaitFrame = Frame(self.main_frame, height=400, width=500, bg="black")
        self.WaitFrame.place(x=500, y=50)
        self.WaitMessage = Message(self.WaitFrame, bg="black", fg="White", font=self.InfoFont, width=500,
                                   justify=CENTER,
                                   text="You are almost there.\n We are confirming your identity\n \n Estimated time 10s")
        self.WaitMessage.place(x=0, y=0)




        self.cap.release()
        cv2.destroyAllWindows()

        import tensorflow as tf
        physical_devices = tf.config.experimental.list_physical_devices("GPU")
        tf.config.experimental.set_memory_growth(physical_devices[0], True)

        #Loading our pre trained Face Recognition Model
        self.FRmodel = faceRecoModel(input_shape=(3, 96, 96))
        self.FRmodel.compile(optimizer = 'adam', loss = triplet_loss, metrics = ['accuracy'])
        load_weights_from_FaceNet(self.FRmodel)
        DataBase = db.DataBase
        self.DictId = int(DataBase["DictId"][DataBase["Name"].str.contains("Arjun Bajaj")])
        self.ImageData = db.ImgDataDict(self.FRmodel)
        self.Distance, self.MarkAttendance = verify("Images/Person.jpg",1,self.ImageData,self.FRmodel)
        self.main_frame.destroy()
        self.create_MainFrame()
        self.HeadingFrame = Frame(self.main_frame, height=100, width=650, bg="black")
        self.HeadingFrame.place(x=500, y=50)
        if self.MarkAttendance:
            self.Heading = Message(self.HeadingFrame,font=self.InfoFont,fg="white",bg="black",width=500,justify=CENTER,
                                   text="Welcome In!!!")
            #text="Welcome " + str(db.DataBase["Name"][self.DictId])
            self.Heading.place(x=0,y=0)
        else:
            self.Heading = Message(self.HeadingFrame, font=self.InfoFont, fg="white", bg="black", width=600,
                                   justify=CENTER,
                                   text="Stay Out! You are not you claim to be."+str(self.Distance))
            self.Heading.place(x=0, y=0)


    ##############################################################################################################
    ############################################# Attendance Page ################################################
    ##############################################################################################################

    def SaveImage(self):
        self.x1 = self.root.winfo_rootx() + self.CameraFrame.winfo_x()
        self.y1 = self.root.winfo_rooty() + self.CameraFrame.winfo_y()
        self.x2 = self.x1 + 1150
        self.y2 = self.y1 + 700
        self.img = ImageGrab.grab((self.x1, self.y1, self.x2, self.y2))
        imgpath = "Images/Person.jpg"
        self.img.save(imgpath)
        self.Image = Image.open("Images/Person.jpg")
        self.Image = self.Image.resize((96,96),Image.ANTIALIAS)
        self.Image.save(imgpath,optimize=True,quality=95)

    def Check_AttendancePage(self):
        self.main_frame.destroy()
        self.create_MainFrame()

        self.SelectSubject = Label(self.main_frame, text="Select subject :", bg="black", fg="white",font=self.TextFont)
        self.SelectSubject.place(x=600, y=200)

        self.course = self.clicked.get()
        self.semester = self.SelectSemester.get()
        self.ClickedSubject = StringVar(self.main_frame)
        self.ClickedSubject.set("Select")
        if self.course == "BCA":
            if self.semester == "I":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "Maths-I",
                                               "Techical Communication", "C language", "ICIT", "Physics")
            elif self.semester == "II":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "Maths-II", "POM", "DE", "DS",
                                               "DBMS")
            elif self.semester == "III":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "Maths-III", "CA", "FEDT",
                                               "POA", "C++")
            elif self.semester == "IV":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "Maths-IV", "Web.Tech", "Java",
                                               "SE", "CN")
            elif self.semester == "V":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "E.com", "CG", "PHP", "OS",
                                               "ST", "BE")
            elif self.semester == "VI":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "DWH & DM", "MC", "Linux",
                                               "M&IA", "BI", "AI", "NS", "NP")
        elif self.course == "B.Tech":
            if self.semester == "I":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "Maths-I",
                                               "Techical Communication", "C language", "ICIT", "Physics-I")
            elif self.semester == "II":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "Maths-II", "POM", "DE", "DS",
                                               "DBMS")
            elif self.semester == "III":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "Maths-III", "CA", "FEDT",
                                               "POA", "C++")
            elif self.semester == "IV":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "Maths-IV", "Web.Tech", "Java",
                                               "SE", "CN")
            elif self.semester == "V":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "E.com", "CG", "PHP", "OS",
                                               "ST", "BE")
            elif self.semester == "VI":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "DWH & DM", "MC", "Linux")
            elif self.semester == "VII":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "DWH & DM", "MC", "Linux")
            elif self.semester == "VIII":
                self.SubjectEnter = OptionMenu(self.main_frame, self.ClickedSubject, "DWH & DM", "MC", "Linux")
        self.SubjectEnter.config(bg="Black", fg="White")
        self.SubjectEnter.place(x=820, y=200)

        self.DisplayAttendance = Button(self.main_frame, text="Display Attendance", activebackground="grey", bd=3,
                                        bg="White",
                                        fg="Black", font=self.ButtonFont, justify=RIGHT, height=1, width=16,
                                        command=self.ShowAttendance)
        self.DisplayAttendance.place(x=744, y=250)

        self.BackButton_Check = Button(self.main_frame, text="Back", activebackground="grey", bd=3, bg="White",
                                       fg="Black", font=self.ButtonFont, justify=RIGHT, height=1, width=8)
        self.BackButton_Check.place(x=700, y=680)

    ###################################################################################################################
    ############################################## About Page #########################################################
    ###################################################################################################################

    def AboutPage(self):
        self.content_frame.destroy() #Just destroy the content frame as the heading is needed
        self.content_frame = Frame(self.main_frame, height=300, width=700, bg="Black")
        self.content_frame.place(x=500, y=450)  # Place below heading
        self.about = "Attendance Manager \n\n This is an application that can mark as well as manage your attendance. It confirms your identity by opening your webcam and using our face recognition model to confirm your identity and automatically mark your attendance.Also you can check your previous attendance. \n This application is developed by Arjun Bajaj and Anirudh Singh"
        self.AboutInfo = Message(self.content_frame,bg="Black",fg="White",font=self.TextFont,justify=CENTER,width=600,
                                 text=self.about)
        self.AboutInfo.place(x=0,y=0)
        self.BackButton = Button(self.content_frame, text="Back", activebackground="grey", bd=3, bg="White",fg="Black",
                                    command=self.FirstPage, font=self.ButtonFont, justify=CENTER, height=1, width=5)
        self.BackButton.place(x=400,y=250)

    def create_MainFrame(self,page="Any"):
        self.main_frame = Frame(self.root, height=800, width=1200)
        self.main_frame.place(x=0, y=0)
        self.BackgroundImage(self.main_frame,page)

    def BackgroundImage(self,frame,page="Any"):
        if page == "First":
            self.bg_image = ImageTk.PhotoImage(file="Images/Background_Front.jpg")
        else:
            self.bg_image = ImageTk.PhotoImage(file="Images/Background.jpg")
        self.bg_label = Label(frame, image=self.bg_image)
        self.bg_label.place(x=0, y=0)


if __name__ == '__main__':
    AttendanceManager()
#Before executing code, Python interpreter reads source file and define few special variables/global variables.
#If the python interpreter is running that module (the source file) as the main program, it sets the special
# __name__ variable to have a value “__main__”. If this file is being imported from another module,
# __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.
#Here our class DigitRecognizer script is being used as a module so its __name__ is __main__
