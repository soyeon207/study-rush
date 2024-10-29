from tkinter import *
from tkinter import messagebox

class Login:
    entry1 = None
    entry2 = None

    def __init__(self, root, _assignment, _header):
        self.frame_setting(root)
        self.assignment = _assignment
        self.type = 's'
        self.header = _header
        self.setting()

    def frame_setting(self, root):
        self.login = Frame(root)
        self.login.place(x=0, y=0, width=1280, height=832)
        self.login.configure(bg='#FFFFFF')
        
    def get_type(self):
        return self.type

    def mode_change(self):
        for widget in self.login.winfo_children():
            widget.destroy()
        
        if self.type == 's':
            self.type = 'm'
        else:
            self.type = 's'
        self.setting()


    def on_connect(self):
        global entry1, entry2
        entry1_val = entry1.get()
        entry2_val = entry2.get()

        if self.type == 's':
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
        if code == '' or name == '':
            messagebox.showwarning("알럿", "코드와 이름을 입력해주세요.")
        elif code != 'SKKU':
            messagebox.showwarning("알럿", "코드가 일치하지 않습니다.")
        else:
            self.assignment.lift()
            self.header.setting(self.type, name)
            self.header.lift()

    def setting(self):
        global entry1, entry2
        Label(self.login, text='Study Rush', bg='#FFFFFF', font=('Helvetica', 55, 'bold'), fg='#000000').place(x=540, y=100)
        
        entry1 = Entry(self.login, bg='#FFFFFF', width=45, fg='#000000')
        entry1.place(x=480, y=250)

        entry2 = Entry(self.login, bg='#FFFFFF', width=45, fg='#000000')
        entry2.place(x=480, y=310)

        Button(self.login, text='접속', bg='#FFFFFF', bd=0, font=('나눔고딕', 24), command=self.on_connect, fg='#000000', height=3, width=2).place(x=900, y=250)
        
        if self.type == 's':
            Label(self.login, text='학번 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=250)
            Label(self.login, text='이름 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=310)
            Button(self.login, text='관리자모드 이동     >', bg='black', font=('나눔고딕', 16), bd=0, command=self.mode_change).place(x=550, y=420)
        else:
            Label(self.login, text='관리자모드', bg = '#9DC238', font=('나눔고딕', 20, 'bold'), fg='#FFFFFF').place(x=640, y=65)
            Button(self.login, text='학생 모드 이동     >', bg='black', font=('나눔고딕', 16), bd=0, command=self.mode_change).place(x=550, y=420)
            Label(self.login, text='코드 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=250)
            Label(self.login, text='이름 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=310)


