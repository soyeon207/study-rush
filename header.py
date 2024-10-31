from tkinter import *
from utils import *

class Header:
    def __init__(self, root):
        self.frame_setting(root)

    def master(self):
        Label(self.header, text='관리자모드', bg = GREEN, font=FONT_20_BOLD, fg=WHITE).place(x=1100, y=50)

    def frame_setting(self, root):
        self.header = Frame(root)
        self.header.place(x=0, y=0, width=1280, height=140)
        self.header.configure(bg=WHITE)

    def setting(self, type, name):
        Label(self.header, text=TITLE, bg=WHITE, font=FONT_50_BOLD, fg=BLACK).place(x=20, y=20)
        Label(self.header, text= name + ' 님 안녕하세요', bg=WHITE, font='나눔고딕', fg=BLACK).place(x=330, y=50)
        self.type = type

    def lift(self):
        self.header.lift()
        if self.type == MASTER:
            self.master()


        
    
    

