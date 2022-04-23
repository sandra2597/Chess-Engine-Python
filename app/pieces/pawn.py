from .interfaces import Piece
from typing import List
from app.schema import Position

class Pawn(Piece):
    """
    Class for the knight in chess
    """
    def get_allowed_moves(self, pieces: List["Piece"]) -> List[Position]:
        """
        Returns list of allowed moves for the piece
        """
        return []
