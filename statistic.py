from tkinter import *
from tkinter import ttk
from utils import *

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Statistic:
    def __init__(self, root):
        self.root = root
        self.setting()
        self.circle()
        self.stick()

    def setting(self):        
        self.statistic = Frame(self.root)
        self.statistic.place(x=0, y=140, width=1280, height=692)
        self.statistic.configure(bg=WHITE)

        Label(self.statistic, text= '카테고리별 통계 보기', bg=WHITE, font=FONT_18_BOLD, fg=BLACK).place(x=40, y=0)
        combo = ttk.Combobox(self.statistic, state="readonly",  values = ["Python", "C", "C++", "Java"], background=LIGHT_GRAY)
        combo.place(x=40, y=40)

        Label(self.statistic, text= '완료 인원 / 총인원', bg=WHITE, font=FONT_18, fg=BLACK).place(x=50, y=120)
        Label(self.statistic, text= '소요 기간', bg=WHITE, font=FONT_18, fg=BLACK).place(x=650, y=120)

    def circle(self):
        ratio = [34, 32, 16, 18]
        labels = ['Apple', 'Banana', 'Melon', 'Grapes']

        fig, ax = plt.subplots()
        fig.set_size_inches(2.5, 2.5)
        ax.pie(ratio, labels=labels, autopct='%.1f%%')

        # Figure를 Tkinter의 Canvas로 변환하여 표시
        canvas = FigureCanvasTkAgg(fig, master=self.statistic)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=100, y=150)
        
    def stick(self):
        x = np.arange(3)
        years = ['2018', '2019', '2020']
        values = [100, 400, 900]

        fig, ax = plt.subplots()
        fig.set_size_inches(2.5, 2.5)  # 크기 설정
        ax.bar(x, values)

        ax.set_xticks(x)
        ax.set_xticklabels(years, fontsize=8)
        ax.tick_params(axis='y', labelsize=6)

        canvas = FigureCanvasTkAgg(fig, master=self.statistic)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=700, y=150)