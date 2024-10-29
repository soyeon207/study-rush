from tkinter import *

class Assignment:
    def __init__(self, root):
        self.frame_setting(root)
        self.setting()

    def setting(self):
        Label(self.assignment, text= '과제 추가', bg='#FFFFFF', font=('나눔고딕', 15, 'bold'), fg='#000000').place(x=20, y=0)
        Label(self.assignment, text= '카테고리', bg='#FFFFFF', font=('나눔고딕', 15), fg='#000000').place(x=30, y=50)
        Label(self.assignment, text= '과제명', bg='#FFFFFF', font=('나눔고딕', 15), fg='#000000').place(x=400, y=50)
        Label(self.assignment, text= '마감 날짜', bg='#FFFFFF', font=('나눔고딕', 15), fg='#000000').place(x=700, y=50)

    def frame_setting(self, root):
        self.assignment = Frame(root)
        self.assignment.place(x=0, y=140, width=1280, height=692)
        self.assignment.configure(bg='#FFFFFF')

    def lift(self):
        self.assignment.lift()
    
