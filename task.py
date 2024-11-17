from tkinter import *
from tkinter import ttk, messagebox
from utils import *
from data import DataTask, DataAssignment
from datetime import datetime

class Task:
    def __init__(self, root, entities, components):
        self.root = root
        self.entities = entities
        self.data_task = DataTask()
        self.data_assignment = DataAssignment()
        self.setting()
        self.components = components
    
    def setting(self):
        self.setting_frame()
        self.setting_frame_add()
        self.setting_frame_list()

    def is_valid_date(self, date_str):
        try:
            date = datetime.strptime(date_str, DATE_FORMAT)
            return date 
        except ValueError:
            return False

    def btn_complete(self, value):
        entry_value = int(self.entries[value-1].get())
        if entry_value == 0:
            messagebox.showwarning("알럿", "걸린 시간을 입력해주세요.")
            return 

        self.data_task.complete(self.entities.get_student_number(), value, entry_value)
        self.list_sync()

    def btn_file(self):
        self.data_task.file(self.entities.get_student_number())
        messagebox.showinfo("알럿", "파일 저장 완료 (task.txt)")

    def btn_statistics(self):
        self.components.statistic.lift()

    def btn_add(self):
        data_name = self.entry_assignment.get()
        data_date = self.entry_task.get()
        data_assignment = self.combo.get()
        
        if self.btn_add_valid(data_name, data_date, data_assignment):
            self.data_task.add_task(self.entities.get_student_number(), data_date, data_assignment, data_name)
            self.list_sync()
            self.clear_entry()

    def clear_entry(self):
        self.entry_task.delete(0, END)
        self.entry_assignment.delete(0, END)
        self.combo.set('')

    def btn_add_valid(self, name, date, assignment):
        valid_date = self.is_valid_date(date)
        if name == '':
            messagebox.showwarning("알럿", "과제명을 입력해주세요.")
        elif date == '':
            messagebox.showwarning("알럿", "마감 날짜를 입력해주세요.")
        elif valid_date == False:
            messagebox.showwarning("알럿", "마감 날짜 형식(년-월-일) 을 맞춰서 입력해주세요.")
        elif valid_date < datetime.now():
            messagebox.showwarning("알럿", "오늘보다 큰 날짜를 입력해주세요.")
        elif assignment == '':
            messagebox.showwarning("알럿", "과제를 선택해주세요.")
        else:
            return True
        return False

    def setting_frame_add(self):
        Label(self.task, text= '작업 추가', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=0)
        self.add = Frame(self.root)
        self.add.place(x=40, y=175, width=1180, height=130)
        self.add.configure(bg=LIGHT_GRAY)

        Label(self.add, text= '과제', bg=LIGHT_GRAY, font=FONT_18, fg=BLACK).place(x=30, y=20)
        Label(self.add, text= '설명', bg=LIGHT_GRAY, font=FONT_18, fg=BLACK).place(x=300, y=20)
        Label(self.add, text= '마감 날짜 (YYYY-MM-DD)', bg=LIGHT_GRAY, font=FONT_18, fg=BLACK).place(x=800, y=20)

        self.combo = None
        self.combo_sync()

        self.entry_assignment = Entry(self.add, bg=GRAY, width=50, fg=BLACK, bd=5, relief=FLAT, highlightthickness=0)
        self.entry_assignment.place(x=300, y=60, height=30)
        self.entry_task = Entry(self.add, bg=GRAY, width=30, fg=BLACK, bd=5, relief=FLAT, highlightthickness=0)
        self.entry_task.place(x=800, y=60, height=30)
        Button(self.add, text='추가', font=FONT_16, bd=0, highlightthickness=0, command=self.btn_add).place(x=1100, y=60, height=30)

    def combo_sync(self):
        if self.combo != None:
            self.combo.destroy()

        combo_values = self.data_assignment.assignment_list()
        self.combo = ttk.Combobox(self.add,  values=combo_values, background=LIGHT_GRAY)
        self.combo.place(x=30, y=60)

    def setting_frame_list(self):
        Label(self.task, text= '작업 리스트', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=200)
        Button(self.task, text='파일로 내보내기', font=FONT_16, bd=0, highlightthickness=0, command=self.btn_file).place(x=150, y=200)
        Button(self.task, text='통계보기', font=FONT_16, bd=0, highlightthickness=0, command=self.btn_statistics).place(x=300, y=200)

        self.list = Frame(self.root)
        self.list.place(x=40, y=380, width=1180, height=370)
        self.list.configure(bg=LIGHT_GRAY)

    def list_sync(self):
        for widget in self.list.winfo_children():
            widget.destroy()
        
        data = self.data_task.format_data(self.entities.get_student_number())
        self.entries = []
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                if i == 0:
                    # 제목 -> Label
                    cell = Label(self.list, text=value, anchor=W, font=FONT_18_BOLD, padx=10, borderwidth=0, relief=SOLID, pady=5, bg=LIGHT_GRAY, fg=BLACK)
                elif j == 4 and value == '':
                    # 걸린 시간을 입력받아야 하는 경우 -> Entry
                    cell = Entry(self.list, bg=GRAY, fg=BLACK, font=FONT_16, relief=FLAT, bd=5, highlightthickness=0, width=8, justify=LEFT)
                    self.entries.append(cell)
                elif j == 5 and value == '완료':
                    # 작업이 완료되지 않은 경우 -> Button
                    cell = Button(self.list,text="완료",font=FONT_16_BOLD, width=3,height=1,bd=0,borderwidth=0,highlightthickness=0, command=lambda row_index=len(self.entries): self.btn_complete(row_index))
                elif j == 0:
                    # 1열은 뱃지로 -> bg 컬러를 다르게, 텍스트를 bold 로
                    cell = Label(self.list, text=value, anchor=W, font=FONT_18_BOLD,  borderwidth=0, relief=SOLID, padx=10, pady=5, bg=GRAY, fg=BLACK)
                else:
                    # 그 외의 경우 일반적인 텍스트로
                    cell = Label(self.list, text=value, anchor=W, font=FONT_18, borderwidth=0, relief=SOLID, padx=10, pady=5, bg=LIGHT_GRAY, fg=BLACK)

                if i != 0 and j == 4 and value != '':
                    self.entries.append('')

                if j != 0:
                    cell.grid(row=i, column=j, padx=10, pady=10, sticky=W)
                else:
                    cell.grid(row=i, column=j, padx=10, pady=10)

        for j in range(len(data[0])):
            self.list.grid_columnconfigure(j, weight=1)

    def setting_frame(self):
        self.task = Frame(self.root)
        self.task.place(x=0, y=140, width=1280, height=692)
        self.task.configure(bg=WHITE)

    def lift(self):
        self.list_sync()
        self.task.lift()
        self.list.lift()
        self.add.lift()
        self.combo_sync()
        
    
