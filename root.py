from tkinter import *
from login import Login
from assignment import Assignment
from header import Header

root = Tk()
root.title('Study Rush')
root.geometry('1280x832+500+150')

header = Header(root)
assignment = Assignment(root)
login = Login(root, assignment, header)

root.mainloop()
