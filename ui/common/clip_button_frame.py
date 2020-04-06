#!/usr/bin/python

# Libs
import tkinter as tk
# Locals
import ui.common.elements_builder as eb


class ClipButtonFrame(tk.Frame):
    def __init__(self, parent, text, button_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)  # create a frame (self)

        self.button = eb.build_button(self, text, button_callback)

        self.button.pack(expand=True, fill='both')
        pass
