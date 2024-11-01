from tkinter import *
from tkinter import ttk
from utils import *

class Assignment:
    def __init__(self, root):
        self.root = root
        self.frame_setting()
        self.frame_add_setting()
        self.frame_list_setting()

    def complete_click(self, value):
        entry_value = self.entries[value-1].get()
        print(f'Row {value} Entry value: {entry_value}')

    def frame_add_setting(self):
        Label(self.assignment, text= '과제 추가', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=0)
        self.add = Frame(self.root)
        self.add.place(x=40, y=175, width=1180, height=130)
        self.add.configure(bg=LIGHT_GRAY)

        Label(self.add, text= '카테고리', bg=LIGHT_GRAY, font=FONT_18, fg=BLACK).place(x=30, y=20)
        Label(self.add, text= '과제명', bg=LIGHT_GRAY, font=FONT_18, fg=BLACK).place(x=300, y=20)
        Label(self.add, text= '마감 날짜 (YYYY-MM-DD)', bg=LIGHT_GRAY, font=FONT_18, fg=BLACK).place(x=800, y=20)

        self.combostyle()
        combo_values = ["러닝페어", "문제해결과 알고리즘 과제", "문제해결과 알고리즘 퀴즈"]
        combo = ttk.Combobox(self.add,  values=combo_values, background=LIGHT_GRAY)
        combo.place(x=30, y=60)

        Entry(self.add, bg=GRAY, width=50, fg=BLACK, bd=5, relief=FLAT, highlightthickness=0).place(x=300, y=60, height=30)
        Entry(self.add, bg=GRAY, width=30, fg=BLACK, bd=5, relief=FLAT, highlightthickness=0).place(x=800, y=60, height=30)
        Button(self.add, text='추가', font=FONT_16, bd=0, highlightthickness=0).place(x=1100, y=60, height=30)


    def frame_list_setting(self):
        Label(self.assignment, text= '과제 리스트', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=200)
        Button(self.assignment, text='파일로 내보내기', font=FONT_16, bd=0, highlightthickness=0).place(x=150, y=200)
        Button(self.assignment, text='통계보기', font=FONT_16, bd=0, highlightthickness=0).place(x=300, y=200)

        self.list = Frame(self.root)
        self.list.place(x=40, y=380, width=1180, height=370)
        self.list.configure(bg=LIGHT_GRAY)

        data = [
            ["", "카테고리", "과제명", "평균 소요 시간", "걸린 시간", ""],
            ["오늘", "러닝페어", "러닝페어 계획서 제출 (중요중요)", "20분", "", "완료"],
            ["D-2", "문제해결과 알고리즘 과제", "과제 2 제출하기", "50분", "", "완료"],
            ["완료", "문제해결과 알고리즘 과제", "과제 1 제출하기", "5분", "15분", ""]
        ]

        self.entries = []
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                if i == 0:
                    cell = Label(self.list, text=value, anchor=W, font=FONT_18_BOLD, padx=10, borderwidth=0, relief=SOLID, pady=5, bg=LIGHT_GRAY, fg=BLACK)
                elif j == 4 and value == '':
                    cell = Entry(self.list, bg=GRAY, fg=BLACK, font=FONT_16, relief=FLAT, bd=5, highlightthickness=0, width=8, justify=LEFT)
                    self.entries.append(cell)
                elif j == 5 and value == '완료':
                    cell = Button(self.list,text="완료",font=FONT_16_BOLD, width=3,height=1,bd=0,borderwidth=0,highlightthickness=0, command=lambda row_index=len(self.entries): self.complete_click(row_index))
                elif j == 0:
                    cell = Label(self.list, text=value, anchor=W, font=FONT_18_BOLD,  borderwidth=0, relief=SOLID, padx=10, pady=5, bg=GRAY, fg=BLACK)
                else:
                    cell = Label(self.list, text=value, anchor=W, font=FONT_18, borderwidth=0, relief=SOLID, padx=10, pady=5, bg=LIGHT_GRAY, fg=BLACK)

                if j != 0:
                    cell.grid(row=i, column=j, padx=10, pady=10, sticky=W)
                else:
                    cell.grid(row=i, column=j, padx=10, pady=10)

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
    
    def combostyle(self):
        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': GRAY,
                                       'fieldbackground': GRAY,
                                       'background': GRAY,
                                       'arrowcolor': '#8A8A8A',
                                       'relief': 'flat',
                                       'borderwidth': 0,
                                       'selectforeground': BLACK,
                                       'foreground': BLACK,
                                       'padding': 5, 
                                       'arrowsize': 20
                                       }}}
                         )
        combostyle.theme_use('combostyle') 