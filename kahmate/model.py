import dataclasses
import enum
import random
from typing import Tuple

from kahmate.settings import *
import pygame as pg


class PlayerColor(enum.Enum):
    PINK = PINK_IMG
    BLUE = BLUE_IMG


class PieceType(enum.Enum):
    """
    The various possible types of a piece.
    [speed, attack_strength, defense_strength, name]
    """
    REGULAR = [3, 0, 0, 'regular']
    BIG = [2, 2, 1, 'big']
    TOUGH = [3, 1, 0, 'tough']
    FAST = [4, -1, 1, 'fast']
    SMART = [3, 0, 1, 'smart']

    def __getitem__(self, index):
        return self.value[index]


class Piece:
    """
    A piece is defined by :
    - its type
    - its position
    - if it has the ball or not
    - if it is down (cannot play) or not
    """
    def __init__(self,  piece_type: PieceType):
        self._piece_type = piece_type
        self.position = []
        self.has_ball = False
        self.is_down = False

    @ property
    def speed(self):
        return self._piece_type.value[0]

    @property
    def attack(self):
        return self._piece_type.value[1]

    @property
    def defense(self):
        return self._piece_type.value[2]

    @property
    def name(self):
        return self._piece_type.value[3]

    @property
    def piece_type(self):
        return self._piece_type

    def __str__(self):
        ans = "The " + self.piece_type.name + " piece is located at " + str(self.position)
        return ans


class Player:
    """
    A player is defined by:
    - the list of his pieces
    - the color of his team
    - his strength card deck
    """

    def __init__(self, color):
        self.pieces = [Piece(piece_type) for piece_type in PieceType]
        self.pieces.append(Piece(PieceType.REGULAR))
        self._color = color
        self._strength_deck = [i for i in range(1, 6)]

    @property
    def color(self):
        return self._color

    def draw(self, screen):
        for piece in self.pieces:
            if piece.piece_type == PieceType.REGULAR:
                screen.blit(self._color.value['REGULAR'], (piece.position[1]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2, piece.position[0]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2))
            elif piece.piece_type == PieceType.BIG:
                screen.blit(self._color.value['BIG'], (piece.position[1]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2, piece.position[0]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2))
            elif piece.piece_type == PieceType.FAST:
                screen.blit(self._color.value['FAST'], (piece.position[1]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2, piece.position[0]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2))
            elif piece.piece_type == PieceType.SMART:
                screen.blit(self._color.value['SMART'], (piece.position[1]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2, piece.position[0]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2))
            elif piece.piece_type == PieceType.TOUGH:
                screen.blit(self._color.value['TOUGH'], (piece.position[1]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2, piece.position[0]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2))
            if piece.is_down:
                screen.blit(self._color.value['RIP'], (piece.position[1]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2, piece.position[0]*GRIDWIDTH + (GRIDWIDTH-IMGSIZE)/2))

    def pick_strength(self):
        random.shuffle(self._strength_deck)
        picked = self._strength_deck.pop()
        if len(self._strength_deck) == 0:
            self._strength_deck = [i for i in range(1, 6)]
        return picked


class HumanPlayer(Player):
    """
    A human player is simply a player with a name, as a string.
    """

    def __init__(self, name: str, color):
        super().__init__(color)
        self._name = name
        self.init_positions()

    def init_positions(self):
        if self.color == PlayerColor.PINK:
            init_pos = PINK_POS
        else:
            init_pos = BLUE_POS
        i = 0
        for piece in self.pieces:
            piece.position = init_pos[i]
            i += 1

    def __str__(self):
        ans = "This is " + self._name + "'s Team : "
        for piece in self.pieces:
            ans += "\n" + str(piece)
        return ans


class Level(enum.Enum):
    """
    The various possible levels of an AI.
    """

    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"


class AIPlayer(Player):
    """
    An AI player is simply a player with a level (`Level` class).
    """

    def __init__(self, level: Level, color):
        super().__init__(color)
        self._level = level

    @property
    def level(self):
        return self._level

    def __str__(self):
        ans = "This is a" + str(self.level) + "AI's Team : "
        for piece in self.pieces:
            ans += "\n" + str(piece)
        return ans


class Board:
    def __init__(self):
        self.matrix = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self._selected_piece: None

    def draw_bgd(self, screen):
        screen.fill(DARK_GREEN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pg.draw.rect(screen, GREEN, (col*GRIDWIDTH, row*GRIDWIDTH, GRIDWIDTH, GRIDWIDTH))

    def draw(self, screen, players):
        self.draw_bgd(screen)
        for player in players:
            player.draw(screen)

    def update_board(self, players):
        self.matrix = [[None for _ in range(COLS)] for _ in range(ROWS)]
        for player in players:
            for piece in player.pieces:
                self.matrix[piece.position[0]][piece.position[1]] = piece

