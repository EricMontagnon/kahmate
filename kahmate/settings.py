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
GRIDWIDTH = 72
PIECESIZE = 64
CARDSIZE = (100, 140)
ROWS = 8
COLS = 11
WIDTH = COLS*GRIDWIDTH
HEIGHT = ROWS*GRIDWIDTH
TITLE = "KAHMATE"
FPS = 60

SETTINGS_PATH = Path(__file__).absolute()
PARENT_PATH = SETTINGS_PATH.parent.parent
IMG_PATH = PARENT_PATH / "img/"

# pieces img
BALL = pg.transform.scale(pg.image.load(IMG_PATH / 'ball.png'), (32, 32))
LIGHTNING = pg.transform.scale(pg.image.load(IMG_PATH / 'lightning.png'), (32, 32))


# initial positions, change later
BLUE_POS = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
PINK_POS = [[0, 10], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10]]

