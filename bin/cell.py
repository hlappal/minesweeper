from tkinter import Button
import settings
import random


class Cell:
    all = []

    def __init__(self, x: int, y: int, is_mine=False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_obj = None

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_obj(self, location: object):
        btn = Button(
            location,
            width=3,
            height=3,
            #text=f"{self.x}, {self.y}"
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_obj = btn

    def left_click_action(self, event):
        print(self.is_mine)

    def right_click_action(self, event):
        print(self.is_mine)

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.N_MINES)
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
