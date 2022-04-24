from typing import Dict, List, Literal, Optional
from abc import ABC, abstractmethod
from app.schema import Displacement, Position


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

    @classmethod
    def calc_position_string(cls, position: Position):
        return f"{position.x}{position.y}"


    @classmethod
    def calc_new_position(cls, old_position: Position, displacement: Displacement) -> Optional[Position]:
        new_x = old_position.x + displacement.x
        new_y = old_position.y + displacement.y
        try:
            return Position(x=new_x, y=new_y)
        except ValueError:
            return None 

    def check_field_available(self, position: Position, pieces: Dict[str, "Piece"]) -> bool:
        position_string = self.__class__.calc_position_string(position)
        if not position_string in pieces.keys():
            return True
        piece = pieces[position_string]
        if piece.color == self.color:
            return False
        return True

    def check_field_occupied_by_opponent(self, position: Position, pieces: Dict[str, "Piece"]) -> bool:
        position_string = self.__class__.calc_position_string(position)
        if not position_string in pieces.keys():
            return False
        piece = pieces[position_string]
        if piece.color == self.color:
            return False
        return True


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