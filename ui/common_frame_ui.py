#!/usr/bin/python

# Libs
from tkinter import *
from tkinter import filedialog
# Locals
import ui.common.elements_builder as eb

# Defines
DEFAULT_OPEN_FILE_PATH = "D:\\Twitch"
_UI_PATH_INPUT_BAR_WIDTH = 80


# each frame builder
class CommonFrame:
    def __init__(self, parent_object):
        self.frame = LabelFrame(parent_object.get(),
                                text="Files",
                                borderwidth=1,
                                padx=eb.UI_FRAME_INSIDE_PAD, pady=eb.UI_FRAME_INSIDE_PAD)

        # Build
        self.in_file_label = eb.build_label(self.frame, "Video File")
        self.in_file_entry = _build_file_entry(self.frame)
        self.in_file_button = _build_file_button(self.frame, self.update_input_filename)
        self.out_dir_label = eb.build_label(self.frame, "Output Folder")
        self.out_dir_entry = _build_file_entry(self.frame)
        self.out_dir_button = _build_file_button(self.frame, self.update_output_dir)

        # Place
        self.in_file_label.grid(row=0, column=0, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y, sticky=W)
        self.in_file_entry.grid(row=0, column=1, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)
        self.in_file_button.grid(row=0, column=2, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)
        self.out_dir_label.grid(row=1, column=0, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y, sticky=W)
        self.out_dir_entry.grid(row=1, column=1, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)
        self.out_dir_button.grid(row=1, column=2, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)

        # Preset
        self.out_dir_entry.insert(0, DEFAULT_OPEN_FILE_PATH)

        # Recording
        self.parent_object = parent_object
        pass

    def get(self):
        return self.frame

    def update_input_filename(self):
        in_filename = filedialog.askopenfilename(initialdir=DEFAULT_OPEN_FILE_PATH)
        self.in_file_entry.delete(0, END)
        self.in_file_entry.insert(0, in_filename)
        pass

    def update_output_dir(self):
        out_dir = filedialog.askdirectory(initialdir=DEFAULT_OPEN_FILE_PATH)
        self.out_dir_entry.delete(0, END)
        self.out_dir_entry.insert(0, out_dir)
        pass


class OutputFrame:
    def __init__(self, parent_object):
        self.frame = LabelFrame(parent_object.get(),
                                text="Output",
                                borderwidth=1,
                                padx=eb.UI_FRAME_INSIDE_PAD, pady=eb.UI_FRAME_INSIDE_PAD)
        self.content = StringVar()

        # Build
        # TODO: output text field
        label = Label(self.frame, textvariable=self.content)

        # Place
        # TODO
        label.grid(row=0, column=0, sticky=W+E)

        # Recording
        self.parent = parent_object
        pass

    def get(self):
        return self.frame


def _build_file_entry(parent):
    return eb.build_entry(parent, _UI_PATH_INPUT_BAR_WIDTH)


def _build_file_button(parent, callback):
    return eb.build_button(parent, "...", callback)
