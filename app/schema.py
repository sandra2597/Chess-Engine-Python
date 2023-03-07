from  pydantic import BaseModel, validator

class Displacement(BaseModel):
    x: int
    y: int
    
class Position(BaseModel):
    x: int
    y: int

    @validator('x', 'y')
    @classmethod
    def name_must_contain_space(cls, value):
        if value < 0 or value > 7:
            raise ValueError('must be in the interval [0,7]')
        return value

