from app.pieces import King
from app.schema import Position
from typing import List
import pytest
from .utils import create_other_piece_dict

def test_calc_moves_1():
    position = Position(x=0, y=0)
    color = 'W'
    piece = King(position, color)
    known_fields = []
    known_fields.append(Position(x=0, y=1))
    known_fields.append(Position(x=1, y=1))
    known_fields.append(Position(x=1, y=0))
    possible_fields = piece.get_allowed_moves({})
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields

def test_calc_moves_2():
    position = Position(x=4, y=4)
    color = 'W'
    piece = King(position, color)
    known_fields = []
    known_fields.append(Position(x=3, y=3))
    known_fields.append(Position(x=3, y=4))
    known_fields.append(Position(x=3, y=5))
    known_fields.append(Position(x=4, y=3))
    known_fields.append(Position(x=4, y=5))
    known_fields.append(Position(x=5, y=3))
    known_fields.append(Position(x=5, y=4))
    known_fields.append(Position(x=5, y=5))
    possible_fields = piece.get_allowed_moves({})
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields

def test_calc_moves_3():
    position = Position(x=4, y=4)
    color = 'B'
    piece = King(position, color)
    known_fields = []
    known_fields.append(Position(x=3, y=3))
    known_fields.append(Position(x=3, y=4))
    known_fields.append(Position(x=3, y=5))
    known_fields.append(Position(x=4, y=5))
    known_fields.append(Position(x=5, y=3))
    known_fields.append(Position(x=5, y=4))
    known_fields.append(Position(x=5, y=5))

    other_pieces = []
    other_pieces.append(
        King(position=Position(x=4,y=3), color='B')
    )
    other_pieces_dict = create_other_piece_dict(other_pieces)
    possible_fields = piece.get_allowed_moves(other_pieces_dict)
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields