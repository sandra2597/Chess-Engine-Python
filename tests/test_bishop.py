# type: ignore

from app.pieces import Bishop, Knight
from app.schema import Position
from typing import List
import pytest


def test_calc_moves_1():
    position = Position(x=4, y=4)
    color = 'W'
    piece = Bishop(position, color)
    known_fields = []
    known_fields.append(Position(x=5, y=5))
    known_fields.append(Position(x=6, y=6))
    known_fields.append(Position(x=7, y=7))
    known_fields.append(Position(x=3, y=5))
    known_fields.append(Position(x=2, y=6))
    known_fields.append(Position(x=1, y=7))
    known_fields.append(Position(x=3, y=3))
    known_fields.append(Position(x=2, y=2))
    known_fields.append(Position(x=1, y=1))
    known_fields.append(Position(x=0, y=0))
    known_fields.append(Position(x=5, y=3))
    known_fields.append(Position(x=6, y=2))
    known_fields.append(Position(x=7, y=1))
    possible_fields = piece.get_allowed_moves([])
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields

def test_calc_moves_2():
    position = Position(x=4, y=4)
    color = 'W'
    piece = Bishop(position, color)
    known_fields = []
    known_fields.append(Position(x=5, y=5))
    known_fields.append(Position(x=6, y=6))
    known_fields.append(Position(x=7, y=7))
    known_fields.append(Position(x=3, y=5))
    known_fields.append(Position(x=2, y=6))
    known_fields.append(Position(x=1, y=7))
    known_fields.append(Position(x=3, y=3))
    known_fields.append(Position(x=2, y=2))
    known_fields.append(Position(x=1, y=1))
    known_fields.append(Position(x=5, y=3))
    known_fields.append(Position(x=6, y=2))
    known_fields.append(Position(x=7, y=1))

    other_pieces = []
    other_pieces.append(
        Knight(position=Position(x=1,y=1), color='B')
    )
    possible_fields = piece.get_allowed_moves(other_pieces)
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields
        

def test_calc_moves_3():
    position = Position(x=4, y=4)
    color = 'B'
    piece = Bishop(position, color)
    known_fields = []
    known_fields.append(Position(x=5, y=5))
    known_fields.append(Position(x=6, y=6))
    known_fields.append(Position(x=7, y=7))
    known_fields.append(Position(x=3, y=5))
    known_fields.append(Position(x=2, y=6))
    known_fields.append(Position(x=1, y=7))
    known_fields.append(Position(x=3, y=3))
    known_fields.append(Position(x=2, y=2))
    known_fields.append(Position(x=5, y=3))
    known_fields.append(Position(x=6, y=2))
    known_fields.append(Position(x=7, y=1))

    other_pieces = []
    other_pieces.append(
        Knight(position=Position(x=1,y=1), color='B')
    )
    possible_fields = piece.get_allowed_moves(other_pieces)
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields

