from typing import List, Literal
from abc import ABC, abstractmethod
from app.schema import Position


class Piece(ABC):
    """
    Abstract base class from which all 6 types of pieces are derived
    """

    def __init__(self, position: Position, color: Literal['W', 'B']):
        if not isinstance(position, Position):
            raise TypeError("The argument position has the wrong type")
        if color not in ['W', 'B']:
            raise ValueError("The argument color must be either 'W' or 'B'")
        self.position = position
        self.color = color
        self.has_moved = False

    @abstractmethod
    def get_allowed_moves(self, pieces: List["Piece"]) -> List[Position]:
        """
        Returns list of allowed moves for the piece
        """

    def move(self, new_position: Position) -> None:
        """
        Executes a move
        """
        if not isinstance(new_position, Position):
            raise TypeError("The argument position has the wrong type")
        self.position = new_position
        self.has_moved = True

    def virtual_move(self, new_position: Position) -> None:
        """
        Executes a move, but does not mark the piece as has moved.
        This is used when the code wants to try out a move for validation
        """
        if not isinstance(new_position, Position):
            raise TypeError("The argument position has the wrong type")
        self.position = new_position