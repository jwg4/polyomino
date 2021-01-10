from polyomino import TilingProblem
from polyomino.board import Rectangle
from polyomino.constant import PENTOMINOS, TETROMINOS


def test_tile_chessboard():
    board = Rectangle(8, 8)
    TILES = list(PENTOMINOS.values()) + [TETROMINOS['Square']]
    problem = TilingProblem(board, TILES)
    problem.solve()
    actual = problem.solution
    assert len(actual) == 13

