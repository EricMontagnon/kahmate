from pathlib import Path
import pygame as pg

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (104, 207, 81)
DARK_GREEN = (52, 148, 31)
LIGHT_GREEN = (221, 255, 190)
VERY_LIGHT_GREEN = (250, 255, 218)
RED = (220, 20, 60)
LIGHT_RED = (255, 95, 107)

# window settings
GRIDWIDTH = 70
PIECESIZE = 64
CARDSIZE = (100, 140)
ROWS = 8
ROWSAUX = 1
COLS = 11
COLSAUX = 3
WIDTH = (COLS + 2*COLSAUX)*GRIDWIDTH
HEIGHT = (ROWS + 2*ROWSAUX)*GRIDWIDTH
TITLE = "KAHMATE"
FPS = 60

SETTINGS_PATH = Path(__file__).absolute()
PARENT_PATH = SETTINGS_PATH.parent.parent
IMG_PATH = PARENT_PATH / "img/"

# pieces img
BALL = pg.transform.scale(pg.image.load(IMG_PATH / 'ball.png'), (32, 32))
LIGHTNING = pg.transform.scale(pg.image.load(IMG_PATH / 'lightning.png'), (32, 32))


# initial positions, change later
BLUE_POS = [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3]]
PINK_POS = [[1, 13], [2, 13], [3, 13], [4, 13], [5, 13], [6, 13]]

