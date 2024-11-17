from tkinter import *
from login import Login
from category import Category
from assignment import Assignment
from header import Header
from statistic import Statistic
from utils import *
from entities import Entities
from components import Components
from style import *

root = Tk()
root.title(TITLE)
root.geometry(WINDOW_SIZE)

combostyle()
entities = Entities()
components = Components()

header = Header(root, entities, components)
category = Category(root, entities, components)
assignment = Assignment(root, entities, components)
statisitc = Statistic(root, entities, components)
login = Login(root, entities, components)

components.set_component(header, category, assignment, statisitc, login)
login.setting()

root.mainloop()
