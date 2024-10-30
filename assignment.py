from tkinter import *
from tkinter import messagebox, ttk

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
        Label(self.assignment, text= '과제 추가', bg='#FFFFFF', font=('나눔고딕', 18, 'bold'), fg='#000000').place(x=40, y=0)
        self.add = Frame(self.root)
        self.add.place(x=40, y=175, width=1180, height=130)
        self.add.configure(bg='#F2F2F2')

        Label(self.add, text= '카테고리', bg='#F2F2F2', font=('나눔고딕', 18), fg='#000000').place(x=30, y=20)
        Label(self.add, text= '과제명', bg='#F2F2F2', font=('나눔고딕', 18), fg='#000000').place(x=300, y=20)
        Label(self.add, text= '마감 날짜 (YYYY-MM-DD)', bg='#F2F2F2', font=('나눔고딕', 18), fg='#000000').place(x=800, y=20)

        combo = ttk.Combobox(self.add, state="readonly",  values = ["Python", "C", "C++", "Java"], background='#F2F2F2')
        combo.place(x=30, y=60)

        Entry(self.add, bg='#D9D9D9', width=50, fg='#000000', bd=0, highlightthickness=0).place(x=300, y=60, height=30)
        Entry(self.add, bg='#D9D9D9', width=30, fg='#000000', bd=0, highlightthickness=0).place(x=800, y=60, height=30)
        Button(self.add, text='추가', font=('나눔고딕', 16), bd=0, highlightthickness=0).place(x=1100, y=60, height=30)


    def frame_list_setting(self):
        Label(self.assignment, text= '과제 리스트', bg='#FFFFFF', font=('나눔고딕', 18, 'bold'), fg='#000000').place(x=40, y=200)
        Button(self.assignment, text='파일로 내보내기', font=('나눔고딕', 16), bd=0, highlightthickness=0).place(x=150, y=200)
        Button(self.assignment, text='통계보기', font=('나눔고딕', 16), bd=0, highlightthickness=0).place(x=300, y=200)

        self.list = Frame(self.root)
        self.list.place(x=40, y=380, width=1180, height=370)
        self.list.configure(bg='#F2F2F2')

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
                    cell = Label(self.list, text=value, anchor='w', font=('나눔고딕', 18, 'bold'), padx=10, borderwidth=0, relief="solid", pady=5, bg='#F2F2F2', fg='#000000')
                elif j == 4 and value == '':
                    cell = Entry(self.list, bg='#D9D9D9', fg='#000000', font=('Arial', 18), bd=0, highlightthickness=0, width=8, justify='center')
                    self.entries.append(cell)
                elif j == 5 and value == '완료':
                    print('i : ', i)
                    cell = Button(self.list,text="완료",font=("나눔고딕", 15, "bold"),width=3,height=1,bd=0,borderwidth=0,highlightthickness=0, command=lambda row_index=len(self.entries): self.complete_click(row_index))
                elif j == 0:
                    cell = Label(self.list, text=value, anchor='w', font=('나눔고딕', 18, 'bold'),  borderwidth=0, relief="solid", padx=10, pady=5, bg='#D9D9D9', fg='#000000')
                else:
                    cell = Label(self.list, text=value, anchor='w', font=('나눔고딕', 18), borderwidth=0, relief="solid", padx=10, pady=5, bg='#F2F2F2', fg='#000000')

                cell.grid(row=i, column=j, padx=10, pady=10)

        # 열 크기 고정
        for j in range(len(data[0])):
            self.list.grid_columnconfigure(j, weight=1)


    def frame_setting(self):
        self.assignment = Frame(self.root)
        self.assignment.place(x=0, y=140, width=1280, height=692)
        self.assignment.configure(bg='#FFFFFF')

    def lift(self):
        self.assignment.lift()
    
