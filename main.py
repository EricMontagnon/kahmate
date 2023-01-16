from kahmate.settings import *
from kahmate import model
import pygame as pg


def get_row_col_from_mouse(pos):
    """
    Converts the position of the mouse into a position on the grid
    """
    x, y = pos
    row = y // GRIDWIDTH
    col = x // GRIDWIDTH
    return row, col


class Game:
    """
    PARAMETERS :
    running : boolean           -> state of the game
    clock
    screen
    players : list of model.Players
    _next_player : int          -> index of the next player
    ball_position : [int, int]  -> used to display the ball
    board : model.Board         -> contains the players' pieces in a more practical way
    valid_moves : list of moves -> possible moves for the selected piece
    turn_count : int            -> used to decide whose turn it is and when to resuscitate a piece

    METHODS :
    __init__(players)        -> create a game from the names of the players and their colors
    next_player() : Player   -> outputs the next player
    update()                -> update the ball's owner, which piece is down, the screen
    __str__()               -> creates a description of the deck in str
    opponent_search(search_pos, piece_pos) -> checks if there is an opponent between search_pos and piece_pos)
    generate_displacement(x, y) -> adds in _valid_moves a list of model.Displacement for the piece located at [x, y]
    generate_pass(x, y)         -> adds in _valid_moves a list of model.Pass for the piece located at [x, y]
    face_off(attack_piece, defense_piece) -> simulates a face off between two pieces for example in a conflict of disp
    run()                   -> plays the game
    """
    def __init__(self, players):
        """
        Entry :  list of players [(name_player1 : str, name_player2), (color_player1: model.Color, color_player2)]
        Output : Game ready to play
        """
        # init pygame
        pg.init()
        self.running = True
        self.clock = pg.time.Clock()

        # screen settings
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        icon = pg.image.load(IMG_PATH/'ball.png')
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

        # define ball
        self.players[0].pieces[0].has_ball = True
        self.ball_position = self.players[0].pieces[0].position

        # define board
        self.board = model.Board()
        self.board.update_board(self.players)

        # define move parameters
        self.valid_moves = []
        self.turn_count = 0

    def draw_bgd(self):
        self.screen.fill(BLACK)
        pg.draw.rect(self.screen, DARK_GREEN, (COLSAUX*GRIDWIDTH, ROWSAUX*GRIDWIDTH, COLS*GRIDWIDTH, ROWS*GRIDWIDTH))
        deck = pg.transform.scale(pg.image.load(IMG_PATH / 'deck.png'), (118, 140))
        self.screen.blit(deck, (COLSAUX*GRIDWIDTH/2 - 118/2, (ROWSAUX+1)*GRIDWIDTH))
        self.screen.blit(deck, ((COLSAUX + COLS)*GRIDWIDTH + COLSAUX*GRIDWIDTH/2 - 118/2, (ROWSAUX+1) * GRIDWIDTH))
        for row in range(ROWSAUX, ROWS + ROWSAUX):
            for col in range(row % 2 + COLSAUX, COLS + COLSAUX, 2):
                pg.draw.rect(self.screen, GREEN, (col*GRIDWIDTH, row*GRIDWIDTH, GRIDWIDTH, GRIDWIDTH))

    def draw(self):
        self.draw_bgd()
        for move in self.valid_moves:
            move.draw(self.screen)
        for player in self.players:
            player.draw(self.screen)
        self.screen.blit(BALL, (self.ball_position[1] * GRIDWIDTH, self.ball_position[0] * GRIDWIDTH))

    def next_player(self):
        """
        output : player
        """
        return self.players[self._next_player]

    def update(self):
        """
        If a player has the same position as the ball, it takes it
        If a player has been down for long enough, it comes back up
        The screen is updated
        """
        for player in self.players:
            for piece in player.pieces:
                if piece.position == self.ball_position and piece.has_ball == False:
                    piece.has_ball = True
                if -1 < piece.turn_death + 3 < self.turn_count:
                    piece.is_down = False
                    piece.turn_death = -1
        self.board.draw(self.screen, self.players, self.ball_position, self.valid_moves)
        pg.display.update()
        self.is_end()

    def __str__(self):
        ans = "Description of the first team :"
        ans += "\n" + str(self.players[0])
        ans += "\n" + " "
        ans += "\n" + "Description of the second team :"
        ans += "\n" + str(self.players[1])
        return ans

    def opponent_search(self, search_position, piece_position):
        """
        inputs : search_position = position of the pass or of the displacement desire
                piece_position = position of the active piece
        output : face off opponent if there is an opponent between the two positions
        """
        face_off_opponent = None
        distance = abs(search_position[0] - piece_position[0]) + abs(search_position[1] - piece_position[1])
        for k in range(distance - 1):
            case_x = int(((k + 1) / distance) * search_position[0] + ((distance - (k + 1)) / distance) * piece_position[0])
            case_y = int(((k + 1) / distance) * search_position[1] + ((distance - (k + 1)) / distance) * piece_position[1])
            if self.board.matrix[case_x][case_y] is not None:
                possible_foo = self.board.matrix[case_x][case_y]
                if possible_foo in self.players[(self._next_player + 1) % 2].pieces and not possible_foo.is_down:
                    face_off_opponent = possible_foo
        return face_off_opponent

    def generate_displacement(self, x: int, y: int):
        """
        input : x, y position of the case to try
        output : if a piece in the right team has [x,y] for position, list of model.Displacement possible for the piece
        """
        piece = self.board.matrix[x][y]
        if piece in self.next_player().pieces and not piece.is_down and not piece.has_moved:
            for i in range(1, ROWS+ROWSAUX):
                if self._next_player == 0:
                    mini = COLSAUX
                    maxi = COLS + COLSAUX + 1
                else:
                    mini = COLSAUX - 1
                    maxi = COLS + COLSAUX
                for j in range(mini, maxi):
                    distance_ok = 0 < abs(i-piece.position[0]) + abs(j-piece.position[1]) <= piece.speed
                    empty_case = self.board.matrix[i][j] is None
                    if distance_ok and empty_case:
                        face_off_opponent = self.opponent_search([i, j], piece.position)
                        self.valid_moves.append(model.Displacement(piece, [i, j], face_off_opponent))
                    if distance_ok and not empty_case:
                        possible_opponent = self.board.matrix[i][j]
                        if possible_opponent in self.players[(self._next_player + 1) % 2].pieces and possible_opponent.has_ball:
                            self.valid_moves.append(model.Tackle(piece, possible_opponent))

    def generate_pass(self, x: int, y: int):
        """
        input : x, y position of the case to try
        output : if a piece in the right team has [x,y] for position, list of model.Pass possible for the piece
        """
        piece = self.board.matrix[x][y]
        if piece in self.next_player().pieces and not piece.is_down and piece.has_ball:
            for i in range(max(1, piece.position[0]-2), min(ROWS+1, piece.position[0]+3)):
                if self._next_player == 0:
                    mini = max(1, piece.position[1] - 2)
                    maxi = piece.position[1]
                else:
                    mini = min(COLS+4, piece.position[1]+1)
                    maxi = min(COLS+4, piece.position[1]+3)
                for j in range(mini, maxi):
                    if self.board.matrix[i][j] is not None :
                        possible_friend = self.board.matrix[i][j]
                        if possible_friend in self.players[self._next_player].pieces:
                            face_off_opponent = self.opponent_search([i, j], piece.position)
                            self.valid_moves.append(model.Pass(piece, possible_friend, face_off_opponent))

    def face_off(self, attack_piece: model.Piece, defense_piece: model.Piece):
        """
        input : attack_piece = piece that want to move or pass the ball
            defense_piece = piece which is in the way
        output : result of the face off as a str
        """
        attack_player = self.players[self._next_player]
        defense_player = self.players[(self._next_player + 1) % 2]
        attack_score = attack_player.pick_strength() + attack_piece.attack
        defense_score = defense_player.pick_strength() + defense_piece.defense
        if attack_score >= defense_score + 2:
            return "Plaquage parfait!"
        if defense_score + 2 > attack_score > defense_score:
            return "Attack wins!"
        if defense_score > attack_score:
            return "Defense wins!"
        else:
            attack_pick = attack_player.pick_strength() + attack_piece.attack
            defense_pick = defense_player.pick_strength() + defense_piece.defense
            if attack_score >= defense_score + 2:
                return "Plaquage parfait!"
            if attack_pick > defense_pick:
                return "Attack wins!"
            else:
                return "Defense wins!"

    def is_end(self):
        if self.ball_position[1] < COLSAUX:
            print("PINK HAS WON!!!!")
            self.running = False
        if self.ball_position[1] >= COLS + COLSAUX:
            print("BLUE HAS WON!!!!")
            self.running = False

    def run(self):
        """
        one characteristic loop :
        if no movement have been calculated :
            generation of the possible displacements and passes stored in _valid_moves
        once movements have been calculated :
            wait for a movement to be selected and play it
        """
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
                            if [x, y] == move.second_position:
                                move.play(self)
                                self.valid_moves = []
                    else:
                        self.generate_displacement(x, y)
                        self.generate_pass(x, y)
            self.update()



if __name__ == "__main__":
    game = Game([('BLUE', model.Color.BLUE), ('PINK', model.Color.PINK)])
    game.run()
