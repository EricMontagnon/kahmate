import model
import kahmate

def test_initialisation_piece():
    piece1 = model.Piece(model.PieceType.BIG, [100, 100], False, False)
    assert piece1.get_position() == [100, 100]

def test_initialisation_player():
    piece1 = model.Piece(model.PieceType.BIG, [100, 100], False, False)
    player1 = model.HumanPlayer("Jacques", [piece1], "blue")
    assert piece1.get_position() == [100, 100]

def test_initialisation_jeu():
    piece1 = model.Piece(model.PieceType.BIG, [100, 100], False, False)
    piece2 = model.Piece(model.PieceType.BIG, [500, 500], False, False)
    game = kahmate.Game(["Jean", "Jacques"], [[piece1], [piece2]], ["blue", "blue"])
    positions = game.get_positions()
    assert positions == [[[100, 100]], [[500, 500]]]

def test_movement_initialisation():
    pass

def test_basic_movement():
    pass


