#!/usr/bin/python

# Libs
from tkinter import *
import uuid
# Locals
import ui.common.elements_builder as eb


class ClipByBattleBattleInfoFrame:
    _STARTING_BATTLE_INFO_ROW_NUMBER = 1
    titles = ["Id", "Tank", "Map", "Battle Tier", "Result Level", "Start Time", "End Time"]

    def __init__(self, parent_object):
        self.frame = LabelFrame(parent_object.get(),
                                text="Battles",
                                borderwidth=1,
                                padx=eb.UI_FRAME_INSIDE_PAD, pady=eb.UI_FRAME_INSIDE_PAD)

        # Build
        self.title_elements = self._build_title_row(self.frame)
        self.battle_rows = BattleInfoList(self, self._STARTING_BATTLE_INFO_ROW_NUMBER)
        self.add_battle_row_button = eb.build_button(self.frame, "  Add  ", self.add_battle_row)

        # Place
        self._render_title_row()
        self.battle_rows.render()
        self._render_add_button()

        # Recording
        self.parent_object = parent_object
        pass

    def get(self):
        return self.frame

    """
    ----------------------------------------------------------------
    Operations
    """

    def add_battle_row(self):
        # hide add button
        self._demount_add_button()
        # add new row
        self.battle_rows.add_row()
        # render add button again
        self._render_add_button()
        pass

    """
    ----------------------------------------------------------------
    Builds
    """

    def _build_title_row(self, parent):
        title_labels = []
        for title in self.titles:
            title_labels.append(eb.build_label(parent, title))
        return title_labels

    """
    ----------------------------------------------------------------
    Renderings
    """

    def _render_title_row(self):
        for i, element in enumerate(self.title_elements):
            element.grid(row=0, column=i,
                         padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y,
                         sticky=W)
        pass

    def _render_add_button(self):
        self.add_battle_row_button.grid(row=(self.battle_rows.size() + 1), column=0,
                                        padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y,
                                        sticky=W)

    def _demount_add_button(self):
        self.add_battle_row_button.grid_remove()

    """
    ----------------------------------------------------------------
    Utils
    """


class BattleInfoList(object):
    def __init__(self, parent_object, starting_row_number):
        # Recording
        self.parent_object = parent_object
        self.starting_row_number = starting_row_number
        # self.refresh_battle_row_callback = refresh_battle_row_callback

        # Builds
        self.rows = []
        self.add_row()
        pass

    def get(self):
        return self.parent_object.get()

    def add_row(self):
        # Create a new row
        new_row = BattleInfoRow(self,
                                (len(self.rows) + self.starting_row_number),
                                self.remove_row)
        # add to new list
        self.rows.append(new_row)
        # Render
        new_row.render()

    def remove_row(self):
        # remove disabled rows
        for row in self.rows:
            if not row.is_enabled():
                self.rows.remove(row)
        pass

    def render(self):
        for row in self.rows:
            row.render()

    def size(self):
        return len(self.rows)


class BattleInfoRow(object):
    def __init__(self, parent_object, _row, refresh_battle_row_callback):
        self.parent_object = parent_object
        self.id = self._create_row_id()
        self.row = _row
        self.enabled = True

        self.id_element = eb.build_label(parent_object.get(), self.id)
        self.tank_element = eb.build_entry(parent_object.get(), 8)
        self.map_element = eb.build_entry(parent_object.get(), 8)
        self.tier_element = eb.build_entry(parent_object.get(), 2)
        self.result_level_element = eb.build_entry(parent_object.get(), 2)
        self.start_time_element = eb.build_entry(parent_object.get(), 10)
        self.end_time_element = eb.build_entry(parent_object.get(), 10)
        self.remove_button_element = eb.build_button(parent_object.get(), "-",
                                                     lambda: self.destroy(refresh_battle_row_callback))

        self.elements = [
            self.id_element,
            self.tank_element,
            self.map_element,
            self.tier_element,
            self.result_level_element,
            self.start_time_element,
            self.end_time_element,
            self.remove_button_element
        ]

    def render(self, new_row=None):
        if new_row:
            self.row = new_row

        for column, element in enumerate(self.elements):
            element.grid(row=self.row, column=column,
                         padx=eb.UI_ELEMENT_PAD_X, pady=eb.UI_ELEMENT_PAD_Y,
                         sticky=W)

    def destroy(self, refresh_battle_row_callback):
        # demount all elements and destroy
        for element in self.elements:
            element.grid_remove()
            element.destroy()

        self.enabled = False

        refresh_battle_row_callback()
        pass

    def is_enabled(self):
        return self.enabled

    @staticmethod
    def _create_row_id():
        return str(uuid.uuid4())[-8:]

