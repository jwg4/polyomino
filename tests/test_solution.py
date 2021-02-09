from polyomino.board import Rectangle
from polyomino.solution import Solution


def test_export_to_python():
    board = Rectangle(4, 4)
    tiling = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(1, 0), (1, 1), (1, 2), (1, 3)],
        [(2, 0), (2, 1), (2, 2), (2, 3)],
        [(3, 0), (3, 1), (3, 2), (3, 3)],
    ]
    solution = Solution(board, tiling)
    with open("tests/temp.py", "w") as out:
        out.write(solution.python())
    from tests.temp import TILING
    assert TILING == tiling
