from tkinter import *
import login as m

root = Tk()
root.title('Study Rush')
root.geometry('1280x832+500+150')

assignment = Frame(root)
statistics = Frame(root)
login = Frame(root)

statistics.place(x=0, y=0, width=1280, height=832)
assignment.place(x=0, y=0, width=1280, height=832)
login.place(x=0, y=0, width=1280, height=832)

statistics.configure(bg='#FFFFFF')
assignment.configure(bg='#FFFFFF')
login.configure(bg='#FFFFFF')

m.init(login, assignment, 's')
m.setting()

root.mainloop()
