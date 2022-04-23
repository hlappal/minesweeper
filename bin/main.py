import settings
import utils
import random
from tkinter import Tk, Frame
from mine import Mine


def main():
    # Configure the window settings
    root = Tk()
    root.configure(bg=settings.BOARD_BG)
    root.geometry(f'{settings.BOARD_WIDTH}x{settings.BOARD_HEIGHT}')
    root.resizable(False, False)
    root.title('Minesweeper')

    top_frame = Frame(
        root,
        bg=settings.FRAME_BG,
        width=settings.BOARD_WIDTH,
        height=settings.FRAME_WIDTH
    )
    top_frame.place(x=0, y=0)

    left_frame = Frame(
        root,
        bg=settings.FRAME_BG,
        width=settings.FRAME_WIDTH,
        height=(settings.BOARD_HEIGHT - settings.FRAME_WIDTH)
    )
    left_frame.place(x=0, y=settings.FRAME_WIDTH)

    center_frame = Frame(
        root,
        bg=settings.BOARD_BG,
        width=(settings.BOARD_WIDTH - settings.FRAME_WIDTH),
        height=(settings.BOARD_HEIGHT - settings.FRAME_WIDTH)
    )
    center_frame.place(x=settings.FRAME_WIDTH, y=settings.FRAME_WIDTH)

    mines = utils.init_mines()
    for mine in mines:
        mine.frame = Frame(
            root,
            bg=settings.MINE_BG,
            width=(settings.MINE_SIZE - 2),
            height=(settings.MINE_SIZE - 2)
        )
        mine.frame.place(x=mine.x, y=mine.y)

    # Run the window
    root.mainloop()


if __name__ == '__main__':
    main()
