from .interfaces import Piece
from typing import List
from app.schema import Displacement, Position

class Rook(Piece):
    """
    Class for the knight in chess
    """
    def get_allowed_moves(self, pieces: List["Piece"]) -> List[Position]:
        """
        Returns list of allowed moves for the piece
        """
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        allowed_moves = []
        for direction in directions:
            displacements = []
            for i in range(1,8):
                displacement_x = direction[0] * i
                displacement_y = direction[1] * i
                displacement = Displacement(x=displacement_x, y=displacement_y)
                displacements.append(displacement)
                
            for displacement in displacements:
                new_position = self.__class__.calc_new_position(self.position, displacement)
                if new_position is None:
                    break
                if not self.check_field_available(new_position, pieces):
                    break

                if self.check_field_occupied_by_opponent(new_position, pieces):
                    allowed_moves.append(new_position)
                    break
                allowed_moves.append(new_position)

        return allowed_moves
