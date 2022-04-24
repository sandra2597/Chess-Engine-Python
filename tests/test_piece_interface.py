
# type: ignore

from app.pieces.interfaces import Piece as PieceBase
from app.schema import Displacement, Position
from typing import List
import pytest
from .utils import create_other_piece_dict

class Piece(PieceBase):
    def get_allowed_moves(self, pieces: List["Piece"]) -> List[Position]:
        return []
def test_attributes():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Piece(position, color)
    assert hasattr(piece, 'position')
    assert hasattr(piece, 'color')
    assert hasattr(piece, 'has_moved')


def test_methods():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Piece(position, color)
    assert hasattr(piece, 'get_allowed_moves')
    get_allowed_moves_method = getattr(piece, 'get_allowed_moves')
    assert callable(get_allowed_moves_method)
    assert hasattr(piece, 'move')
    move_method = getattr(piece, 'move')
    assert callable(move_method)
    assert hasattr(piece, 'virtual_move')
    virtual_move_method = getattr(piece, 'virtual_move')
    assert callable(virtual_move_method)


def test_get_allowed_moves():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Piece(position, color)
    allowed_moves = piece.get_allowed_moves([])
    assert isinstance(allowed_moves, List)


def test_init_position_validation():
    position = [0, 0]
    color = 'W'
    with pytest.raises(TypeError):
        Piece(position, color)


def test_init_color_validation1():
    position = Position(x=0, y=0)
    color = 'Z'
    with pytest.raises(Exception):
        Piece(position, color)


def test_init_color_validation2():
    position = Position(x=0, y=0)
    color = 0
    with pytest.raises(Exception):
        Piece(position, color)


def test_move_position_validation():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Piece(position, color)
    with pytest.raises(TypeError):
        piece.move([1, 1])


def test_virtual_move_position_validation():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Piece(position, color)
    with pytest.raises(TypeError):
        piece.move([1, 1])

def test_has_moved_flag():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Piece(position, color)
    assert piece.has_moved == False
    new_position = Position(x=1, y=2)
    piece.move(new_position)
    assert piece.has_moved

def test_piece_moved():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Piece(position, color)
    new_position = Position(x=1, y=2)
    piece.move(new_position)
    assert piece.position == new_position

def test_piece_moved_virtual():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Piece(position, color)
    new_position = Position(x=1, y=2)
    piece.virtual_move(new_position)
    assert piece.position == new_position

def test_calc_new_position():
    old_position = Position(x=5, y=7)
    displacement = Displacement(x=2,y=-1)
    piece = Piece(position=old_position, color='W')
    expected_position = Position(x=7,y=6)
    assert Piece.calc_new_position(old_position, displacement) == expected_position

def test_field_available():
    position = Position(x=5, y=7)
    piece = Piece(position=position, color='W')
    other_pieces = [
        Piece(position=Position(x=0,y=0), color='W'),
        Piece(position=Position(x=6,y=6), color='W'),
        Piece(position=Position(x=1,y=2), color='B')
    ]
    other_pieces_dict = create_other_piece_dict(other_pieces)
    assert piece.check_field_available(Position(x=6, y=6), other_pieces_dict) == False
    other_pieces = [
        Piece(position=Position(x=0,y=0), color='W'),
        Piece(position=Position(x=6,y=5), color='W'),
        Piece(position=Position(x=6,y=6), color='B')
    ]
    other_pieces_dict = create_other_piece_dict(other_pieces)
    assert piece.check_field_available(Position(x=6, y=6), other_pieces_dict)