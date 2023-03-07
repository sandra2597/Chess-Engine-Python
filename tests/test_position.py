# type: ignore

from app.schema import Position
import pytest


def test_range():
    with pytest.raises(ValueError):
        Position(x=8, y=0)

    with pytest.raises(ValueError):
        Position(x=0, y='hey')
