from typing import TYPE_CHECKING

from kahmate import model
from kahmate.settings import *

if TYPE_CHECKING:
    from kahmate.model import Piece


class Game:
    def __init__(self, players):
        # init pygame
        pg.init()
        self._running = True
        self._clock = pg.time.Clock()

        # screen settings
        self._board = model.Board()
        self._screen = pg.display.set_mode((WIDTH, HEIGHT))
        icon = pg.image.load('img/ball.png')
        pg.display.set_icon(icon)
        pg.display.set_caption(TITLE)

        # define players
        self.players = []
        for player, color in players:
            if isinstance(player, str):
                self.players.append(model.HumanPlayer(player, color))
            elif isinstance(player, model.Level):
                self.players.append(model.AIPlayer(player, color))
            else:
                assert False, "unknown player definition"
        self._next_player = 0
        self._ball_position = [0, 0]

    def next_player(self):
        return self.players[self._next_player]

    def update(self):
        self._board.draw(self._screen, self.players)
        pg.display.update()

    def __str__(self):
        ans = "Description of the first team :"
        ans += "\n" + str(self.players[0])
        ans += "\n" + " "
        ans += "\n" + "Description of the second team :"
        ans += "\n" + str(self.players[1])
        return ans

    def generate_displacement(self, piece: 'Piece'):
        # LOOPS TO BE OPTIMIZED
        moves = []
        for i in range(ROWS):
            for j in range(COLS):
                distance_ok = 0 < abs(i - piece.position[0]) + abs(j - piece.position[1]) <= piece.speed
                empty_case = self._board.matrix[i][j] is None
                if distance_ok and empty_case:
                    moves.append(Displacement(piece, [i, j]))
        return moves

    def face_off(self, attack_piece: model.Piece, defense_piece: model.Piece):
        attack_player = self.players[self._next_player]
        defense_player = self.players[(self._next_player + 1) % 2]
        attack_score = attack_player.pick_strength() + attack_piece.attack
        defense_score = defense_player.pick_strength() + defense_piece.defense
        if attack_score > defense_score:
            return "Attack wins!"
        if defense_score > attack_score:
            return "Defense wins!"
        else:
            attack_pick = attack_player.pick_strength() - attack_piece
            defense_pick = defense_player.pick_strength()
            if attack_pick > defense_pick:
                return "Attack wins!"
            else:
                return "Defense wins!"

    def update_ball_position(self, new_position: [int, int]):
        self._ball_position = new_position

    def update_board(self):
        self._board.update_board(self.players)

    def run(self):
        while self._running:
            for event in pg.event.get():
                self._clock.tick(FPS)
                if event.type == pg.QUIT:
                    self._running = False

            self.update()


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

    def __init__(self, piece: model.Piece, new_position: [int, int], face_off_opponent=None):
        super().__init__()
        self._piece = piece
        self._new_position = new_position
        self._face_off_opponent = face_off_opponent

    def __str__(self):
        return "Displacement of the piece " + str(self._piece.name) + " to the position : " + str(self._new_position)

    def play(self, game: Game):
        if self._face_off_opponent.position == [-1, -1]:
            self._piece.position = self._new_position
            if self._piece.has_ball:
                game.update_ball_position(self._new_position)
        else:
            result_face_off = game.face_off(self._piece, self._face_off_opponent)
            if result_face_off == "Denfense wins!":
                position = self._piece.position()
                if self._piece.has_ball:
                    game.update_ball_position([position[0], position[1] - 1])
                self._piece.is_down = True
            else:
                self._piece.position = self._new_position,
                if self._piece.has_ball:
                    game.update_ball_position(self._new_position)
                self._face_off_opponent.is_down = True
            game.update_board()


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


if __name__ == "__main__":
    first_player = input('Name of the first player:')
    second_player = input('Name of the second player:')

    game = Game([(first_player, model.PlayerColor.BLUE), (second_player, model.PlayerColor.PINK)])
    game.update_board()
    possible_displacements = game.generate_displacement(game.players[1].pieces[0])
    displacement = possible_displacements[2]
    displacement.play(game)

    print("LIST OF DISPLACEMENTS")
    for d in possible_displacements:
        print(d)

    game.run()
