from kahmate.settings import *
from kahmate import model
import pygame as pg


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // GRIDWIDTH
    col = x // GRIDWIDTH
    return row, col


class Game:
    def __init__(self, players):
        # init pygame
        pg.init()
        self.running = True
        self.clock = pg.time.Clock()

        # screen settings
        self.board = model.Board()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
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
        self.ball_position = [0, 0]
        self.valid_moves = []
        self.board.update_board(self.players)

    def next_player(self):
        return self.players[self._next_player]

    def update(self):
        self.board.draw(self.screen, self.players)
        pg.display.update()

    def __str__(self):
        ans = "Description of the first team :"
        ans += "\n" + str(self.players[0])
        ans += "\n" + " "
        ans += "\n" + "Description of the second team :"
        ans += "\n" + str(self.players[1])
        return ans

    def generate_displacement(self, x, y):
        # LOOPS TO BE OPTIMIZED
        piece = self.board.matrix[x][y]
        if piece in self.next_player().pieces:
            for i in range(ROWS):
                for j in range(COLS):
                    distance_ok = 0 < abs(i-piece.position[0]) + abs(j-piece.position[1]) <= piece.speed
                    empty_case = self.board.matrix[i][j] is None
                    if distance_ok and empty_case:
                        self.valid_moves.append(model.Displacement(piece, [i, j], None))

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
            attack_pick = attack_player.pick_strength() + attack_piece.attack
            defense_pick = defense_player.pick_strength() + defense_piece.defense
            if attack_pick > defense_pick:
                return "Attack wins!"
            else:
                return "Defense wins!"

    def play(self, move: model.Displacement):
        if move.face_off_opponent is None:
            move.piece.position = move.new_position
            if move.piece.has_ball:
                self.ball_position = move.new_position
        else:
            result_face_off = game.face_off(move.piece, move.face_off_opponent)
            if result_face_off == "Defense wins!":
                position = move.piece.position()
                if move.piece.has_ball:
                    self.ball_position = [position[0], position[1] - 1]
                move.piece.is_down = True
            else:
                move.piece.position = move.new_position,
                if move.piece.has_ball:
                    self.ball_position = move.new_position
                move.face_off_opponent.is_down = True
        self.board.update_board(self.players)

    def run(self):
        while self.running:
            for event in pg.event.get():
                self.clock.tick(FPS)
                if event.type == pg.QUIT:
                    self.running = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    x, y = get_row_col_from_mouse(mouse_pos)
                    if self.valid_moves:
                        for move in self.valid_moves:
                            if [x, y] == move.new_position:
                                self.play(move)
                                self.valid_moves = []
                                self._next_player = (self._next_player + 1) % 2
                    else:
                        self.generate_displacement(x, y)

            self.update()


if __name__ == "__main__":
    first_player = input('Name of the first player:')
    second_player = input('Name of the second player:')

    game = Game([(first_player, model.PlayerColor.BLUE), (second_player, model.PlayerColor.PINK)])

    game.run()
