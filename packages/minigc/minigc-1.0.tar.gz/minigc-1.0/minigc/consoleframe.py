#!/usr/bin/env python
# coding:utf-8
# created by Peixuan Shu
# 2023.2.21

import tkinter as tk
# from tkinter import ttk
from datetime import datetime

green = '#95C943'
font = 'TkDefaultFont'+' ' # Times

class ConsoleFrame(tk.Frame):

    def __init__(self, root, main_gui):
        self.scale = root.scale_factor
        super().__init__(root, width=int(850*self.scale), height=int(100*self.scale), bd=2, relief='ridge')

        self.main_gui = main_gui

        self.pack(side='top',fill='both')
        self.grid_propagate(0) # 0

        self.console_text = tk.Text(self, fg="green", bg="black", width=73, height=10, state=tk.DISABLED)
        scrollbar = tk.Scrollbar(self, width=int(20*self.scale), command=self.console_text.yview)
        scrollbar.pack(side="right", fill=tk.Y)
        self.console_text.pack(expand=1, fill=tk.BOTH)
        self.console_text['yscrollcommand'] = scrollbar.set

        self.console_row = 0
    
    def print_console(self, msg, color="white"):
        self.console_row = self.console_row + 1
        self.console_text.config(state=tk.NORMAL)
        hour = datetime.now().strftime("%H")
        min = datetime.now().strftime("%M")
        sec = datetime.now().strftime("%S")
        time = ("[{}:{}:{}] ").format(hour,min,sec)
        self.console_text.insert(tk.END, time + msg+'\n', 'text_marker'+str(self.console_row))
        self.console_text.tag_config('text_marker'+str(self.console_row), foreground=color)
        # self.console_text.tag_remove('text_marker', )
        self.console_text.see(tk.END)
        self.console_text.config(state=tk.DISABLED)