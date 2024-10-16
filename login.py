from tkinter import *
from tkinter import messagebox

login = ''
assignment = ''
entry1 = ''
entry2 = ''
type = '' # s = student, m = master

def init(login_frame, assignment_frame, type_):
    global login, assignment, type
    login = login_frame
    assignment = assignment_frame
    type = type_
    
def mode_change():
    global type, login
    for widget in login.winfo_children():
        widget.destroy()
    
    if type == 's':
        type = 'm'
    else:
        type = 's'

    setting()


def on_connect():
    global entry1, entry2, type
    entry1_val = entry1.get()
    entry2_val = entry2.get()

    if type == 's':
        valid_student(entry1_val, entry2_val)
    else:
        valid_master(entry1_val, entry2_val)


def valid_student(student_id, name):
    global assignment

    if student_id == '' or name == '':
        messagebox.showwarning("알럿", "학번과 이름을 입력해주세요.")
    else:
        print('>>>>> 학생 접속 >>>>>')
        print(f'학번: {student_id}, 이름: {name}')
        assignment.lift()

def valid_master(code, name):
    global assignment

    if code == '' or name == '':
        messagebox.showwarning("알럿", "코드와 이름을 입력해주세요.")
    elif code != 'SKKU':
        messagebox.showwarning("알럿", "코드가 일치하지 않습니다.")
    else:
        print('>>>>> 관리자 접속 >>>>>')
        print(f'코드: {code}, 이름: {name}')
        assignment.lift()

def setting():
    global login, entry1, entry2

    Label(login, text='Study Rush', bg='#FFFFFF', font=('Helvetica', 55, 'bold'), fg='#000000').place(x=540, y=100)
    
    entry1 = Entry(login, bg='#FFFFFF', width=45, fg='#000000')
    entry1.place(x=480, y=250)

    entry2 = Entry(login, bg='#FFFFFF', width=45, fg='#000000')
    entry2.place(x=480, y=310)

    Button(login, text='접속', bg='#FFFFFF', bd=0, font=('나눔고딕', 24), command=on_connect, fg='#000000', height=3, width=2).place(x=900, y=250)
    
    if type == 's':
        Label(login, text='학번 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=250)
        Label(login, text='이름 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=310)
        Button(login, text='관리자모드 이동     >', bg='black', font=('나눔고딕', 16), bd=0, command=mode_change).place(x=550, y=420)
    else:
        Label(login, text='관리자모드', bg = '#9DC238', font=('나눔고딕', 20, 'bold'), fg='#FFFFFF').place(x=640, y=65)
        Button(login, text='학생 모드 이동     >', bg='black', font=('나눔고딕', 16), bd=0, command=mode_change).place(x=550, y=420)
        Label(login, text='코드 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=250)
        Label(login, text='이름 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=310)


