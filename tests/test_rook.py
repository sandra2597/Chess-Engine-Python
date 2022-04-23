# type: ignore

from app.pieces import Rook
from app.schema import Position
from typing import List
import pytest


def test_attributes():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Rook(position, color)
    assert hasattr(piece, 'position')
    assert hasattr(piece, 'color')
    assert hasattr(piece, 'has_moved')


def test_methods():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Rook(position, color)
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
    piece = Rook(position, color)
    allowed_moves = piece.get_allowed_moves([])
    assert isinstance(allowed_moves, List)


def test_init_position_validation():
    position = [0, 0]
    color = 'W'
    with pytest.raises(TypeError):
        Rook(position, color)


def test_init_color_validation1():
    position = Position(x=0, y=0)
    color = 'Z'
    with pytest.raises(Exception):
        Rook(position, color)


def test_init_color_validation2():
    position = Position(x=0, y=0)
    color = 0
    with pytest.raises(Exception):
        Rook(position, color)


def test_move_position_validation():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Rook(position, color)
    with pytest.raises(TypeError):
        piece.move([1, 1])


def test_virtual_move_position_validation():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Rook(position, color)
    with pytest.raises(TypeError):
        piece.move([1, 1])

def test_has_moved_flag():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Rook(position, color)
    assert piece.has_moved == False
    new_position = Position(x=1, y=2)
    piece.move(new_position)
    assert piece.has_moved

def test_piece_moved():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Rook(position, color)
    new_position = Position(x=1, y=2)
    piece.move(new_position)
    assert piece.position == new_position

def test_piece_moved_virtual():
    position = Position(x=0, y=0)
    color = 'W'
    piece = Rook(position, color)
    new_position = Position(x=1, y=2)
    piece.virtual_move(new_position)
    assert piece.position == new_position