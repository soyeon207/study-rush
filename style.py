from tkinter import ttk
from utils import *

def combostyle():
    combostyle = ttk.Style()
    combostyle.theme_create('combostyle', parent='alt',
                        settings = {'TCombobox':
                                    {'configure':
                                    {'selectbackground': GRAY,
                                    'fieldbackground': GRAY,
                                    'background': GRAY,
                                    'arrowcolor': DARK_GRAY,
                                    'relief': 'flat',
                                    'borderwidth': 10,
                                    'selectforeground': BLACK,
                                    'foreground': BLACK,
                                    'padding': 5, 
                                    'arrowsize': 20
                                    }}}
                        )
    combostyle.theme_use('combostyle') 