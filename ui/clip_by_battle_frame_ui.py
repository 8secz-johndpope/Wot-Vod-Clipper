#!/usr/bin/python

# Libs
import datetime
from tkinter import *
# Locals
import ui.common.elements_builder as eb
from ui.clip_by_battle_battle_info_fram_ui import ClipByBattleBattleInfoFrame


# Defines


class ClipByBattleFrame:
    def __init__(self, parent_object):
        self.frame = LabelFrame(parent_object.get(),
                                text="Clip By Battle",
                                borderwidth=1,
                                height=2500,
                                padx=eb.UI_FRAME_INSIDE_PAD, pady=eb.UI_FRAME_INSIDE_PAD)

        # Build
        self.vod_frame = ClipByBattleVodInfoFrame(self)
        self.clip_button = eb.build_button(self.frame, "Start", self._clip)
        self.battle_frame = ClipByBattleBattleInfoFrame(self)

        # Place
        self.vod_frame.get().grid(row=0, column=0, columnspan=3,
                                  padx=eb.UI_FRAME_OUTSIDE_PAD, pady=eb.UI_FRAME_OUTSIDE_PAD,
                                  sticky=W + E)
        self.clip_button.grid(row=1, column=0, columnspan=6, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y,
                              sticky='we')
        self.battle_frame.get().grid(row=2, column=0, columnspan=3,
                                     padx=eb.UI_FRAME_OUTSIDE_PAD, pady=eb.UI_FRAME_OUTSIDE_PAD,
                                     sticky=W + E)

        # Recording
        self.parent_object = parent_object
        pass

    def get(self):
        return self.frame

    def _clip(self):
        print("[{}] Clip".format(self.__class__.__name__))
        pass


class ClipByBattleVodInfoFrame:
    def __init__(self, parent_object):
        self.frame = LabelFrame(parent_object.get(),
                                text="VoD",
                                borderwidth=1,
                                padx=eb.UI_FRAME_INSIDE_PAD, pady=eb.UI_FRAME_INSIDE_PAD)
        row = 0
        # -- Date
        # Build
        self.date_label = eb.build_label(self.frame, "Date")
        self.date_entry = eb.build_entry(self.frame, 10)
        # Place
        self.date_label.grid(row=row, column=0, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y, sticky=W)
        self.date_entry.grid(row=row, column=1, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y, sticky=W)
        # Preset
        now = datetime.datetime.now()
        self.date_entry.insert(0, "{:04d}{:02d}{:02d}".format(now.year, now.month, now.day))
        # Finish
        row += 1

        # -- VoD id
        # Build
        self.id_label = eb.build_label(self.frame, "id")
        self.id_entry = eb.build_entry(self.frame, 10)
        # Place
        self.id_label.grid(row=row, column=0, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y, sticky=W)
        self.id_entry.grid(row=row, column=1, padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y, sticky=W)
        # Finish
        row += 1

        # -- Title
        # Build
        self.title_label = eb.build_label(self.frame, "Title")
        self.title_entry = eb.build_entry(self.frame, 86)
        # Place
        self.title_label.grid(row=row, column=0,
                              padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y,
                              sticky=W)
        self.title_entry.grid(row=row, column=1, columnspan=6,
                              padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y,
                              sticky=W)
        # Finish
        row += 1

        # Recording
        self.parent_object = parent_object
        pass

    def get(self):
        return self.frame
