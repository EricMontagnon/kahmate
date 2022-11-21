import model
import random

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

    def __init__(self, players, pieces, colors):
        self._players = []
        k = -1
        for player in players:
            k += 1
            if isinstance(player, str):
                self._players.append(model.HumanPlayer(player, pieces[k], colors[k]))
            elif isinstance(player, model.Level):
                self._players.append(model.AIPlayer(player, pieces[k], colors[k]))
            else:
                assert False, "unknown player definition"
        self._currentPlayer = 0

    def currentPlayer(self):
        return self._currentPlayer

    def get_positions(self):
        return[self._players[0].get_positions(), self._players[1].get_positions()]

    def update_positions(self, playerID, pieceID, new_position, ball):
        self._players[playerID].update_positions(pieceID, new_position, ball)




    def generate_valid_moves(self):
        moves = []
        pass

    def winners(self):
        pass


if __name__ == "__main__":
    game = Game(["xclerc", model.Level.HARD])
    print(game)