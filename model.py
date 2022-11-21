import dataclasses
import enum
import random


class PieceType(enum.Enum):
    """
    The various possible types of a piece.
    [speed, attack_strength, defense_strength]
    """

    REGULAR = [3, 0, 0]
    BIG = [2, 2, 1]
    TOUGH = [3, 1, 0]
    FAST = [4, -1, 1]
    SMART = [3, 0, 1]


class Piece:
    """
    A piece is defined by :
    - its ID
    - its strength
    - its number of cases during a movement
    - its position
    - if it has the ball or not
    """
    def __init__(self, piece_type: PieceType, position: [int, int], ball: bool, is_down: bool):
        self._piece_type = piece_type
        self._position = position
        self._ball = ball
        self._is_down = is_down

    def get_position(self):
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
            positions.append(p.get_position())
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


class Tackle(Move):
    """
    The move of Forcing a piece's way through, defined by the two pieces
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Tackle"


class FootKick(Move):
    """
        The move of Forcing a piece's way through, defined by the two pieces
        """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "FootKick"


class Try(Move):
    """
    The move of Trying,
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Try"
