import random
import settings


class Mine():
    def __init__(self):
        self.x = random.randint(0, settings.BOARD_WIDTH)
        self.y = random.randint(0, settings.BOARD_HEIGHT)
        self.frame = None
