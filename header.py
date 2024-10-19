from tkinter import *
header = None
type = None
name = None

def init(_header):
    global header
    header = _header

def setting(_type, _name):
    global type
    type = _type
    Label(header, text='Study Rush', bg='#FFFFFF', font=('Helvetica', 50, 'bold'), fg='#000000').place(x=20, y=20)
    Label(header, text= _name + ' 님 안녕하세요', bg='#FFFFFF', font='나눔고딕', fg='#000000').place(x=330, y=50)
    if type == 'm':
        Label(header, text='관리자모드', bg = '#9DC238', font=('나눔고딕', 20, 'bold'), fg='#FFFFFF').place(x=1100, y=50)
    
    
    
    

