from tkinter import * #For designing of front end
from HelperFunctions import *   # utility functions
#Add more libraries here

class AttendanceManager(object):

    def __init__(self):
        self.root = Tk()   #root widget for the app window
        self.root.geometry("1200X800")
        self.root.title("Attendance Manager")
        self.root.resizable(0,0)  #to disable resizing of root window to avoid distortion

if __name__ == '__main__':
    AttendanceManager()
#Before executing code, Python interpreter reads source file and define few special variables/global variables.
#If the python interpreter is running that module (the source file) as the main program, it sets the special
# __name__ variable to have a value “__main__”. If this file is being imported from another module,
# __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.
#Here our class DigitRecognizer script is being used as a module so its __name__ is __main__
