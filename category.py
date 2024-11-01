from tkinter import *
from utils import *
from data import DataCategory

class Category:
    def __init__(self, root):
        self.root = root
        self.frame_setting()
        self.frame_add_setting()
        self.frame_list_setting()

    def add_button(self):
        category_val = self.entry_category.get()

    def frame_add_setting(self):
        Label(self.assignment, text= '과제 추가', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=0)
        self.add = Frame(self.root)
        self.add.place(x=40, y=175, width=1180, height=130)
        self.add.configure(bg=LIGHT_GRAY)

        Label(self.add, text= '카테고리', bg=LIGHT_GRAY, font=FONT_18, fg=BLACK).place(x=30, y=20)
        self.entry_category = Entry(self.add, bg=GRAY, width=115, fg=BLACK, bd=5, relief=FLAT, highlightthickness=0)
        self.entry_category.place(x=30, y=60, height=30)
        Button(self.add, text='추가', font=FONT_16, bd=0, highlightthickness=0, command=self.add_button).place(x=1100, y=60, height=30)

    def frame_list_setting(self):
        Label(self.assignment, text= '카테고리 리스트', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=200)
        Button(self.assignment, text='파일로 내보내기', font=FONT_16, bd=0, highlightthickness=0).place(x=180, y=200)
        Button(self.assignment, text='통계보기', font=FONT_16, bd=0, highlightthickness=0).place(x=330, y=200)

        self.list = Frame(self.root)
        self.list.place(x=40, y=380, width=1180, height=370)
        self.list.configure(bg=LIGHT_GRAY)

        data = DataCategory().format_data()
        self.entries = []
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                if i == 0:
                    cell = Label(self.list, anchor=W, text=value, font=FONT_18_BOLD, borderwidth=0, padx=20, pady=5, relief=SOLID, bg=LIGHT_GRAY, fg=BLACK)
                else:
                    cell = Label(self.list, text=value, anchor=W, font=FONT_18, borderwidth=0, bg=LIGHT_GRAY, padx=20, pady=5, fg=BLACK)
                cell.grid(row=i, column=j, padx=3, pady=10, sticky=W)

        for j in range(len(data[0])):
            self.list.grid_columnconfigure(j, weight=1)


    def frame_setting(self):
        self.assignment = Frame(self.root)
        self.assignment.place(x=0, y=140, width=1280, height=692)
        self.assignment.configure(bg=WHITE)

    def lift(self):
        self.assignment.lift()
        self.list.lift()
        self.add.lift()
    
