import pytest

from polyomino.board import Rectangle
from polyomino.constant import DOMINO, TETROMINOS
from polyomino.constant import ALL_PENTOMINOS
from polyomino.error import CoverWithWrongModulus, CoverWithWrongSize
from polyomino.tileset import Tileset


def test_not_enough_tiles():
    board = Rectangle(3, 3)
    tile = TETROMINOS["T"]
    tileset = Tileset([tile, tile], [], [])
    with pytest.raises(CoverWithWrongSize):
        tileset.check(board)


def test_too_many_tiles():
    board = Rectangle(3, 4)
    tile = TETROMINOS["T"]
    tileset = Tileset([tile] * 4, [], [])
    with pytest.raises(CoverWithWrongSize):
        tileset.check(board)


def test_wrong_gcd():
    board = Rectangle(3, 3)
    tile = TETROMINOS["T"]
    tileset = Tileset([], [], [tile])
    with pytest.raises(CoverWithWrongModulus):
        tileset.check(board)


def test_optional_tiles():
    tileset = Tileset([], ALL_PENTOMINOS, [DOMINO])
    board = Rectangle(20, 20)
    tileset.check(board)
