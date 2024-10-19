from tkinter import *
import login as m
import assignment as a
import header as h

root = Tk()
root.title('Study Rush')
root.geometry('1280x832+500+150')

header = Frame(root)
assignment = Frame(root)
statistics = Frame(root)
login = Frame(root)

statistics.place(x=0, y=140, width=1280, height=692)
assignment.place(x=0, y=140, width=1280, height=692)
header.place(x=0, y=0, width=1280, height=140)
login.place(x=0, y=0, width=1280, height=832)

header.configure(bg='#FFFFFF')
statistics.configure(bg='#FFFFFF')
assignment.configure(bg='#FFFFFF')
login.configure(bg='#FFFFFF')

m.init(_login = login, _assignment = assignment, _type = 's', _header = header)
a.init(login)
h.init(header)

root.mainloop()
