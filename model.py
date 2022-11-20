import dataclasses
import enum
import random


class Color(enum.Enum):
    """
    The various possible colors of a team.
    """

    BLACK = "black"
    BLUE = "blue"
    GREEN = "green"
    RED = "red"
    WHITE = "white"
    YELLOW = "yellow"


class Piece:
    """
    A piece is defined by :
    - its ID
    - its strength
    - its number of cases during a movement
    - its position
    - if it has the ball or not
    """
    def __init__(self, strength, speed, position, ball):
        self._strength = strength
        self._speed = speed
        self._position = position
        self._ball = ball

    def position(self):
        return self._position

    def set_position(self, position, ball):
        self._position = position
        self._ball = ball

class Player:
    """
    A player is defined by:
    - the list of his pieces
    - the color of his team
    - his strength card deck
    """

    def __init__(self, pieces, color):
        self._pieces = pieces
        self._color = color
        self._strength_deck = [1, 2, 3, 4, 5, 6]

    @property
    def pieces(self):
        return self._pieces

    def get_positions(self):
        positions = []
        for p in self._pieces:
            positions.append(p.position())
        return positions

    def update_positions(self, pieceID, new_position, ball):
        self._pieces[pieceID].set_position(new_position, ball)

    def pick_strength(self):
        random.shuffle(self._strength_deck)
        return self._strength_deck.pop()

    # setters?


class HumanPlayer(Player):
    """
    A human player is simply a player with a name, as a string.
    """

    def __init__(self, name,  pieces, color):
        super().__init__(pieces, color)
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"{self._name} (human)"


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

    def __init__(self, level, pieces, color):
        super().__init__(pieces, color)
        self._level = level

    @property
    def level(self):
        return self._level

    def __str__(self):
        return f"{self._level.value} (AI)"

class Move:
    """
    The parent class of all possible moves.
    """

    def __init__(self):
        pass


class Movement(Move):
    """
    The move of drawing cards from the train card deck.
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Try"

    def play(self):
        pass


class Pass(Move):
    """
    The move of passing the ball to another piece.
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "pass"


class ForceWayThrough(Move):
    """
    The move of Forcing a piece's way through, defined by the two pieces
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "ForceWayThrough"


class Try(Move):
    """
    The move of Trying,
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Try"
