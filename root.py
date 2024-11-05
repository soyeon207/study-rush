from tkinter import *
from login import Login
from category import Category
from assignment import Assignment
from header import Header
from statistic import Statistic
from utils import *
from data_factory import DataFactory
from style import *

root = Tk()
root.title(TITLE)
root.geometry('1280x832+500+150')

combostyle()
factory = DataFactory()
header = Header(root, factory)
assignment = Assignment(root, factory)
category = Category(root)
statisitc = Statistic(root)
login = Login(root, assignment, category, header, factory)

header.set_login(login)
root.mainloop()
