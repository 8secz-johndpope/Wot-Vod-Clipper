#!/usr/bin/python

# Libs
import tkinter as tk
# Locals


# Defines
UI_ELEMENT_PAD_X = 5
UI_ELEMENT_PAD_Y = 5
UI_FRAME_INSIDE_PAD = 10
UI_FRAME_OUTSIDE_PAD = 10


def build_label(parent, text):
    return tk.Label(parent, text=text)


def build_entry(parent, width):
    return tk.Entry(parent, width=width)


def build_button(parent, text, callback):
    return tk.Button(parent, text=text, command=callback)
