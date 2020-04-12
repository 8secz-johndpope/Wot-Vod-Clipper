#!/usr/bin/python

# Libs
import tkinter as tk
import uuid
# Locals
import ui.common.elements_builder as eb
from ui.clipbybattle.battle_list_frames import BattleRowListFrame
from ui.common.clip_button_frame import ClipButtonFrame


class TitleLabel(object):
    def __init__(self, text, index: int, width: int):
        self.text = text
        self.index = index
        self.width = width
        pass


class ClipByBattleTitleFrame(tk.Frame):
    __titles = [
        TitleLabel("Tank", 1, 8),
        TitleLabel("Map", 2, 9),
        TitleLabel("Battle Tier", 3, 10),
        TitleLabel("Mastery Badge", 4, 14),
        TitleLabel("StartTime", 5, 16),
        TitleLabel("EndTime", 6, 16)
    ]

    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # Create labels and render
        for title in self.__titles:
            element = tk.Label(self, text=title.text, width=title.width, bg="pink")
            element.grid(row=0, column=title.index,
                         padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y,
                         sticky='w')
        pass


class ClipByBattleFrame(tk.LabelFrame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.title_frame = ClipByBattleTitleFrame(self)
        self.battle_list_frame = BattleRowListFrame(self)
        self.add_button_frame = ClipButtonFrame(self, "Add", self.battle_list_frame.add_row)

        self.title_frame.pack(expand=True, fill='both')
        self.battle_list_frame.pack(expand=True, fill='both')
        self.add_button_frame.pack(expand=True, fill='both')

        pass
