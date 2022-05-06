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
            height=2,
            #text=f"{self.x}, {self.y}"
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_obj = btn

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.neighboring_mines == 0:
                for cell in self.neighboring_cells:
                    cell.show_cell()
            self.show_cell()

    def get_cell_by_axis(self, x: int, y: int) -> object:
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def neighboring_cells(self) -> list:
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]
        return [cell for cell in cells if cell]

    @property
    def neighboring_mines(self) -> int:
        count = 0
        for cell in self.neighboring_cells:
            if cell.is_mine:
                count += 1
        return count

    def show_cell(self):
        self.cell_btn_obj.configure(text=self.neighboring_mines)

    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')

    def right_click_action(self, event):
        pass

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.N_MINES)
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
