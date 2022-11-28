from kahmate import model
from kahmate.settings import *


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
        self._players = []
        for player, color in players:
            if isinstance(player, str):
                self._players.append(model.HumanPlayer(player, color))
            elif isinstance(player, model.Level):
                self._players.append(model.AIPlayer(player, color))
            else:
                assert False, "unknown player definition"
        self._next_player = 0

    def next_player(self):
        return self._players[self._next_player]

    def update(self):
        self._board.draw(self._screen, self._players)
        pg.display.update()

    def run(self):
        while self._running:
            for event in pg.event.get():
                self._clock.tick(FPS)
                if event.type == pg.QUIT:
                    self._running = False

            self.update()


if __name__ == "__main__":
    first_player = input('Name of the first player:')
    second_player = input('Name of the second player:')

    game = Game([(first_player, model.PlayerColor.BLUE), (second_player, model.PlayerColor.PINK)])
    game.run()



