from polyomino.board import Irregular, Rectangle
from polyomino.constant import TETROMINOS


LEFT_CAP_13_HEIGHTS = [
    0, 1, 0, 1, -1, -1, -1, -1, -1, -2, -1, -2, -1
]


def gen_13_cylinder(n):
    for i in range(0, 13):
        h = LEFT_CAP_13_HEIGHTS[i]
        for j in range(h, n + h):
            yield (i, j)
    

def make_13_cylinder():
    return list(gen_13_cylinder(16))


def test_13_cylinder():
    board = Irregular(make_13_cylinder())    
    problem = board.tile_with_many(TETROMINOS['T'])
    solution = problem.solve()
    assert solution is not None


def test_4_square():
    board = Rectangle(4, 4)
    problem = board.tile_with_many(TETROMINOS['T'])
    solution = problem.solve()
    assert solution is not None


def test_4_square_with_irregular():
    board = Irregular([(i, j) for i in range(0, 4) for j in range(0, 4)])
    problem = board.tile_with_many(TETROMINOS['T'])
    solution = problem.solve()
    assert solution is not None


def test_12_x_16_with_irregular():
    board = Irregular([(i, j) for i in range(0, 12) for j in range(0, 16)])
    problem = board.tile_with_many(TETROMINOS['T'])
    solution = problem.solve()
    assert solution is not None
