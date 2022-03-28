from datetime import timedelta
from os import environ

import numpy as np

import pytest

from hypothesis import given, settings
from hypothesis.strategies import integers

from polyomino import TilingProblem
from polyomino.board import Rectangle
from polyomino.constant import PENTOMINOS, TETROMINOS
from polyomino.constant import ALL_PENTOMINOS
from polyomino.tileset import exactly


def test_tile_chessboard():
    board = Rectangle(8, 8)
    TILES = list(PENTOMINOS.values()) + [TETROMINOS['Square']]
    problem = TilingProblem(board, exactly(TILES))
    solution = problem.solve()
    actual = solution.tiling
    assert len(actual) == 13


def test_tile_chessboard_check_problem():
    board = Rectangle(8, 8)
    TILES = list(PENTOMINOS.values()) + [TETROMINOS['Square']]
    problem = TilingProblem(board, exactly(TILES))
    problem.make_problem()
    
    assert 37 * 16 < problem.array.shape[0] < 4 * 49 * 13
    assert problem.array.shape[1] == 77

    row_sums = np.sum(problem.array, 1)  
    assert min(row_sums) == 5
    assert max(row_sums) == 6

    assert len(problem.key) == problem.array.shape[0]


@pytest.mark.skipif('POLYOMINO_SLOW_TESTS' not in environ, reason="No slow tests")
@given(x=integers(0, 3), y=integers(0, 3))
@settings(deadline=timedelta(milliseconds=1000))
def test_tile_chessboard_minus_square(x, y):
    board = Rectangle(8, 8).remove_all([(x, y), (x+1, y), (x, y+1), (x+1, y+1)])
    problem = TilingProblem(board, exactly(ALL_PENTOMINOS).with_reflections())
    solution = problem.solve()
    actual = solution.tiling
    assert len(actual) == 12
