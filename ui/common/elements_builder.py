#!/usr/bin/python

# Libs
from tkinter import *
# Locals


# Defines
UI_ELEMENT_PAD_X = 5
UI_ELEMENT_PAD_Y = 5
UI_FRAME_INSIDE_PAD = 10
UI_FRAME_OUTSIDE_PAD = 10


def build_label(parent, text):
    return Label(parent, text=text)


def build_entry(parent, width):
    return Entry(parent, width=width)


def build_button(parent, text, callback):
    return Button(parent, text=text, command=callback)
