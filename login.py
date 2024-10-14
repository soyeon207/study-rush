from tkinter import *
from tkinter import messagebox

login = ''
assignment = ''
student_entry = ''
name_entry = ''

def init(login_frame, assignment_frame):
    global login, assignment, type
    login = login_frame
    assignment = assignment_frame
    
def on_connect():
    global assignment, login, student_entry, name_entry
    student_id = student_entry.get()
    name = name_entry.get()

    if student_id == '' or name == '':
        messagebox.showwarning("알럿", "학번과 이름을 입력해주세요.")
    else:
        assignment.lift()

    print(f'학번: {student_id}, 이름: {name}')

def setting():
    global login, student_entry, name_entry
    Label(login, text='Study Rush', bg='#FFFFFF', font=('Helvetica', 55, 'bold'), fg='#000000').place(x=540, y=100)
    Label(login, text='학번 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=250)
    student_entry = Entry(login, bg='#FFFFFF', width=45, fg='#000000')
    student_entry.place(x=480, y=250)

    Label(login, text='이름 입력 : ', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=400, y=310)
    name_entry = Entry(login, bg='#FFFFFF', width=45, fg='#000000')
    name_entry.place(x=480, y=310)

    Button(login, text='접속', bg='#FFFFFF', bd=0, font=('나눔고딕', 24), command=on_connect, fg='#000000', height=3, width=2).place(x=900, y=250)
    Button(login, text='관리자모드 이동     >', bg='black', font=('나눔고딕', 16), bd=0).place(x=550, y=420)

