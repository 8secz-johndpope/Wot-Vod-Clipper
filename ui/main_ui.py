#!/usr/bin/python

# Libs
from tkinter import *
# Locals
from ui.clip_by_battle_frame_ui import ClipByBattleFrame
from ui.clip_by_duration_frame_ui import ClipByDurationFrame
from ui.common_frame_ui import CommonFrame, OutputFrame
import ui.common.elements_builder as eb
from ui.common.scrollable_frame import ScrollFrame

# Defines
_UI_TITLE = "World of Tanks VoD Clipper"
_UI_ICON_PATH = ""
UI_HEIGHT = 1024
UI_WIDTH = 670


class WotVodClipperUI(object):
    # ------------------------------------------------------------------------------------------------------------------
    # Instantiate elements

    def __init__(self):
        # --------------------------------
        # main ui
        self.main_ui = self.__build_main_ui()
        self.main_ui.geometry("{}x{}".format(UI_WIDTH, UI_HEIGHT))

        # --------------------------------
        # Scroll Bar
        self.scroll_frame = ScrollFrame(self.main_ui)
        self.scroll_frame.place(x=0, y=0, anchor="nw", width=UI_WIDTH, height=UI_HEIGHT)

        # --------------------------------
        # Notebook widget (tab control)
        # self.tab_control = ttk.Notebook(self.main_ui)

        # --------------------------------
        # Main frames
        self.common_frame = CommonFrame(self)
        self.clip_by_battle_frame = ClipByBattleFrame(self)
        self.clip_by_duration_frame = ClipByDurationFrame(self)
        self.output_frame = OutputFrame(self)
        pass

    def get(self):
        # return self.inner_frame
        return self.scroll_frame.inner_frame

    @staticmethod
    def __build_main_ui():
        ui = Tk()
        ui.title(_UI_TITLE)

        return ui

    def render(self):
        self.common_frame.get().grid(row=0, column=0,
                                     padx=eb.UI_FRAME_OUTSIDE_PAD, pady=eb.UI_FRAME_OUTSIDE_PAD,
                                     sticky=W + E)
        self.clip_by_battle_frame.get().grid(row=1, column=0, columnspan=3,
                                             padx=eb.UI_FRAME_OUTSIDE_PAD, pady=eb.UI_FRAME_OUTSIDE_PAD,
                                             sticky=W + E)
        self.clip_by_duration_frame.get().grid(row=2, column=0, columnspan=3,
                                               padx=eb.UI_FRAME_OUTSIDE_PAD, pady=eb.UI_FRAME_OUTSIDE_PAD,
                                               sticky=W + E)
        self.output_frame.get().grid(row=3, column=0, columnspan=3,
                                     padx=eb.UI_FRAME_OUTSIDE_PAD, pady=eb.UI_FRAME_OUTSIDE_PAD,
                                     sticky=W + E)

        self.main_ui.mainloop()
        pass
