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
        self.turn_count = 0
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
        self.players[0].pieces[0].has_ball = True
        self.ball_position = self.players[0].pieces[0].position
        self.valid_moves = []
        self.board.update_board(self.players)
        self.turn_count = 0

    def next_player(self):
        return self.players[self._next_player]

    def update(self):
        for player in self.players:
            for piece in player.pieces :
                if piece.position == self.ball_position:
                    piece.has_ball = True
                if -1 < piece.turn_death + 3 < self.turn_count:
                    piece.is_down = False
                    piece.turn_death = -1
        self.board.draw(self.screen, self.players, self.ball_position, self.valid_moves)
        pg.display.update()

    def __str__(self):
        ans = "Description of the first team :"
        ans += "\n" + str(self.players[0])
        ans += "\n" + " "
        ans += "\n" + "Description of the second team :"
        ans += "\n" + str(self.players[1])
        return ans

    def opponent_search(self, search_position, piece_position):
        face_off_opponent = None
        distance = abs(search_position[0] - piece_position[0]) + abs(search_position[1] - piece_position[1])
        for k in range(distance - 1):
            case_x = int(((k + 1) / distance) * search_position[0] + ((distance - (k + 1)) / distance) * piece_position[0])
            case_y = int(((k + 1) / distance) * search_position[1] + ((distance - (k + 1)) / distance) * piece_position[1])
            if self.board.matrix[case_x][case_y] is not None:
                possible_foo = self.board.matrix[case_x][case_y]
                if possible_foo in self.players[(self._next_player + 1) % 2].pieces:
                    face_off_opponent = possible_foo
        return face_off_opponent


    def generate_displacement(self, x, y):
        # LOOPS TO BE OPTIMIZED
        piece = self.board.matrix[x][y]
        if piece in self.next_player().pieces and not piece.is_down:
            for i in range(ROWS):
                for j in range(COLS):
                    distance_ok = 0 < abs(i-piece.position[0]) + abs(j-piece.position[1]) <= piece.speed
                    empty_case = self.board.matrix[i][j] is None
                    if distance_ok and empty_case:
                        face_off_opponent = self.opponent_search([i, j], piece.position)
                        self.valid_moves.append(model.Displacement(piece, [i, j], face_off_opponent))

    def generate_pass(self, x, y):
        piece = self.board.matrix[x][y]
        if piece in self.next_player().pieces and not piece.is_down:
            for i in range(max(0, piece.position[0]-2), min(ROWS, piece.position[0]+3)):
                if self._next_player == 0:
                    mini = max(0, piece.position[1] - 2)
                    maxi = piece.position[1]
                else:
                    mini = piece.position[1]
                    maxi = min(ROWS, piece.position[1]+2)
                for j in range(mini, maxi):
                    if self.board.matrix[i][j] is not None :
                        possible_friend = self.board.matrix[i][j]
                        if possible_friend in self.players[self._next_player].pieces:
                            face_off_opponent = self.opponent_search([i, j], piece.position)
                            self.valid_moves.append(model.Pass(piece, possible_friend,face_off_opponent))


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

    def play_displacement(self, move: model.Displacement):
        if move.face_off_opponent is None:
            move.piece.position = move.new_position
            if move.piece.has_ball:
                self.ball_position = move.new_position
        else:
            result_face_off = game.face_off(move.piece, move.face_off_opponent)
            print(result_face_off)
            if result_face_off == "Defense wins!":
                position = move.piece.position
                if move.piece.has_ball:
                    move.piece.has_ball = False
                    if self.next_player()._color == model.Color.PINK:
                        self.ball_position = [position[0], position[1] + 1]
                    else :
                        self.ball_position = [position[0], position[1] - 1]
                move.piece.is_down = True
                move.piece.turn_death = self.turn_count
            else:
                move.piece.position = move.new_position
                if move.piece.has_ball:
                    self.ball_position = move.new_position
                move.face_off_opponent.is_down = True
                move.face_off_opponent.turn_death = self.turn_count
        self.board.update_board(self.players)
        self.turn_count += 1
        self._next_player = (self.turn_count // 2) % 2

    def play_pass(self, move: model.Pass):
        move.piece.has_ball = False
        move.new_piece.has_ball = True
        self.ball_position = move.new_piece.position
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
                            if type(move) == model.Displacement:
                                if [x, y] == move.new_position:
                                    self.play_displacement(move)
                                    self.valid_moves = []
                            if type(move) == model.Pass:
                                if [x, y] == move.new_piece.position:
                                    self.play_pass(move)
                                    self.valid_moves = []
                    else:
                        self.generate_displacement(x, y)
                        self.generate_pass(x, y)
                        self.board.draw_displacements(self.valid_moves, self.screen)
            self.update()


if __name__ == "__main__":
    first_player = input('Name of the first player:')
    second_player = input('Name of the second player:')

    game = Game([(first_player, model.Color.BLUE), (second_player, model.Color.PINK)])
    game.run()



