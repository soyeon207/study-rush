from tkinter import *
from tkinter import messagebox
from utils import *

class Login:
    entry1 = None
    entry2 = None

    def __init__(self, root, _assignment, _header):
        self.frame_setting(root)
        self.assignment = _assignment
        self.type = STUDENT
        self.header = _header
        self.setting()

    def frame_setting(self, root):
        self.login = Frame(root)
        self.login.place(x=0, y=0, width=1280, height=832)
        self.login.configure(bg=WHITE)
        
    def get_type(self):
        return self.type

    def mode_change(self):
        for widget in self.login.winfo_children():
            widget.destroy()
        
        if self.type == STUDENT:
            self.type = MASTER
        else:
            self.type = STUDENT
        self.setting()


    def on_connect(self):
        global entry1, entry2
        entry1_val = entry1.get()
        entry2_val = entry2.get()

        if self.type == STUDENT:
            self.valid_student(entry1_val, entry2_val)
        else:
            self.valid_master(entry1_val, entry2_val)


    def valid_student(self, student_id, name):
        if student_id == '' or name == '':
            messagebox.showwarning("알럿", "학번과 이름을 입력해주세요.")
        else:
            self.assignment.lift()
            self.header.setting(self.type, student_id+' ' + name)
            self.header.lift()

    def valid_master(self, code, name):
        print(code, SKKU)

        if code == '' or name == '':
            messagebox.showwarning("알럿", "코드와 이름을 입력해주세요.")
        elif code.upper() != SKKU :
            messagebox.showwarning("알럿", "코드가 일치하지 않습니다.")
        else:
            self.assignment.lift()
            self.header.setting(self.type, name)
            self.header.lift()

    def setting(self):
        global entry1, entry2
        Label(self.login, text=TITLE, bg=WHITE, font=FONT_55_BOLD, fg=BLACK).place(x=500, y=100)
        
        entry1 = Entry(self.login, bg=GRAY, font=FONT_20, width=30, fg=BLACK, bd=7, relief=FLAT, highlightthickness=0)
        entry1.place(x=480, y=250)

        entry2 = Entry(self.login, bg=GRAY, relief=FLAT, font=FONT_20,  width=30, fg=BLACK, bd=7, highlightthickness=0)
        entry2.place(x=480, y=310)

        Button(self.login, text='접속', bg=WHITE, highlightthickness=0, bd=0, font=FONT_16, command=self.on_connect, fg=BLACK, height=5, width=3).place(x=900, y=250)
        
        if self.type == STUDENT:
            Label(self.login, text='학번 : ', bg=WHITE, font=FONT_20, fg=BLACK).place(x=400, y=250)
            Label(self.login, text='이름 : ', bg=WHITE, font=FONT_20, fg=BLACK).place(x=400, y=318)
            Button(self.login, text='관리자모드 이동    ->', bg=BLACK, font=FONT_16, bd=0, highlightthickness=0, command=self.mode_change).place(x=550, y=420)
        else:
            Label(self.login, text='관리자모드', bg = '#9DC238', font=FONT_20_BOLD, fg=WHITE).place(x=620, y=65)
            Button(self.login, text='학생 모드 이동    ->', bg=BLACK, font=FONT_16, bd=0, highlightthickness=0, command=self.mode_change).place(x=550, y=420)
            Label(self.login, text='코드 : ', bg=WHITE, font=FONT_20, fg=BLACK).place(x=400, y=250)
            Label(self.login, text='이름 : ', bg=WHITE, font=FONT_20, fg=BLACK).place(x=400, y=318)


