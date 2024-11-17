from tkinter import *
from login import Login
from assignment import Assignment
from study import Study
from header import Header
from statistic import Statistic
from utils import *
from entities import Entities
from components import Components
from style import *

def setup_root():
    root = Tk()
    root.title(TITLE)
    root.geometry(WINDOW_SIZE)
    combostyle()
    return root

def initialize_components(root, entities, components):
    header = Header(root, entities, components)
    assignment = Assignment(root, entities, components)
    study = Study(root, entities, components)
    statisitc = Statistic(root, entities, components)
    login = Login(root, entities, components)

    components.set_component(header, assignment, study, statisitc, login)
    login.setting()

def main():
    root = setup_root()

    entities = Entities()
    components = Components()

    initialize_components(root, entities, components)
    root.mainloop()

if __name__ == "__main__":
    main()
