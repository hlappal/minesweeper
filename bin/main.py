import settings
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
        height=(settings.BOARD_HEIGHT-settings.FRAME_WIDTH)
    )
    left_frame.place(x=0, y=settings.FRAME_WIDTH)

    mine = Mine()
    print(f'x: {mine.x}, y: {mine.y}')

    # Run the window
    root.mainloop()


if __name__ == '__main__':
    main()
