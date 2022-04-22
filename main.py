from tkinter import Tk, Frame
import random


BOARD_WIDTH = 980
BOARD_HEIGHT = 640
PANEL_WIDTH = 80


class Mine():
    def __init__(self):
        self.x = random.randint(0, BOARD_WIDTH)
        self.y = random.randint(PANEL_WIDTH, BOARD_HEIGHT)


def main():
    # Configure the window settings
    root = Tk()
    root.configure(bg="#afafaf")
    root.geometry(f'{BOARD_WIDTH}x{BOARD_HEIGHT}')
    root.resizable(False, False)
    root.title('Minesweeper')

    top_frame = Frame(
        root,
        bg="#a0a0a0",
        width=BOARD_WIDTH,
        height=PANEL_WIDTH
    )
    top_frame.place(x=0, y=0)

    left_frame = Frame(
        root,
        bg="#a0a0a0",
        width = PANEL_WIDTH,
        height = BOARD_HEIGHT - PANEL_WIDTH
    )
    left_frame.place(x=0, y=PANEL_WIDTH)

    mine = Mine()
    print(f'x: {mine.x}, y: {mine.y}')

    # Run the window
    root.mainloop()


if __name__ == '__main__':
    main()
