import settings
import utils
import random
from tkinter import Tk, Frame, Button
from cell import Cell


def main():
    # Configure the window settings
    root = Tk()
    root.configure(bg=settings.FIELD_BG)
    root.geometry('500x300')
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.resizable(False, False)
    root.title('Minesweeper')

    top_frame = Frame(
        root,
        bg=settings.PANEL_BG,
        width=500,
        height=settings.PANEL_WIDTH
    )
    top_frame.place(x=0, y=0)

    #left_frame = Frame(
    #    root,
    #    bg=settings.PANEL_BG,
    #    width=settings.PANEL_WIDTH,
    #    height=(settings.FIELD_HEIGHT - settings.PANEL_WIDTH)
    #)
    #left_frame.place(x=0, y=settings.PANEL_WIDTH)

    center_frame = Frame(
        root,
        bg=settings.FIELD_BG,
        width=500,
        height=(300-settings.PANEL_WIDTH)
    )
    center_frame.grid(row=0, column=0, sticky='nesw')
    center_frame.place(x=0, y=settings.PANEL_WIDTH)

    for row in range(settings.GRID_HEIGHT):
        center_frame.grid_rowconfigure(row, weight=1)
        for col in range(settings.GRID_WIDTH):
            center_frame.grid_columnconfigure(col, weight=1)
            cell = Cell(row, col)
            cell.create_btn_obj(center_frame)
            cell.cell_btn_obj.grid(row=row, column=col, sticky='nesw')

    # Call the labels from the Cell class
    Cell.create_cell_count_label(top_frame)
    Cell.cell_count_label_obj.place(x=0, y=0)
    Cell.create_mine_count_label(top_frame)
    Cell.mine_count_label_obj.place(x=100, y=0)

    Cell.randomize_mines()

    # Run the window
    root.mainloop()


if __name__ == '__main__':
    main()
