import dataclasses
import enum
import random

i_limit = 600
j_limit = 800


class PieceType(enum.Enum):
    """
    The various possible types of a piece.
    [speed, attack_strength, defense_strength]
    """

    NONE = [0, 0, 0]
    REGULAR = [3, 0, 0]
    BIG = [2, 2, 1]
    TOUGH = [3, 1, 0]
    FAST = [4, -1, 1]
    SMART = [3, 0, 1]


class Piece:
    """
    A piece is defined by :
    - its player's ID
    - its ID
    - its type
    - its position
    - if it has the ball or not
    - if it is down (cannot play) or not
    """
    def __init__(self, playerID: int, pieceID: int,  piece_type, position: [int, int], ball: bool, is_down: bool):
        self._playerID = playerID
        self._ID = pieceID
        self._piece_type = piece_type
        self._position = position
        self._ball = ball
        self._is_down = is_down

    def __str__(self):
        type_piece = "The unknown guy"
        if self._piece_type == PieceType.REGULAR.value:
            type_piece = "The regular guy"
        if self._piece_type == PieceType.BIG.value:
            type_piece = "The big guy"
        if self._piece_type == PieceType.FAST.value:
            type_piece = "The fast guy"
        if self._piece_type == PieceType.SMART.value:
            type_piece = "The smart guy"
        if self._piece_type == PieceType.TOUGH.value:
            type_piece = "The tough guy"
        has_ball = " "
        if self._ball:
            has_ball = "has the ball"
        if not self._ball:
            has_ball = "does not have the ball"
        down = " "
        if self._is_down :
            down = "and needs to recover"
        if not self._is_down:
            down = "and is ready to play"
        ans = " ".join((type_piece, "located at", str(self._position), has_ball, down))
        return ans

    def get_position(self):
        return self._position

    def set_position(self, position: [int, int], ball: bool, down: bool):
        self._position = position
        self._ball = ball
        self._is_down = down

    @ property
    def speed(self):
        return self._piece_type[0]

    @property
    def attack(self):
        return self._piece_type[1]

    @property
    def defense(self):
        return self._piece_type[2]

    @property
    def playerID(self):
        return self._playerID

    @property
    def ID(self):
        return self._ID

    def ball(self):
        return self._ball


class Player:
    """
    A player is defined by:
    - its ID
    - the list of his pieces
    - the color of his team
    - his strength card deck
    """

    def __init__(self, ID: int,  pieces, color):
        self._ID = ID
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

    def update_positions(self, pieceID: int, new_position: [int, int], ball: bool, down: bool):
        self._pieces[pieceID].set_position(new_position, ball, down)

    def pick_strength(self):
        random.shuffle(self._strength_deck)
        picked = self._strength_deck.pop()
        if len(self._strength_deck) == 0:
            self._strength_deck = [1, 2, 3, 4, 5, 6]
        return picked

    # setters?


class HumanPlayer(Player):
    """
    A human player is simply a player with a name, as a string.
    """

    def __init__(self, name: str,  ID: int, pieces, color):
        super().__init__(ID, pieces, color)
        self._name = name

    def __str__(self):
        ans = "This is " + self._name + "'s Team : "
        for piece in self._pieces:
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

    def __init__(self, level, ID: int, pieces, color):
        super().__init__(ID, pieces, color)
        self._level = level

    @property
    def level(self):
        return self._level

    def __str__(self):
        ans = "This is a" + str(self.level) + "AI's Team : "
        for piece in self._pieces:
            ans += "\n" + str(piece)
        return ans


