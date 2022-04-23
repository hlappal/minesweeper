import settings
import random
from mine import Mine


def height_prct(percentage):
    return (settings.BOARD_HEIGHT / 100.0) * percentage

def width_prct(percentage):
    return (settings.BOARD_WIDTH / 100.0) * percentage

def init_mines():
    mines = []
    coords = []
    random.seed(42)  # TODO: Delete
    for i in range(settings.N_MINES):
        coords.append([random.randint(settings.FRAME_WIDTH, settings.BOARD_WIDTH),
                       random.randint(settings.FRAME_WIDTH, settings.BOARD_HEIGHT)])

    duplicates = True
    while duplicates:
        duplicates = False
        for i in range(len(coords) - 1):
            for j in range(i + 1, len(coords)):
                if coords[i] == coords[j]:
                    duplicates = True
                    print('Duplicates found')
                    break
            if duplicates:
                coords[i] = [
                    random.randint(settings.FRAME_WIDTH, settings.BOARD_WIDTH),
                    random.randint(settings.FRAME_WIDTH, settings.BOARD_HEIGHT)]
                break

    for c in coords:
        mine = Mine()
        mine.x = c[0]
        mine.y = c[1]
        mines.append(mine)

    return mines
