from tkinter import Button, Label
import settings
import random


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_obj = None
    mine_count = settings.N_MINES
    mine_count_label_obj = None
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

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells left: {Cell.cell_count}",
            width=12,
            height=2,
            bg=settings.PANEL_BG,
            #font=('', 24)
        )
        Cell.cell_count_label_obj = lbl

    @staticmethod
    def create_mine_count_label(location):
        lbl = Label(
            location,
            text=f"Mines left: {Cell.mine_count}",
            width=12,
            height=2,
            bg=settings.PANEL_BG,
        )
        Cell.mine_count_label_obj = lbl

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
        Cell.cell_count -= 1
        self.cell_btn_obj.configure(text=self.neighboring_mines)
        # Update cell count label
        if Cell.cell_count_label_obj:
            Cell.cell_count_label_obj.configure(
                text=f"Cells left: {Cell.cell_count}"
            )

    def show_mine(self):
        Cell.mine_count -= 1
        self.cell_btn_obj.configure(bg='red')
        # Update mine count label
        if Cell.mine_count_label_obj:
            Cell.mine_count_label_obj.configure(
                text=f"Mines left: {Cell.mine_count}"
            )

    def right_click_action(self, event):
        pass

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.N_MINES)
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
