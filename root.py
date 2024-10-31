from tkinter import *
from login import Login
from assignment_s import AssignmentS
from assignment_m import AssignmentM
from header import Header
from utils import *

root = Tk()
root.title(TITLE)
root.geometry('1280x832+500+150')

header = Header(root)
assignment_s = AssignmentS(root)
assignment_m = AssignmentM(root)
login = Login(root, assignment_s, header)

root.mainloop()
