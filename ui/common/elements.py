#!/usr/bin/python
from __future__ import annotations

# Libs
import tkinter as tk
# Locals
import ui.common.elements_builder as eb


class ThreeStageFrame(tk.Frame):
    def __init__(self, master,
                 first_stage_from=0, first_stage_to=100, first_stage_size=2,
                 first_symbol='-',
                 second_stage_from=0, second_stage_to=100, second_stage_size=2,
                 second_symbol='-',
                 third_stage_from=0, third_stage_to=100, third_stage_size=2,
                 third_symbol='',
                 **kw):
        super().__init__(master, **kw)

        # Variables
        self.first_var = tk.IntVar()
        self.first_var.set(0)
        self.second_var = tk.IntVar()
        self.second_var.set(0)
        self.third_var = tk.IntVar()
        self.third_var.set(0)

        # Create
        self.first_element = tk.Spinbox(self, from_=first_stage_from, to=first_stage_to, width=first_stage_size,
                                        textvariable=self.first_var, wrap=True)
        self.second_element = tk.Spinbox(self, from_=second_stage_from, to=second_stage_to, width=second_stage_size,
                                         textvariable=self.second_var, wrap=True)
        self.third_element = tk.Spinbox(self, from_=third_stage_from, to=third_stage_to, width=third_stage_size,
                                        textvariable=self.third_var, wrap=True)
        self.first_symbol_label = tk.Label(self, text=first_symbol)
        self.second_symbol_label = tk.Label(self, text=second_symbol)
        self.third_symbol_label = tk.Label(self, text=third_symbol)

        # Render
        self.first_element.grid(row=0, column=0)
        self.first_symbol_label.grid(row=0, column=1)
        self.second_element.grid(row=0, column=2)
        self.second_symbol_label.grid(row=0, column=3)
        self.third_element.grid(row=0, column=4)
        self.third_symbol_label.grid(row=0, column=5)
        pass

    def set(self, first, second, third):
        self.first_var.set(first)
        self.second_var.set(second)
        self.third_var.set(third)
        pass

    def copy(self, old_frame):
        self.set(old_frame.first_var.get(), old_frame.second_var.get(), old_frame.third_var.get())
        pass


class TimeStampFrame(ThreeStageFrame):
    def __init__(self, master, **kw):
        super().__init__(master,
                         first_stage_from=0, first_stage_to=20, first_stage_size=2,
                         first_symbol=':',
                         second_stage_from=0, second_stage_to=59, second_stage_size=2,
                         second_symbol=':',
                         third_stage_from=0, third_stage_to=59, third_stage_size=2,
                         third_symbol='    ',
                         **kw)
        pass


class DateFrame(ThreeStageFrame):
    def __init__(self, master, **kw):
        super().__init__(master,
                         first_stage_from=2020, first_stage_to=3000, first_stage_size=4,
                         first_symbol='-',
                         second_stage_from=1, second_stage_to=12, second_stage_size=2,
                         second_symbol='-',
                         third_stage_from=1, third_stage_to=31, third_stage_size=2,
                         **kw)
        pass


class SingleEntryFrame(tk.Frame):
    def __init__(self, master,
                 name="Name", label_width=10,
                 entry_default_text='', entry_width=10,
                 **kw):
        super().__init__(master, **kw)

        # Create
        self.label = tk.Label(self, text=name, width=label_width)
        self.entry = tk.Entry(self, width=entry_width)
        # Configuration
        self.entry.insert(0, entry_default_text)
        # Render
        self.label.grid(row=0, column=0,
                        padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)
        self.entry.grid(row=0, column=1,
                        padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)
        pass
