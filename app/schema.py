from  pydantic import BaseModel, validator

class Position(BaseModel):
    x: int
    y: int

    @validator('x', 'y')
    def name_must_contain_space(cls, v):
        if v < 0 or v > 7:
            raise ValueError('must be in the interval [0,7]')
        return v