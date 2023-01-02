from pathlib import Path

import pygame as pg
import os

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
BALL = pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'ball.png')), (32, 32))
LIGHTNING = pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'lightning.png')), (32, 32))

PINK_IMG = {
    'BIG': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'big_pink.png')), (PIECESIZE, PIECESIZE)),
    'FAST': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'fast_pink.png')), (PIECESIZE, PIECESIZE)),
    'REGULAR': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'regular_pink.png')), (PIECESIZE, PIECESIZE)),
    'SMART': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'smart_pink.png')), (PIECESIZE, PIECESIZE)),
    'TOUGH': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'tough_pink.png')), (PIECESIZE, PIECESIZE)),
    'RIP': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'rip_pink.png')), (PIECESIZE, PIECESIZE))
}

BLUE_IMG = {
    'BIG': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'big_blue.png')), (PIECESIZE, PIECESIZE)),
    'FAST': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'fast_blue.png')), (PIECESIZE, PIECESIZE)),
    'REGULAR': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'regular_blue.png')), (PIECESIZE, PIECESIZE)),
    'SMART': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'smart_blue.png')), (PIECESIZE, PIECESIZE)),
    'TOUGH': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'tough_blue.png')), (PIECESIZE, PIECESIZE)),
    'RIP': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'rip_blue.png')), (PIECESIZE, PIECESIZE))
}

# initial positions

BLUE_POS = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
PINK_POS = [[0, 10], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10]]


# strength cards

PINK_CARDS = {
    '1': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_pink_1.png')), CARDSIZE),
    '2': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_pink_2.png')), CARDSIZE),
    '3': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_pink_3.png')), CARDSIZE),
    '4': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_pink_4.png')), CARDSIZE),
    '5': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_pink_5.png')), CARDSIZE),
    '6': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_pink_6.png')), CARDSIZE)
}

BLUE_CARDS = {
    '1': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_blue_1.png')), CARDSIZE),
    '2': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_blue_2.png')), CARDSIZE),
    '3': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_blue_3.png')), CARDSIZE),
    '4': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_blue_4.png')), CARDSIZE),
    '5': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_blue_5.png')), CARDSIZE),
    '6': pg.transform.scale(pg.image.load(os.path.join(IMG_PATH, 'card_blue_6.png')), CARDSIZE)
}