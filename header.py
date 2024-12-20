from tkinter import *
from utils import *

class Header:
    def __init__(self, root, entities, compoenents):
        self.root = root
        self.frame_setting()
        self.entities = entities
        self.compoenents = compoenents

    def master(self):
        Label(self.header, text='관리자모드', bg = GREEN, font=FONT_20_BOLD, fg=WHITE).place(x=1100, y=50)

    def logout(self):
        self.compoenents.login.lift()

    def frame_setting(self):
        self.header = Frame(self.root)
        self.header.place(x=0, y=0, width=1280, height=140)
        self.header.configure(bg=WHITE)

    def setting(self):
        self.member = self.entities.member
        Label(self.header, text=TITLE, bg=WHITE, font=FONT_50_BOLD, fg=BLACK).place(x=20, y=20)
        Label(self.header, text= self.member.displated_name() + ' 님 안녕하세요', bg=WHITE, font='나눔고딕', fg=BLACK).place(x=330, y=50)
        Button(self.header, text='로그아웃', font=FONT_16, bd=0, highlightthickness=0, command=self.logout).place(x=600, y=50)

    def lift(self):
        for widget in self.header.winfo_children():
            widget.destroy()
            
        self.header.lift()
        self.setting()
        if self.member.type == MASTER:
            self.master()

