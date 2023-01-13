import dataclasses
import enum
import random
from typing import Optional
from kahmate.settings import *
import pygame as pg


class Color(enum.Enum):
    PINK = 'pink'
    BLUE = 'blue'


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
        self.turn_death = -1
        self.has_moved = False

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

    def screen_position(self):
        x = self.position[1] * GRIDWIDTH + (GRIDWIDTH - PIECESIZE) / 2
        y = self.position[0] * GRIDWIDTH + (GRIDWIDTH - PIECESIZE) / 2
        return x, y

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
        self.strength_deck = [i for i in range(1, 6)]
        self.pieces_img = {}
        for piece in self.pieces:
            path = piece.name + '_' + self._color.value + '.png'
            self.pieces_img[piece.name] = pg.transform.scale(pg.image.load(IMG_PATH / path), (PIECESIZE, PIECESIZE))
        path = 'rip_' + self._color.value + '.png'
        self.pieces_img['rip'] = pg.transform.scale(pg.image.load(IMG_PATH / path), (PIECESIZE, PIECESIZE))
        self.strength_deck_img = {}
        for i in range(1, 6):
            path = 'card_' + self._color.value + '_' + str(i) + '.png'
            self.strength_deck_img[i] = pg.transform.scale(pg.image.load(IMG_PATH / path), CARDSIZE)

    @property
    def color(self):
        return self.color

    def draw(self, screen):
        for piece in self.pieces:
            screen.blit(self.pieces_img[piece.name], piece.screen_position())
            if piece.is_down:
                screen.blit(self.pieces_img['rip'], (piece.screen_position()))

    def pick_strength(self):
        random.shuffle(self.strength_deck)
        picked = self.strength_deck.pop()
        if len(self.strength_deck) == 0:
            self.strength_deck = [i for i in range(1, 6)]
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
        if self._color == Color.PINK:
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
        self.matrix = [[None for _ in range(COLS+2*COLSAUX)] for _ in range(ROWS + 2*ROWSAUX)]
        self._selected_piece: None

    def draw_bgd(self, screen):
        screen.fill(BLACK)
        pg.draw.rect(screen, DARK_GREEN, (COLSAUX*GRIDWIDTH, ROWSAUX*GRIDWIDTH, COLS*GRIDWIDTH, ROWS*GRIDWIDTH))
        deck = pg.transform.scale(pg.image.load(IMG_PATH / 'deck.png'), (118, 140))
        screen.blit(deck, (COLSAUX*GRIDWIDTH/2 - 118/2, (ROWSAUX+1)*GRIDWIDTH))
        screen.blit(deck, ((COLSAUX + COLS)*GRIDWIDTH + COLSAUX*GRIDWIDTH/2 - 118/2, (ROWSAUX+1) * GRIDWIDTH))
        for row in range(ROWSAUX, ROWS + ROWSAUX):
            for col in range(row % 2 + COLSAUX, COLS + COLSAUX, 2):
                pg.draw.rect(screen, GREEN, (col*GRIDWIDTH, row*GRIDWIDTH, GRIDWIDTH, GRIDWIDTH))

    def draw(self, screen, players, ball_position, valid_moves):
        self.draw_bgd(screen)
        for move in valid_moves:
            move.draw(screen)
        for player in players:
            player.draw(screen)
        screen.blit(BALL, (ball_position[1] * GRIDWIDTH, ball_position[0] * GRIDWIDTH))

    def update_board(self, players):
        self.matrix = [[None for _ in range(COLS + 2*COLSAUX)] for _ in range(ROWS + 2*ROWSAUX)]
        for player in players:
            for piece in player.pieces:
                self.matrix[piece.position[0]][piece.position[1]] = piece

    def check_click(self):
        pass


class Move:
    """
    The parent class of all possible moves.
    """

    def __init__(self, piece: Piece, second_position : [int, int]):
        self.piece = piece
        self.second_position = second_position
        pass


