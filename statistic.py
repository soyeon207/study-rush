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

    def __init__(self, root, entities, components):
        self.root = root
        self.entities = entities
        self.components = components
        plt.rcParams['font.family'] = 'AppleGothic'
        self.setting()

    def on_combobox_selected(self, event):
        self.clear()
        selected_value = self.combo.get()
        self.pie(selected_value)
        self.bar(selected_value)

    def btn_back(self):
        if self.entities.is_student():
            self.components.assignment.lift()
        else:
            self.components.category.lift()

    def setting(self):        
        self.statistic = Frame(self.root)
        self.statistic.place(x=0, y=140, width=1280, height=100)       
        self.statistic.configure(bg=WHITE)

        self.statistical_data = Frame(self.root)
        self.statistical_data.place(x=0, y=240, width=1280, height=592)       
        self.statistical_data.configure(bg=WHITE)

        self.data_category = DataCategory()
        Label(self.statistic, text= '과제별 통계 보기', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=0)
        Button(self.statistic, text='뒤로 가기', font=FONT_16, bd=0, highlightthickness=0, command=self.btn_back).place(x=1150, y=0)

        self.combo = None
        self.combo_sync()

    def combo_sync(self):
        if self.combo != None:
            self.combo.destroy()

        category_list = list(DataCategory().category_list())
        self.combo = ttk.Combobox(self.statistic, height=15, state="readonly",  values = category_list, background=LIGHT_GRAY)
        self.combo.place(x=40, y=40)
        self.combo.bind("<<ComboboxSelected>>", self.on_combobox_selected)

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
        if len(years) == 0:
            return
    
        year_counts = Counter(years)
        x = list(year_counts.keys())
        values = list(year_counts.values()) 

        fig, ax = plt.subplots()
        fig.set_size_inches(5, 5)
        ax.bar(x, values)

        ax.set_xlabel('걸린 시간 (분)', fontsize=self.LABEL_FONT_SIZE)
        ax.set_ylabel('인원 수 ', fontsize=self.LABEL_FONT_SIZE)
        ax.set_title('소요 시간 통계', fontsize=self.TITLE_FONT_SIZE)
        ax.set_xticks(x)
        ax.set_xticklabels(x, fontsize=self.LABEL_FONT_SIZE)
        ax.tick_params(axis='y', labelsize=6)
        ax.yaxis.get_major_locator().set_params(integer=True)

        self.add_canvas_to_statistic(fig, 650, 90)
    
    def add_canvas_to_statistic(self, fig, x, y):
        self.canvas = FigureCanvasTkAgg(fig, master=self.statistical_data)
        self.canvas.draw()
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.place(x=x, y=y)

    def lift(self):
        self.statistic.lift()
        self.statistical_data.lift()
        self.clear()
        self.combo_sync()
    
    def clear(self):
        for widget in self.statistical_data.winfo_children():
            widget.destroy()