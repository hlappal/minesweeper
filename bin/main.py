import settings
import utils
import random
from tkinter import Tk, Frame, Button
from cell import Cell


def main():
    # Configure the window settings
    root = Tk()
    root.configure(bg=settings.FIELD_BG)
    root.geometry(f"{settings.FIELD_WIDTH}x{settings.FIELD_HEIGHT}")
    root.resizable(False, False)
    root.title('Minesweeper')

    #top_frame = Frame(
    #    root,
    #    bg=settings.PANEL_BG,
    #    width=settings.FIELD_WIDTH,
    #    height=settings.PANEL_WIDTH
    #)
    #top_frame.place(x=0, y=0)

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
        width=settings.FIELD_WIDTH,
        height=settings.FIELD_HEIGHT
    )
    center_frame.place(x=0, y=0) #settings.PANEL_WIDTH)

    for i in range(settings.GRID_HEIGHT):
        for j in range(settings.GRID_WIDTH):
            cell = Cell(i, j)
            cell.create_btn_obj(center_frame)
            cell.cell_btn_obj.grid(row=i, column=j)

    Cell.randomize_mines()

    # Run the window
    root.mainloop()


if __name__ == '__main__':
    main()
