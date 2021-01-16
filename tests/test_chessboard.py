import numpy as np

from polyomino import TilingProblem
from polyomino.board import Rectangle
from polyomino.constant import PENTOMINOS, TETROMINOS
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
