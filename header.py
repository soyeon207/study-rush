from tkinter import *

class Header:
    def __init__(self, root):
        self.frame_setting(root)
        self.setting('m', '소연')

    def frame_setting(self, root):
        self.header = Frame(root)
        self.header.place(x=0, y=0, width=1280, height=140)
        self.header.configure(bg='#FFFFFF')

    def setting(self, _type, _name):
        self.type = _type
        Label(self.header, text='Study Rush', bg='#FFFFFF', font=('Helvetica', 50, 'bold'), fg='#000000').place(x=20, y=20)
        Label(self.header, text= _name + ' 님 안녕하세요', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=330, y=50)
        if type == 'm':
            Label(self.header, text='관리자모드', bg = '#9DC238', font=('나눔고딕', 20, 'bold'), fg='#FFFFFF').place(x=1100, y=50)
    
    def lift(self):
        self.header.lift()
    
    

