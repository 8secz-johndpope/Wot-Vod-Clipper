#!/usr/bin/python

# Libs
import datetime
import tkinter as tk
# Locals
from ui.common.frames import DateFrame, SingleEntryFrame
import ui.common.elements_builder as eb


class VodDateRowFrame(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # Create
        self.label = tk.Label(self, text="Date", width=10)
        self.date = DateFrame(self)
        # Set date
        now = datetime.datetime.now()
        self.date.set(now.year, now.month, now.day)
        # Render
        self.label.grid(row=0, column=0,
                        padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)
        self.date.grid(row=0, column=1,
                       padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)
        pass


class VodIdRowFrame(SingleEntryFrame):
    def __init__(self, master, **kw):
        super().__init__(master,
                         name='Id', label_width=10,
                         entry_width=10,
                         **kw)
        pass


class VodTitleRowFrame(SingleEntryFrame):
    def __init__(self, master, **kw):
        super().__init__(master,
                         name='Title', label_width=10,
                         entry_width=90,
                         **kw)
        pass


class VodInfoFrame(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # Create
        self.date = VodDateRowFrame(self)
        self.id = VodIdRowFrame(self)
        self.title = VodTitleRowFrame(self)
        # Elements
        self.elements = [self.date, self.id, self.title]
        # Render
        for element in self.elements:
            element.pack(expand=True, fill='both')
        pass
