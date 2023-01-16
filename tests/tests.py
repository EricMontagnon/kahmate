from kahmate import model
from kahmate.settings import *
import main


def test_initialisation_piece():
    piece1 = model.Piece(model.PieceType.BIG)
    piece1.position = [100, 100]
    assert str(piece1) == "The BIG piece is located at [100, 100]"


def test_initialisation_blue_player():
    col = model.Color.BLUE
    player1 = model.HumanPlayer("Jacques", col)
    ans = "This is Jacques's Team : \n"
    types = [piecetype for piecetype in model.PieceType]
    types.append(model.PieceType.REGULAR)
    pos = BLUE_POS
    for k in range(len(pos)-1):
        ans += f"The {types[k].name} piece is located at {pos[k]}\n"
    ans += f"The {types[len(pos)-1].name} piece is located at {pos[len(pos)-1]}"
    assert str(player1) == ans


def test_initialisation_pink_player():
    col = model.Color.PINK
    player1 = model.HumanPlayer("Jacques", col)
    ans = "This is Jacques's Team : \n"
    types = [piecetype for piecetype in model.PieceType]
    types.append(model.PieceType.REGULAR)
    pos = PINK_POS
    for k in range(len(pos)-1):
        ans += f"The {types[k].name} piece is located at {pos[k]}\n"
    ans += f"The {types[len(pos)-1].name} piece is located at {pos[len(pos)-1]}"
    assert str(player1) == ans


def test_initialisation_jeu():
    game = main.Game([('BLUE', model.Color.BLUE), ('PINK', model.Color.PINK)])
    game.running = False
    types = [piecetype for piecetype in model.PieceType]
    types.append(model.PieceType.REGULAR)
    ans = "Description of the first team :\n"
    ans += "This is BLUE's Team : \n"
    pos = BLUE_POS
    for k in range(len(pos)):
        ans += f"The {types[k].name} piece is located at {pos[k]}\n"
    ans += " \n"
    ans += "Description of the second team :\n"
    ans += "This is PINK's Team : \n"
    pos = PINK_POS
    for k in range(len(pos)-1):
        ans += f"The {types[k].name} piece is located at {pos[k]}\n"
    ans += f"The {types[len(pos)-1].name} piece is located at {pos[len(pos)-1]}"
    assert str(game) == ans


def test_access_speed_piece():
    piece1 = model.Piece(model.PieceType.BIG)
    assert piece1.speed == model.PieceType.BIG.value[0]


def test_access_attack_piece():
    piece1 = model.Piece(model.PieceType.BIG)
    assert piece1.attack == model.PieceType.BIG.value[1]


def test_access_defense_piece():
    piece1 = model.Piece(model.PieceType.BIG)
    assert piece1.defense == model.PieceType.BIG.value[2]


def test_access_name_piece():
    piece1 = model.Piece(model.PieceType.BIG)
    assert piece1.name == model.PieceType.BIG.value[3]


def test_face_off():
    game = main.Game([('BLUE', model.Color.BLUE), ('PINK', model.Color.PINK)])
    game.running = False
    face_off = game.face_off(game.players[0].pieces[0], game.players[0].pieces[1])
    assert face_off == "Attack wins!" or face_off == "Defense wins!" or face_off == "Plaquage parfait!"
