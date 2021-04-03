import numpy as np

from polyomino.board import Irregular, Rectangle
from polyomino.constant import TETROMINOS
from polyomino.tileset import many


LEFT_CAP_13_HEIGHTS = [0, 1, 0, 1, -1, -1, -1, -1, -1, -2, -1, -2, -1]


def gen_13_cylinder(n):
    for i in range(0, 13):
        h = LEFT_CAP_13_HEIGHTS[i]
        for j in range(h, n + h):
            yield (i, j)


def make_13_cylinder():
    return list(gen_13_cylinder(16))


def test_13_cylinder():
    board = Irregular(make_13_cylinder())
    problem = board.tile_with_many(TETROMINOS["T"])
    solution = problem.solve()
    assert solution is not None


def test_13_cylinder_tileset():
    tileset = many(TETROMINOS["T"])
    assert tileset.mandatory == []
    assert tileset.optional == []
    assert len(tileset.filler) == 1
    assert tileset.reflections is False
    assert tileset.selector_size == 0


def test_13_cylinder_problem():
    board = Irregular(make_13_cylinder())
    problem = board.tile_with_many(TETROMINOS["T"])
    problem.make_problem()
    a = problem.array
    assert a.shape[1] == 16 * 13
    assert 16 * 13 < a.shape[0] < 8 * 16 * 13

    col_sums = np.sum(a, 0)
    assert min(col_sums) == 1
    assert max(col_sums) == 16

    row_sums = np.sum(a, 1)
    assert min(row_sums) == 4
    assert max(row_sums) == 4


def test_13_cylinder_look_for_row():
    board = Irregular(make_13_cylinder())
    problem = board.tile_with_many(TETROMINOS["T"])
    problem.make_problem()
    a = problem.array
    expected = np.array([144, 145, 146, 160])
    assert any([(row.nonzero() == expected).all() for row in a])
    expected = np.array([128, 144, 145, 146])
    assert any([(row.nonzero() == expected).all() for row in a])


def test_4_square():
    board = Rectangle(4, 4)
    problem = board.tile_with_many(TETROMINOS["T"])
    solution = problem.solve()
    assert solution is not None


def test_4_square_with_irregular():
    board = Irregular([(i, j) for i in range(0, 4) for j in range(0, 4)])
    problem = board.tile_with_many(TETROMINOS["T"])
    solution = problem.solve()
    assert solution is not None


def test_12_x_16_with_irregular():
    board = Irregular([(i, j) for i in range(0, 12) for j in range(0, 16)])
    problem = board.tile_with_many(TETROMINOS["T"])
    solution = problem.solve()
    assert solution is not None
