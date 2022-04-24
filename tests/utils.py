

from typing import TypeVar, List
from app.pieces import Piece

PieceType = TypeVar('PieceType', bound=Piece)
def create_other_piece_dict(pieces: List[PieceType]):
    other_pieces = {}
    for piece in pieces:
        position = piece.position
        position_string = piece.calc_position_string(position)
        other_pieces[position_string] = piece
    return other_pieces