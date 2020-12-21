from exact_cover_np import get_exact_cover

from polyomino import tiling_to_array
from polyomino.board import Rectangle
from polyomino.constant import PENTOMINOS


if __name__ == '__main__':
    board = Rectangle(8, 8)
    SQUARE = [(0, 0), (1, 0), (1, 1), (0, 1)]
    TILES = list(PENTOMINOS.values()) + [SQUARE]
    key, array = tiling_to_array(TILES, board)
    solution = get_exact_cover(array)
    tiles = [key[s] for s in solution]
    print(board.format_tiling(tiles))

