from polyomino.board import Rectangle
from polyomino.error import CantPlaceSinglePiece


def rectangles(size):
    """
        >>> list(rectangles(20):
        [(1, 20), (2, 10), (4, 5)]
        >>> list(rectangles(16):
        [(1, 16), (2, 8), (4, 6)]
    """
    for i in range(1, size):
        if size % i == 0:
            yield i, size // i


def has_order_greater_than(tile, k):
    n = len(tile)

    for i in range(1, k + 1):
        for x, y in rectangles(n * i):
            board = Rectangle(x, y)
            problem = board.tile_with_many(tile)
            try:
                solution = problem.solve()
                if solution:
                    return False, i, solution.tiling
            except CantPlaceSinglePiece:
                pass

    return True, None, None
