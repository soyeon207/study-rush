from tkinter import *
from login import Login
from category import Category
from assignment import Assignment
from header import Header
from statistic import Statistic
from utils import *
from data_factory import DataFactory
from class_factory import ClassFactory
from style import *

root = Tk()
root.title(TITLE)
root.geometry('1280x832+500+150')

combostyle()
factory = DataFactory()
class_factory = ClassFactory()

header = Header(root, factory)
category = Category(root, factory, class_factory)
assignment = Assignment(root, factory, class_factory)
statisitc = Statistic(root, factory, class_factory)
login = Login(root, assignment, category, header, factory)

header.set_login(login)
class_factory.set_data(header, category, assignment, statisitc, login)

root.mainloop()
