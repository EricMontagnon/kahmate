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

# pieces img
BALL = pg.transform.scale(pg.image.load('img/ball.png'), (32, 32))
LIGHTNING = pg.transform.scale(pg.image.load('img/lightning.png'), (32, 32))

PINK_IMG = {
    'BIG': pg.transform.scale(pg.image.load('img/big_pink.png'), (PIECESIZE, PIECESIZE)),
    'FAST': pg.transform.scale(pg.image.load('img/fast_pink.png'), (PIECESIZE, PIECESIZE)),
    'REGULAR': pg.transform.scale(pg.image.load('img/regular_pink.png'), (PIECESIZE, PIECESIZE)),
    'SMART': pg.transform.scale(pg.image.load('img/smart_pink.png'), (PIECESIZE, PIECESIZE)),
    'TOUGH': pg.transform.scale(pg.image.load('img/tough_pink.png'), (PIECESIZE, PIECESIZE)),
    'RIP': pg.transform.scale(pg.image.load('img/rip_pink.png'), (PIECESIZE, PIECESIZE))
}

BLUE_IMG = {
    'BIG': pg.transform.scale(pg.image.load('img/big_blue.png'), (PIECESIZE, PIECESIZE)),
    'FAST': pg.transform.scale(pg.image.load('img/fast_blue.png'), (PIECESIZE, PIECESIZE)),
    'REGULAR': pg.transform.scale(pg.image.load('img/regular_blue.png'), (PIECESIZE, PIECESIZE)),
    'SMART': pg.transform.scale(pg.image.load('img/smart_blue.png'), (PIECESIZE, PIECESIZE)),
    'TOUGH': pg.transform.scale(pg.image.load('img/tough_blue.png'), (PIECESIZE, PIECESIZE)),
    'RIP': pg.transform.scale(pg.image.load('img/rip_blue.png'), (PIECESIZE, PIECESIZE))
}

# path.itrdir()

# initial positions

BLUE_POS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
PINK_POS = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]


# strength cards

PINK_CARDS = {
    '1': pg.transform.scale(pg.image.load('img/card_pink_1.png'), CARDSIZE),
    '2': pg.transform.scale(pg.image.load('img/card_pink_2.png'), CARDSIZE),
    '3': pg.transform.scale(pg.image.load('img/card_pink_3.png'), CARDSIZE),
    '4': pg.transform.scale(pg.image.load('img/card_pink_4.png'), CARDSIZE),
    '5': pg.transform.scale(pg.image.load('img/card_pink_5.png'), CARDSIZE),
    '6': pg.transform.scale(pg.image.load('img/card_pink_6.png'), CARDSIZE)
}

BLUE_CARDS = {
    '1': pg.transform.scale(pg.image.load('img/card_blue_1.png'), CARDSIZE),
    '2': pg.transform.scale(pg.image.load('img/card_blue_2.png'), CARDSIZE),
    '3': pg.transform.scale(pg.image.load('img/card_blue_3.png'), CARDSIZE),
    '4': pg.transform.scale(pg.image.load('img/card_blue_4.png'), CARDSIZE),
    '5': pg.transform.scale(pg.image.load('img/card_blue_5.png'), CARDSIZE),
    '6': pg.transform.scale(pg.image.load('img/card_blue_6.png'), CARDSIZE)
}
