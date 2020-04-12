#!/usr/bin/python

# Libs
import tkinter as tk
# Locals
from ui.clipbybattle.frames import ClipByBattleFrame


if __name__ == '__main__':
    tk = tk.Tk()
    element = ClipByBattleFrame(tk)
    element.pack(expand=True, fill='both')
    tk.mainloop()
    pass
