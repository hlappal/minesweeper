from tkinter import Button
import settings


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None

    def create_btn_obj(self, location):
        btn = Button(
            location,
            # width=settings.CELL_SIZE,
            # height=settings.CELL_SIZE
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_obj = btn

    def left_click_action(self, event):
        print(event)

    def right_click_action(self, event):
        print(event)
