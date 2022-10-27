import model
import random

UNICODE_COLORS = {
    None: "\U00002B1A",
    model.Color.BLACK: "\U00002B1B",
    model.Color.BLUE: "\U0001F7E6",
    model.Color.GREEN: "\U0001F7E9",
    model.Color.RED: "\U0001F7E5",
    model.Color.WHITE: "\U00002B1C",
    model.Color.YELLOW: "\U0001F7E8",
}


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

    def __init__(self, players):
        self._board = model.Board()
        self._players = []
        for player in players:
            if isinstance(player, str):
                self._players.append(model.HumanPlayer(player))
            elif isinstance(player, model.Level):
                self._players.append(model.AIPlayer(player))
            else:
                assert False, "unknown player definition"
        self._next_player = 0

    def next_player(self):
        return self._players[self._next_player]

    def generate_valid_moves(self):
        moves = []
        pass

    def winners(self):
        pass

    def __str__(self):
        pass


if __name__ == "__main__":
    game = Game(["xclerc", model.Level.HARD])
    print(game)