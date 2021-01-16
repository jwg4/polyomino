import pytest

from polyomino.board import Rectangle
from polyomino.constant import TETROMINOS
from polyomino.error import CoverWithWrongModulus, CoverWithWrongSize
from polyomino.tileset import Tileset


def test_not_enough_tiles():
    board = Rectangle(3, 3)
    tile = TETROMINOS['T']
    tileset = Tileset([(tile, 2)])
    with pytest.raises(CoverWithWrongSize):
        tileset.check(board)


def test_too_many_tiles():
    board = Rectangle(3, 4)
    tile = TETROMINOS['T']
    tileset = Tileset([(tile, 4)])
    with pytest.raises(CoverWithWrongSize):
        tileset.check(board)

    
def test_wrong_gcd():
    board = Rectangle(3, 3)
    tile = TETROMINOS['T']
    tileset = Tileset([(tile, 0)])
    with pytest.raises(CoverWithWrongModulus):
        tileset.check(board)
