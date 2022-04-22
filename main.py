from tkinter import Tk, Frame


def main():
    # Configure the window settings
    root = Tk()
    root.configure(bg="#afafaf")
    root.geometry('980x640')
    root.resizable(False, False)
    root.title('Minesweeper')

    top_frame = Frame(
        root,
        bg="#a0a0a0",
        width=980,
        height=30
    )
    top_frame.place(x=0, y=0)

    # Run the window
    root.mainloop()


if __name__ == '__main__':
    main()