class Game:
    """
    The state of the game, defined by:
    - a board;
    - a list of players
    - an integer used as the index of the next player in the list of players.

    When building the list of players, the argument `player` is used and:
    - if an item is a string (`str`) then a human player is built using the
      string as their name;
    - if an item is a level (`Level`) then an AI player is built using the
      level.
    """

    def __init__(self, players, pieces, colors, ball_position):
        self._players = []
        k = -1
        for player in players:
            k += 1
            if isinstance(player, str):
                self._players.append(HumanPlayer(player, k, pieces[k], colors[k]))
            elif isinstance(player, Level):
                self._players.append(AIPlayer(player, k, pieces[k], colors[k]))
            else:
                assert False, "unknown player definition"
        self._currentPlayer = 0
        self._ball_position = ball_position
        self._board = self.board_state()

    def __str__(self):
        ans = "Description of the first team :"
        ans += "\n" + str(self._players[0])
        ans += "\n" + " "
        ans += "\n" + "Description of the second team :"
        ans += "\n" + str(self._players[1])
        return ans

    def get_positions(self):
        return[self._players[0].get_positions(), self._players[1].get_positions()]

    def board_state(self):
        piece0 = Piece(-1, -1, PieceType.NONE, [-1, -1], False, False)
        board = []
        team1 = self._players[0].pieces
        team2 = self._players[1].pieces
        for i in range(i_limit):
            board.append([])
            for j in range(j_limit):
                found_piece = False
                for piece in team1:
                    if piece.get_position() == [i, j]:
                        board[i].append(piece)
                        found_piece = True
                for piece in team2:
                    if piece.get_position() == [i, j]:
                        board[i].append(piece)
                        found_piece = True
                if not found_piece:
                    board[i].append(piece0)
        return board

    def update_positions(self, playerID: int, pieceID: int, new_position: [int, int], ball: bool, down: bool):
        self._players[playerID].update_positions(pieceID, new_position, ball, down)

    def update_ball_position(self, new_position: [int, int]):
        self._ball_position = new_position

    def generate_displacement(self, playerID: int, pieceID: int):
        moves = []
        piece = self._players[playerID].pieces[pieceID]
        for i in range(i_limit):
            for j in range(j_limit):
                if 0 < abs(i-piece.get_position()[0])+abs(j-piece.get_position()[1]) <= piece.speed:
                    moves.append(Displacement(piece, [i, j]))
        return moves

    def generate_ball_throwing(self, playerID: int, pieceID: int):
        pass

    def generate_tackle(self, playerID: int, pieceID: int):
        pass

    def generate_try(self, playerID: int, pieceID: int):
        pass

    def update_board(self):
        self._board = self.board_state()

    def face_off(self, attack_player_ID, attack_piece_ID, defense_piece_ID):
        attack_player = self._players[attack_player_ID]
        defense_player = self._players[(attack_player_ID + 1) % 2]
        attack_piece = attack_player.pieces[attack_piece_ID]
        defense_piece = defense_player.pieces[defense_piece_ID]
        attack_score = attack_player.pick_strength() + attack_piece.attack
        defense_score = defense_player.pick_strength() + defense_piece.defense
        if attack_score > defense_score :
            return "Attack wins!"
        if defense_score > attack_score :
            return "Defense wins!"
        else:
            attack_pick = attack_player.pick_strength()
            defense_pick = defense_player.pick_strength()
            if attack_pick > defense_pick :
                return "Attack wins!"
            else:
                return "Defense wins!"

    def winners(self):
        pass


class Move:
    """
    The parent class of all possible moves.
    """

    def __init__(self):
        pass


class Displacement(Move):
    """
    The move of drawing cards from the train card deck.
    """
    def __init__(self, piece: Piece, new_position: [int, int], face_off_opponent=-1):
        super().__init__()
        self._piece = piece
        self._new_position = new_position
        self._face_off_opponent = face_off_opponent

    def __str__(self):
        return "Displacement of the piece " + str(self._piece.ID) + " to the position : " + str(self._new_position)

    def play(self, game: Game):
        if self._face_off_opponent == -1:
            game.update_positions(self._piece.playerID, self._piece.ID, self._new_position, self._piece.ball(), False)
            game.update_ball_position(self._new_position)
        else:
            result_face_off = game.face_off(self._piece.playerID, self._piece.ID, self._face_off_opponent)
            if result_face_off == "Denfense wins!":
                position = self._piece.get_position()
                if self._piece.ball():
                    game.update_ball_position([position[0], position[1] - 1])
                game.update_positions(self._piece.playerID, self._piece.ID, position, False, True)
            else:
                game.update_positions(self._piece.playerID, self._piece.ID, self._new_position, self._piece.ball(), False)
                game.update_ball_position(self._new_position)
                game.update_positions((self._piece.playerID+1) % 2, self._face_off_opponent, False, True)


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


piece1 = Piece(0, 0, PieceType.BIG.value, [100, 100], False, False)
piece2 = Piece(1, 0, PieceType.BIG.value, [500, 500], False, False)
game = Game(["Jean", "Jacques"], [[piece1], [piece2]], ["blue", "blue"], [int(i_limit/2), int(j_limit/2)])

displacement = game.generate_displacement(0, 0)
for d in displacement:
    print(d)