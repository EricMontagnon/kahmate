import model
import kahmate


def essai_initialisation_jeu():
    piece1 = model.Piece(1, 1, [100, 100], False)
    piece2 = model.Piece(1, 1, [500, 500], False)
    game = kahmate.Game(["Jean", "Jacques"], [[piece1], [piece2]], ["blue", "blue"])
    positions = game.get_positions()
    print("essai_initialisation_jeu")
    print("positions == [[[100, 100]], [[500, 500]]] :", positions == [[[100, 100]], [[500, 500]]])

essai_initialisation_jeu()
