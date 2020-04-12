#!/usr/bin/python

# Libs
import tkinter as tk
import uuid
# Locals
import ui.common.elements_builder as eb
from common.wot_vod_elements import MasteryBadge, Tier
from ui.clipbybattle.elements import TimeStampFrame


class BattleRowListFrame(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # Parameters
        self.rows = []
        self.add_row()
        pass

    def add_row(self):
        # Get last row
        last_row = self.rows[-1] if self.size() > 0 else None

        # Create a new row
        new_row = BattleRowFrame(self, self.refresh_list)
        # Render
        new_row.pack(expand=True, fill='both')
        # add to new list
        self.rows.append(new_row)

        # Fill in values from last row
        # Both time use last end time
        new_row.copy(last_row)
        pass

    def refresh_list(self):
        for row in self.rows:
            if not row.is_enabled():
                self.rows.remove(row)
        pass

    def size(self):
        return len(self.rows)


class BattleRowFrame(tk.Frame):
    def __init__(self, master, refresh_battle_list_callback, **kw):
        super().__init__(master, **kw)

        # Set self parameters
        self.enabled = True
        self.refresh_battle_list_callback = refresh_battle_list_callback

        # Vars for UI elements
        self.battle_tier_var = tk.IntVar()
        self.battle_tier_var.set(Tier.Ten.value)
        self.mastery_badge_var = tk.StringVar()
        self.mastery_badge_var.set(MasteryBadge.First.value)
        # Create child elements
        self.tank_element = tk.Entry(self, width=10)
        self.map_element = tk.Entry(self, width=10)
        self.tier_element = tk.OptionMenu(self, self.battle_tier_var, *Tier.values())
        self.mastery_badge_element = tk.OptionMenu(self, self.mastery_badge_var, *MasteryBadge.values())
        self.start_time_element = TimeStampFrame(self)
        self.end_time_element = TimeStampFrame(self)
        self.remove_button_element = tk.Button(self, text="-", command=lambda: self.clear(), width=3)
        # Additional configurations
        self.tier_element.configure(width=5)
        self.mastery_badge_element.configure(width=11)
        # Put in group
        self.elements = [
            self.tank_element,
            self.map_element,
            self.tier_element,
            self.mastery_badge_element,
            self.start_time_element,
            self.end_time_element,
            self.remove_button_element
        ]

        # Render inside self frame
        for i, element in enumerate(self.elements):
            element.grid(row=0, column=i,
                         sticky="ew",
                         padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y)

        pass

    def clear(self):
        # Disable self
        self.enabled = False

        # demount all elements and destroy
        for element in self.elements:
            element.grid_remove()
            element.destroy()

        # Call callback to refresh and remove itself from battle list
        self.refresh_battle_list_callback()

        # Clear self
        self.grid_remove()
        self.destroy()
        pass

    def is_enabled(self):
        return self.enabled

    @staticmethod
    def _create_row_id():
        return str(uuid.uuid4())[-8:]

    def copy(self, old_row):
        if old_row:
            self.tank_element.insert(0, old_row.tank_element.get())
            self.map_element.insert(0, old_row.map_element.get())
            self.battle_tier_var.set(old_row.battle_tier_var.get())
            self.mastery_badge_var.set(old_row.mastery_badge_var.get())
            self.start_time_element.copy(old_row.end_time_element)
            self.end_time_element.copy(old_row.end_time_element)
        pass
