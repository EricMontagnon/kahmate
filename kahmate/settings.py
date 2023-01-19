import enum
from pathlib import Path
import pygame as pg

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (104, 207, 81)
PINK = (234, 163, 172)
BLUE = (123, 230, 222)
DARK_GREEN = (52, 148, 31)
LIGHT_GREEN = (221, 255, 190)
VERY_LIGHT_GREEN = (250, 255, 218)
RED = (220, 20, 60)
LIGHT_RED = (255, 95, 107)

# window settings
GRIDWIDTH = 70
PIECESIZE = 64
CARDSIZE = (100, 140)
DECKSIZE = 140
ARROWSIZE = (20, 20)
ROWS = 8
ROWSAUX = 1
COLS = 11
COLSAUX = 4
WIDTH = (COLS + 2 * COLSAUX) * GRIDWIDTH
HEIGHT = (ROWS + 2 * ROWSAUX) * GRIDWIDTH
TITLE = "KAHMATE"
FPS = 60

SETTINGS_PATH = Path(__file__).absolute()
PARENT_PATH = SETTINGS_PATH.parent.parent
IMG_PATH = PARENT_PATH / "img/"

# pieces img
BALL = pg.transform.scale(pg.image.load(IMG_PATH / 'ball.png'), (32, 32))
LIGHTNING = pg.transform.scale(pg.image.load(IMG_PATH / 'lightning.png'), (32, 32))

# initial positions, change later
BLUE_POS = [[2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4]]
PINK_POS = [[2, 14], [3, 14], [4, 14], [5, 14], [6, 14], [7, 14]]

def create_text(text, font, size, color, is_bold):
    font = pg.font.SysFont(font, size, bold=is_bold)
    image = font.render(text, True, color)
    return image

class Fonts(enum.Enum):

    TITLE = 'Verdana'
    SUBTITLE = 'Lucida Console'


class TextSize(enum.Enum):
    TITLE = 30
    SUBTITLE = 25
    REGULAR = 14

