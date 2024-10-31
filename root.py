from tkinter import *
from login import Login
from category import Category
from assignment import Assignment
from header import Header
from utils import *

root = Tk()
root.title(TITLE)
root.geometry('1280x832+500+150')

header = Header(root)
assignment = Assignment(root)
category = Category(root)
login = Login(root, assignment, header)

root.mainloop()
