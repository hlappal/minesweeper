import random
import settings


class Mine():
    def __init__(self):
        self.x = random.randint(0, settings.BOARD_WIDTH)
        self.y = random.randint(int(settings.FRAME_WIDTH), settings.BOARD_HEIGHT)
