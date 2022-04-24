#type: ignore[reportGeneralTypeIssues]
from app.pieces import Pawn, Knight, King
from app.schema import Position
from typing import List
import pytest
from .utils import create_other_piece_dict

def test_second_row_check_1():
    position = Position(x=4, y=2)
    color = 'W'
    piece = Pawn(position, color)
    assert piece._Pawn__is_on_second_row() == False

def test_second_row_check_2():
    position = Position(x=4, y=1)
    color = 'W'
    piece = Pawn(position, color)
    assert piece._Pawn__is_on_second_row()

def test_second_row_check_3():
    position = Position(x=4, y=6)
    color = 'B'
    piece = Pawn(position, color)
    assert piece._Pawn__is_on_second_row()

def test_field_available():
    position = Position(x=4, y=1)
    color = 'W'
    piece = Pawn(position, color)
    tested_position = Position(x=4, y=3)
    added_pieces = []
    added_pieces_dict = create_other_piece_dict(added_pieces)
    assert piece.check_field_available(tested_position, added_pieces_dict)
    added_pieces.append(
        Knight(position=Position(x=4,y=3), color='B')
    )
    added_pieces_dict = create_other_piece_dict(added_pieces)
    assert piece.check_field_available(tested_position, added_pieces_dict) ==False


def test_calc_moves_white_1():
    position = Position(x=4, y=2)
    color = 'W'
    piece = Pawn(position, color)
    known_fields = []
    known_fields.append(Position(x=4, y=3))
    possible_fields = piece.get_allowed_moves({})
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields

def test_calc_moves_white_2():
    position = Position(x=4, y=1)
    color = 'W'
    piece = Pawn(position, color)
    known_fields = []
    known_fields.append(Position(x=4, y=2))
    known_fields.append(Position(x=4, y=3))
    possible_fields = piece.get_allowed_moves({})
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields

def test_calc_moves_white_3():
    position = Position(x=4, y=2)
    color = 'W'
    piece = Pawn(position, color)
    known_fields = []

    other_pieces = []
    other_pieces.append(
        Knight(position=Position(x=4,y=3), color='B')
    )
    other_pieces_dict = create_other_piece_dict(other_pieces)
    possible_fields = piece.get_allowed_moves(other_pieces_dict)
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields
        

def test_calc_moves_white_4():
    position = Position(x=4, y=2)
    color = 'W'
    piece = Pawn(position, color)
    known_fields = []
    known_fields.append(Position(x=3, y=3))
    known_fields.append(Position(x=4, y=3))

    other_pieces = []
    other_pieces.append(
        Knight(position=Position(x=3,y=3), color='B')
    )
    other_pieces_dict = create_other_piece_dict(other_pieces)
    possible_fields = piece.get_allowed_moves(other_pieces_dict)
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields


def test_calc_moves_black_1():
    position = Position(x=4, y=5)
    color = 'B'
    piece = Pawn(position, color)
    known_fields = []
    known_fields.append(Position(x=4, y=4))
    possible_fields = piece.get_allowed_moves({})
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields

def test_calc_moves_black_2():
    position = Position(x=4, y=6)
    color = 'B'
    piece = Pawn(position, color)
    known_fields = []
    known_fields.append(Position(x=4, y=5))
    known_fields.append(Position(x=4, y=4))
    possible_fields = piece.get_allowed_moves({})
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields

def test_calc_moves_black_3():
    position = Position(x=4, y=5)
    color = 'B'
    piece = Pawn(position, color)
    known_fields = []

    other_pieces = []
    other_pieces.append(
        Knight(position=Position(x=4,y=4), color='B')
    )
    other_pieces_dict = create_other_piece_dict(other_pieces)
    possible_fields = piece.get_allowed_moves(other_pieces_dict)
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields
        

def test_calc_moves_black_4():
    position = Position(x=4, y=5)
    color = 'B'
    piece = Pawn(position, color)
    known_fields = []
    known_fields.append(Position(x=3, y=4))
    known_fields.append(Position(x=4, y=4))

    other_pieces = []
    other_pieces.append(
        Knight(position=Position(x=3,y=4), color='W')
    )
    other_pieces_dict = create_other_piece_dict(other_pieces)
    possible_fields = piece.get_allowed_moves(other_pieces_dict)
    assert len(possible_fields) == len(known_fields)
    for known_field in known_fields:
        assert known_field in possible_fields
