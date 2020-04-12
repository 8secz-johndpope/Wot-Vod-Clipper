#!/usr/bin/python
from __future__ import annotations

# Libs
import tkinter as tk
# Locals


class TimeStampFrame(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # Variables
        self.hour_var = tk.IntVar()
        self.hour_var.set(0)
        self.minute_var = tk.IntVar()
        self.minute_var.set(0)
        self.second_var = tk.IntVar()
        self.second_var.set(0)

        # Create
        self.hour_element = tk.Spinbox(self, from_=0, to=99, wrap=True,
                                       textvariable=self.hour_var, width=2)
        self.minute_element = tk.Spinbox(self, from_=0, to=59, wrap=True,
                                         textvariable=self.minute_var, width=2)
        self.second_element = tk.Spinbox(self, from_=0, to=59, wrap=True,
                                         textvariable=self.second_var, width=2)
        self.hm_label = tk.Label(self, text=':')
        self.ms_label = tk.Label(self, text=':')
        self.s_label = tk.Label(self, text='    ')

        # Render
        self.hour_element.grid(row=0, column=0)
        self.hm_label.grid(row=0, column=1)
        self.minute_element.grid(row=0, column=2)
        self.ms_label.grid(row=0, column=3)
        self.second_element.grid(row=0, column=4)
        self.s_label.grid(row=0, column=5)
        pass

    def _hour_invalid(self):
        self.hour_var.set(0)
        pass

    def _minute_invalid(self):
        self.minute_var.set(0)
        pass

    def _second_invalid(self):
        self.second_var.set(0)
        pass

    def set(self, hour, minute, second):
        self.hour_var.set(hour)
        self.minute_var.set(minute)
        self.second_var.set(second)
        pass

    def copy(self, old_frame: TimeStampFrame):
        self.set(old_frame.hour_var.get(), old_frame.minute_var.get(), old_frame.second_var.get())
        pass
