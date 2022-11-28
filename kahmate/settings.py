import pygame as pg

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (104, 207, 81)
DARK_GREEN = (52, 148, 31)

# window settings
GRIDWIDTH = 72
IMGSIZE = 64
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
    'BIG': pg.transform.scale(pg.image.load('img/big_pink.png'), (IMGSIZE, IMGSIZE)),
    'FAST': pg.transform.scale(pg.image.load('img/fast_pink.png'), (IMGSIZE, IMGSIZE)),
    'REGULAR': pg.transform.scale(pg.image.load('img/regular_pink.png'), (IMGSIZE, IMGSIZE)),
    'SMART': pg.transform.scale(pg.image.load('img/smart_pink.png'), (IMGSIZE, IMGSIZE)),
    'TOUGH': pg.transform.scale(pg.image.load('img/tough_pink.png'), (IMGSIZE, IMGSIZE)),
    'RIP': pg.transform.scale(pg.image.load('img/rip_pink.png'), (IMGSIZE, IMGSIZE))
}

BLUE_IMG = {
    'BIG': pg.transform.scale(pg.image.load('img/big_blue.png'), (IMGSIZE, IMGSIZE)),
    'FAST': pg.transform.scale(pg.image.load('img/fast_blue.png'), (IMGSIZE, IMGSIZE)),
    'REGULAR': pg.transform.scale(pg.image.load('img/regular_blue.png'), (IMGSIZE, IMGSIZE)),
    'SMART': pg.transform.scale(pg.image.load('img/smart_blue.png'), (IMGSIZE, IMGSIZE)),
    'TOUGH': pg.transform.scale(pg.image.load('img/tough_blue.png'), (IMGSIZE, IMGSIZE)),
    'RIP': pg.transform.scale(pg.image.load('img/rip_blue.png'), (IMGSIZE, IMGSIZE))
}

# initial positions

PINK_POS = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
BLUE_POS = [[0, 10], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10]]
