#!/usr/bin/python

# Libs
import tkinter as tk
# Locals
from ui.clipbybattle.battle_list_frames import BattleListFrame
from ui.clipbybattle.vod_frames import VodInfoFrame


class ClipByBattleFrame(tk.LabelFrame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.vod_info = VodInfoFrame(self)
        self.battle_list = BattleListFrame(self)

        self.vod_info.pack(expand=True, fill='both')
        self.battle_list.pack(expand=True, fill='both')
        pass
