from tkinter import *
import cv2


class Face_Recognition(Tk):
    def __init__(self):
        super().__init__()
        self.title("Face Recognition")
        self.w = int(self.winfo_screenwidth())
        self.h = int(self.winfo_screenheight())
        self.geometry("{0}x{1}".format(self.w, self.h))
        self.minsize(self.w,self.h)
        self.Start()
        self.mainloop()

    def Start(self):
        self.introduction = Label(self, text="INTRODUCTION")
        self.introduction.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.proceed = Button(self, text="Proceed", command=self.Proceed)
        self.proceed.place(relx=0.47, rely=0.58)

        self.About = Button(self, text="About", command=self.about)
        self.About.place(relx=0.4, rely=0.58)

        self.Dekhte_hai = Button(self, text="dekhte hai")
        self.Dekhte_hai.place(relx=0.54, rely=0.58)

        self.exit= Button(self, text="EXIT", command= exit)
        self.exit.place(relx=0.9, rely=0.9)

    def ddestroy(self):
        self.About.destroy()
        self.proceed.destroy()
        self.introduction.destroy()
        self.Dekhte_hai.destroy()
        self.exit.destroy()

    def about(self):

        self.ddestroy()

        self.about_system = Label(self, text= "About project")
        self.about_system.place(relx=0.5, rely=0.5)

        self.back = Button(master=None, text= "Back", command= self.Back)
        self.back.place(relx=0.9, rely=0.9)

    def Back(self):
        self.back.destroy()
        self.about_system.destroy()
        self.Start()

    def Proceed(self):

        self.ddestroy()

        self.details= Label(self, text= "Enter your details")
        self.details.place(relx=0.37, rely=0.15)

        self.name = Label(self, text= "Name")
        self.name.place(relx=0.3, rely=0.3)

        self.Enter_name = Entry(self)
        self.Enter_name.place(relx=0.4, rely=0.3)

        self.roll_no = Label(self, text= "Enrollment No")
        self.roll_no.place(relx=0.3, rely=0.37)

        self.Enter_roll_no = Entry(self)
        self.Enter_roll_no.place(relx=0.4, rely=0.37)

        self.next = Button(self, text="Next", command=self.Next)
        self.next.place(relx=0.466, rely=0.42)

        self.back_s = Button(self, text="Back", command=self.back_to_start)
        self.back_s.place(relx=0.9, rely=0.9)

    def back_to_start(self):
        self.back_s.destroy()
        self.next.destroy()
        self.Enter_roll_no.destroy()
        self.roll_no.destroy()
        self.Enter_name.destroy()
        self.name.destroy()
        self.details.destroy()

        self.Start()

    def Next(self):
        self.next.destroy()
        self.Enter_roll_no.destroy()
        self.roll_no.destroy()
        self.Enter_name.destroy()
        self.name.destroy()
        self.details.destroy()
        self.back_s.destroy()

        self.Check_your_attendance= Button(self, text="Check your attendance", command=self.check_attendance)
        self.Check_your_attendance.place(relx=0.5, rely=0.3)

        self.Mark_your_Attendance = Button(self, text="Mark your attendance", command=self.mark_attendance)
        self.Mark_your_Attendance.place(relx=0.5, rely=0.37)

        self.back_p = Button(self, text="Back", command=self.back_to_proceed)
        self.back_p.place(relx=0.9, rely=0.9)

    def back_to_proceed(self):
        self.Check_your_attendance.destroy()
        self.Mark_your_Attendance.destroy()
        self.Proceed()

    def check_attendance(self):
        self.Check_your_attendance.destroy()
        self.Mark_your_Attendance.destroy()

        self.back_d = Button(self, text="Back", command=self.back_to_details)
        self.back_d.place(relx=0.9, rely=0.9)

    def back_to_details(self):
        self.Check_your_attendance.destroy()
        self.Mark_your_Attendance.destroy()
        self.back_d.destroy()

        self.Next()

    def mark_attendance(self):
        self.Check_your_attendance.destroy()
        self.Mark_your_Attendance.destroy()

        self.back_d = Button(self, text="Back", command=self.back_to_details)
        self.back_d.place(relx=0.9, rely=0.9)

if __name__ == '__main__':
    Face_Recognition()


