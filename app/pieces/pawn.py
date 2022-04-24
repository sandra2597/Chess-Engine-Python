from typing import List
from app.schema import Position, Displacement
from .interfaces import Piece

class Pawn(Piece):
    """
    Class for the knight in chess
    """
    def __is_on_second_row(self) -> bool:
        """
        Determines whether the pawn is on the second row
        """
        if self.color == 'W' and self.position.y == 1:
            return True
        if self.color == 'B' and self.position.y == 6:
            return True
        return False

    def __get_move_displacements(self) -> List[Displacement]:
        """
        Calculates all displacements for moving (not taking) with the pawn
        """
        displacements = []
        if self.color == 'W':
            displacements.append(Displacement(x=0, y=1))
        if self.color == 'B':
            displacements.append(Displacement(x=0, y=-1))
        on_second_row = self.__is_on_second_row()
        if on_second_row:
            if self.color == 'W':
                displacements.append(Displacement(x=0, y=2))
            if self.color == 'B':
                displacements.append(Displacement(x=0, y=-2))
        return displacements

    def check_field_available(self, position: Position, pieces: List["Piece"]) -> bool:
        """
        Checks whether the target field is available when moving (not taking) with the pawn
        """
        for piece in pieces:
            if piece.position == position:
                return False
        return True

    def __get_possible_take_displacements(self) -> List[Displacement]:
        """
        Returns a list for all possible displacements when taking a piece
        """
        if self.color == 'W':
            return [
                Displacement(x=-1, y=1),
                Displacement(x=1, y=1),
            ]
        return [
            Displacement(x=-1, y=-1),
            Displacement(x=1, y=-1),
        ]

    def get_allowed_moves(self, pieces: List["Piece"]) -> List[Position]:
        """
        Returns list of allowed moves for the piece
        """
        displacements = self.__get_move_displacements()
        allowed_moves = []
        for displacement in displacements:
            new_position = self.__class__.calc_new_position(self.position, displacement)
            if new_position is not None and self.check_field_available(new_position, pieces):
                allowed_moves.append(new_position)

        take_displacements = self.__get_possible_take_displacements()
        for displacement in take_displacements:
            new_position = self.__class__.calc_new_position(self.position, displacement)
            if new_position is not None:
                field_is_occupied = self.check_field_occupied_by_opponent(new_position, pieces)
                if field_is_occupied:
                    allowed_moves.append(new_position)

        return allowed_moves
