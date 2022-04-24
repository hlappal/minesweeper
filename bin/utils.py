import settings
import random


def height_prct(percentage):
    return (settings.FIELD_HEIGHT / 100.0) * percentage

def width_prct(percentage):
    return (settings.FIELD_WIDTH / 100.0) * percentage
