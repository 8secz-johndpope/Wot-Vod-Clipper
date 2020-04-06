#!/usr/bin/python

# from https://gist.github.com/mp035/9f2027c3ef9172264532fcd6262f3b01

import tkinter as tk


class ScrollFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)  # create a frame (self)

        self.canvas = tk.Canvas(self, borderwidth=0)
        self.inner_frame = tk.Frame(self.canvas)
        self.scroll_bar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.scroll_bar.set)

        self.scroll_bar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window((4, 4), window=self.inner_frame, anchor="nw",
                                                       tags="self.inner_frame")

        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.on_frame_configure(None)

    def on_frame_configure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)
