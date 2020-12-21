from exact_cover_np import get_exact_cover

from polyomino import TilingProblem
from polyomino.board import Rectangle
from polyomino.constant import PENTOMINOS, TETROMINOS


if __name__ == '__main__':
    board = Rectangle(8, 8)
    TILES = list(PENTOMINOS.values()) + [TETROMINOS['Square']]
    problem = TilingProblem(board, TILES)
    problem.solve()
    print(problem.format_output())