class Displacement(Move):
    """
    The move of drawing cards from the train card deck.
    """
    def __init__(self, piece: Piece, new_position: [int, int], face_off_opponent: Optional[Piece]):
        super().__init__(piece, new_position)
        self.face_off_opponent = face_off_opponent

    def play(self, game):
        """
        input : move : model.Displacement = Displacement chosen to be played
        action : if no face off -> the piece is moved to new position
            if face off -> face off, pieces displaced of put down according to the result, next_player updated
        """
        if self.face_off_opponent is None:
            self.piece.position = self.second_position
            if self.piece.has_ball:
                game.ball_position = self.second_position
        else:
            result_face_off = game.face_off(self.piece, self.face_off_opponent)
            print(result_face_off)
            if result_face_off == "Defense wins!":
                position = self.piece.position
                if self.piece.has_ball:
                    self.piece.has_ball = False
                    if game.next_player()._color == Color.PINK:
                        game.ball_position = [position[0], position[1] + 1]
                    else:
                        game.ball_position = [position[0], position[1] - 1]
                self.piece.is_down = True
                self.piece.turn_death = game.turn_count
            else:
                self.piece.position = self.second_position
                if self.piece.has_ball:
                    game.ball_position = self.second_position
                self.face_off_opponent.is_down = True
                self.face_off_opponent.turn_death = game.turn_count
        game.board.update_board(game.players)
        self.piece.has_moved = True
        if game.turn_count % 2 == 1:
            for piece in game.next_player().pieces:
                piece.has_moved = False
        game.turn_count += 1
        game._next_player = (game.turn_count // 2) % 2

    def draw(self, screen):
        list_cols = [VERY_LIGHT_GREEN, LIGHT_GREEN]
        list_reds = [LIGHT_RED, RED]
        x = self.second_position[1]
        y = self.second_position[0]
        if self.face_off_opponent:
            pg.draw.rect(screen, list_reds[(x + y) % 2], (x * GRIDWIDTH, y * GRIDWIDTH, GRIDWIDTH, GRIDWIDTH))
        else:
            pg.draw.rect(screen, list_cols[(x+y) % 2], (x * GRIDWIDTH, y * GRIDWIDTH, GRIDWIDTH, GRIDWIDTH))


    def __str__(self):
        return "Displacement of the piece " + str(self.piece.name) + " to the position : " + str(self.second_position)

class Pass(Move):
    """
    The move of passing the ball to another piece.
    """

    def __init__(self, piece: Piece, new_piece: Piece, face_off_opponent: Optional[Piece]):
        super().__init__(piece, new_piece.position)
        self.new_piece = new_piece
        self.face_off_opponent = face_off_opponent

    def play(self, game):
        """
        input : move : model.Pass = Pass chosen to be played
        action : if no face off -> the ball changes player
            if face off -> to be implemented
        """
        game.ball_position = self.new_piece.position
        self.piece.has_ball = False
        self.new_piece.has_ball = True
        game.board.update_board(game.players)

    def draw(self, screen):
        screen.blit(BALL, (self.second_position[1] * GRIDWIDTH, self.second_position[0] * GRIDWIDTH))

    def __str__(self):
        return "Pass from piece " + str(self.piece.name) + " to piece " + str(self.new_piece.name)


class Tackle(Move):
    """
    The move of Forcing a piece's way through, defined by the two pieces
    """

    def __init__(self, piece: Piece, opponent: Piece):
        super().__init__(piece, opponent.position)
        self.piece = piece
        self.opponent = opponent

    def play(self, game):
        """
        input : move : model.Pass = Pass chosen to be played
        action : if no face off -> the ball changes player
            if face off -> to be implemented
        """
        result_face_off = game.face_off(self.piece, self.opponent)
        print(result_face_off)
        if result_face_off == "Defense wins!":
            self.piece.is_down = True
            self.piece.turn_death = game.turn_count
        if result_face_off == "Plaquage parfait!":
            self.opponent.has_ball = False
            self.opponent.is_down = True
            self.opponent.turn_death = game.turn_count
            self.piece.has_ball = True
            game.ball_position = self.piece.position
        if result_face_off == "Attack wins!":
            self.opponent.has_ball = False
            self.opponent.is_down = True
            self.opponent.turn_death = game.turn_count
            position = self.opponent.position
            if game.players[(game._next_player + 1) % 2]._color == Color.PINK:
                game.ball_position = [position[0], position[1] + 1]
            else:
                game.ball_position = [position[0], position[1] - 1]
        game.board.update_board(game.players)
        if game.turn_count % 2 == 1:
            for piece in game.next_player().pieces:
                piece.has_moved = False
        game.turn_count += 1
        game._next_player = (game.turn_count // 2) % 2

    def draw(self, screen):
        pg.draw.rect(screen, RED, (self.second_position[1] * GRIDWIDTH, self.second_position[0] * GRIDWIDTH, GRIDWIDTH, GRIDWIDTH))

    def __str__(self):
        return "Tackle"