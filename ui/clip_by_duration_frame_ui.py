#!/usr/bin/python

# Libs
from tkinter import *
# Locals
import ui.common.elements_builder as eb
from ui.common.clip_button_frame import ClipButtonFrame

# Defines
_UI_INT_INPUT_BAR_WIDTH = 5


class ClipByDurationFrame:
    def __init__(self, parent_object):
        self.frame = LabelFrame(parent_object.get(),
                                text="Clip By Duration",
                                borderwidth=1,
                                padx=eb.UI_FRAME_INSIDE_PAD, pady=eb.UI_FRAME_INSIDE_PAD)

        self.sub_frame = Frame(self.frame)
        self.sub_frame.pack(expand=True, fill='both')
        # -- Duration
        # Build
        self.duration_label = eb.build_label(self.sub_frame, "Duration")
        self.duration_entry = eb.build_entry(self.sub_frame, _UI_INT_INPUT_BAR_WIDTH)
        self.duration_unit_label = eb.build_label(self.sub_frame, "minute(s)")
        # Place
        self.duration_label.grid(row=0, column=0, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y, sticky=W)
        self.duration_entry.grid(row=0, column=1, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)
        self.duration_unit_label.grid(row=0, column=2, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y, sticky=W)
        # Preset
        self.duration_entry.insert(0, "20")
        # Finish

        # # -- Clip Button
        self.clip_button_frame = ClipButtonFrame(self.frame, "Clip", self._clip)
        self.clip_button_frame.pack(expand=True, fill='both')

        # Recording
        self.parent_object = parent_object
        pass

    def get(self):
        return self.frame

    @staticmethod
    def _clip():
        # TODO
        print("CLIPPPPPPP")
        pass
