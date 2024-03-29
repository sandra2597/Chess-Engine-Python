from .interfaces import Piece
from typing import List, Dict
from app.schema import Position, Displacement

class King(Piece):
    """
    Class for the knight in chess
    """
    def get_allowed_moves(self, pieces: Dict[str,"Piece"]) -> List[Position]:
        """
        Returns list of allowed moves for the piece
        """
        displacements = [
            Displacement(x=-1, y=1),
            Displacement(x=-1, y=0),
            Displacement(x=-1, y=-1),
            Displacement(x=0, y=1),
            Displacement(x=0, y=-1),
            Displacement(x=1, y=1),
            Displacement(x=1, y=0),
            Displacement(x=1, y=-1),
        ]
        allowed_moves = []
        for displacement in displacements:
            new_position = self.__class__.calc_new_position(self.position, displacement)
            if new_position is not None and self.check_field_available(new_position, pieces):
                allowed_moves.append(new_position)


        return allowed_moves
