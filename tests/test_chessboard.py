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

