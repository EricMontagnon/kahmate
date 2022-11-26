import model
import kahmate

i_limit = 600
j_limit = 800


def test_initialisation_piece():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    assert str(piece1) == "The big guy located at [100, 100] does not have the ball and is ready to play"


def test_initialisation_player():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    player1 = model.HumanPlayer("Jacques", 0, [piece1], "blue")
    ans = "This is Jacques's Team : \n"
    ans += "The big guy located at [100, 100] does not have the ball and is ready to play"
    assert str(player1) == ans


def test_initialisation_jeu():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    piece2 = model.Piece(1, 0, model.PieceType.BIG.value, [500, 500], False, False)
    game = model.Game(["Jean", "Jacques"], [[piece1], [piece2]], ["blue", "blue"], [int(i_limit/2), int(j_limit/2)])
    ans = "Description of the first team :\n"
    ans += "This is Jean's Team : \n"
    ans += "The big guy located at [100, 100] does not have the ball and is ready to play\n"
    ans += " \n"
    ans += "Description of the second team :\n"
    ans += "This is Jacques's Team : \n"
    ans += "The big guy located at [500, 500] does not have the ball and is ready to play"
    assert str(game) == ans


def test_set_position_piece():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    piece1.set_position([200, 200], True, False)
    assert str(piece1) == "The big guy located at [200, 200] has the ball and is ready to play"


def test_set_position_player():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    player1 = model.HumanPlayer("Jacques", 0,  [piece1], "blue")
    player1.update_positions(0, [200, 200], True, False)
    assert str(piece1) == "The big guy located at [200, 200] has the ball and is ready to play"


def test_set_position_game():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    piece2 = model.Piece(1, 0, model.PieceType.BIG.value, [500, 500], False, False)
    game = model.Game(["Jean", "Jacques"], [[piece1], [piece2]], ["blue", "blue"], [int(i_limit/2), int(j_limit/2)])
    game.update_positions(0, 0, [200, 200], True, False)
    assert str(piece1) == "The big guy located at [200, 200] has the ball and is ready to play"


def test_initialisation_displacement():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    piece2 = model.Piece(1, 0, model.PieceType.BIG.value, [500, 500], False, False)
    game = model.Game(["Jean", "Jacques"], [[piece1], [piece2]], ["blue", "blue"], [int(i_limit/2), int(j_limit/2)])
    displacement = game.generate_displacement(0, 0)
    assert str(displacement[0]) == "Displacement of the piece 0 to the position : [98, 100]"


def test_play_displacement():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    piece2 = model.Piece(1, 0, model.PieceType.BIG.value, [500, 500], False, False)
    game = model.Game(["Jean", "Jacques"], [[piece1], [piece2]], ["blue", "blue"], [int(i_limit/2), int(j_limit/2)])
    displacement = game.generate_displacement(0, 0)
    displacement[0].play(game)
    assert str(piece1) == "The big guy located at [98, 100] does not have the ball and is ready to play"


def test_face_off():
    piece1 = model.Piece(0, 0, model.PieceType.BIG.value, [100, 100], False, False)
    piece2 = model.Piece(1, 0, model.PieceType.BIG.value, [500, 500], False, False)
    game = model.Game(["Jean", "Jacques"], [[piece1], [piece2]], ["blue", "blue"], [int(i_limit/2), int(j_limit/2)])
    face_off = game.face_off(0, 0, 0)
    assert face_off == "Attack wins!" or face_off == "Defense wins!"