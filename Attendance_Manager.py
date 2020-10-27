from tkinter import * #For designing of front end
from PIL import ImageTk, Image #For loading images
from tkinter import font as tkFont
#Add more libraries here

class AttendanceManager(object):

    def __init__(self):
        self.root = Tk()   #root widget for the app window
        self.root.geometry("1200x800")
        self.root.title("Attendance Manager")
        self.root.resizable(0,0)  #to disable resizing of root window to avoid distortion
        self.BackgroundImage(self.root)
        self.create_MainFrame("First")
        self.ButtonFont = tkFont.Font(family="Playbill", size=20, weight="bold")
        self.TextFont = tkFont.Font(family="Courier New", size=15, weight="bold")
        self.FirstPage()
        self.root.mainloop()

    def FirstPage(self):
        self.content_frame = Frame(self.main_frame,height=300,width=700,bg="Black")
        self.content_frame.place(x=500,y=450)  #Place below heading
        self.ProceedButton = Button(self.content_frame,text="Proceed",activebackground="grey",bd=3,bg="White",fg="Black",
                                    command=self.ProceedPage,font=self.ButtonFont,justify=CENTER,height=2,width=10)
        self.ProceedButton.place(x=0,y=25)
        self.AboutButton = Button(self.content_frame, text="About", activebackground="grey", bd=3, bg="White",fg="Black",
                                    command=self.AboutPage, font=self.ButtonFont, justify=CENTER, height=2, width=10)
        self.AboutButton.place(x=300, y=25)

    def ProceedPage(self):
        self.main_frame.destroy()  #Destroy the entire main frame and create a new page
        self.create_MainFrame()

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
