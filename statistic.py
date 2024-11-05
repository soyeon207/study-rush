from tkinter import *
from tkinter import ttk
from utils import *
from collections import Counter
from data import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Statistic:
    LABEL_FONT_SIZE = 8
    TITLE_FONT_SIZE = 13

    def __init__(self, root, class_factory):
        self.root = root
        self.class_factory = class_factory
        plt.rcParams['font.family'] = 'AppleGothic'
        self.setting()

    def on_combobox_selected(self, event):
        selected_value = self.combo.get()
        self.pie(selected_value)
        self.bar(selected_value)

    def btn_back(self):
        self.class_factory.assignment.lift()

    def setting(self):        
        self.statistic = Frame(self.root)
        self.statistic.place(x=0, y=140, width=1280, height=692)       
        self.statistic.configure(bg=WHITE)

        self.data_category = DataCategory()

        Label(self.statistic, text= '카테고리별 통계 보기', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=0)
        category_list = list(DataCategory().category_list())
        self.combo = ttk.Combobox(self.statistic, height=15, state="readonly",  values = category_list, background=LIGHT_GRAY)
        self.combo.place(x=40, y=40)
        self.combo.bind("<<ComboboxSelected>>", self.on_combobox_selected)

        Button(self.statistic, text='뒤로 가기', font=FONT_16, bd=0, highlightthickness=0, command=self.btn_back).place(x=1150, y=0)

    def pie(self, category):
        ratio = self.data_category.statistic_pie_data(category)
        if ratio[0] == 0 and ratio[1] == 0:
            messagebox.showwarning('알럿', '데이터가 없습니다.')
            return

        labels = ['완료 수', '미완료 수']
        
        fig, ax = plt.subplots()
        fig.set_size_inches(5, 5)
        ax.pie(ratio, labels=labels, autopct='%.1f%%')
        ax.set_title('완료 수 통계', fontsize=self.TITLE_FONT_SIZE)

        self.add_canvas_to_statistic(fig, 30, 90)
        
    def bar(self, category):
        years = self.data_category.statistic_bar_data(category)
        year_counts = Counter(years)

        x = list(year_counts.keys())  # 연도 (X축)
        values = list(year_counts.values())  # 각 연도의 개수 (Y축)

        fig, ax = plt.subplots()
        fig.set_size_inches(5, 5)  # 크기 설정
        ax.bar(x, values)

        ax.set_xlabel('걸린 시간', fontsize=self.LABEL_FONT_SIZE)
        ax.set_ylabel('인원 수 ', fontsize=self.LABEL_FONT_SIZE)
        ax.set_title('소요 시간 통계', fontsize=self.TITLE_FONT_SIZE)
        ax.set_xticks(x)
        ax.set_xticklabels(x, fontsize=self.LABEL_FONT_SIZE)
        ax.tick_params(axis='y', labelsize=6)
        ax.yaxis.get_major_locator().set_params(integer=True)

        self.add_canvas_to_statistic(fig, 650, 90)
        

    def add_canvas_to_statistic(self, fig, x, y):
        canvas = FigureCanvasTkAgg(fig, master=self.statistic)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=x, y=y)

    def lift(self):
        self.statistic.lift()