import pytest

import numpy as np

from hypothesis import example, given, assume, settings
from hypothesis import HealthCheck
from hypothesis.strategies import integers

from polyomino.board import Irregular, Rectangle
from polyomino.constant import DOMINO, MONOMINO, TETROMINOS
from polyomino.error import PolyominoError
from polyomino.tileset import many, Tileset

from .strategies import polyominos


def test_solve_impossible():
    squares = [(0, 0), (0, 1), (1, 1)]
    with pytest.raises(PolyominoError):
        _ = Irregular(squares).tile_with_many(DOMINO)


def test_solve_impossible_not_wrong_modulus():
    squares = [(0, 0), (0, 1), (1, 1), (0, 2)]
    problem = Irregular(squares).tile_with_many(DOMINO)
    solution = problem.solve()
    assert solution is None


def test_solve_impossible_even_to_place_one_tile():
    squares = [(0, 0), (0, 1), (1, 0), (1, 1)]
    problem = Irregular(squares).tile_with_many(TETROMINOS["T"])
    with pytest.raises(PolyominoError):
        _ = problem.solve()


def test_solve_simple():
    squares = [(0, 0), (0, 1), (1, 1), (1, 2)]
    problem = Irregular(squares).tile_with_many(DOMINO)
    solution = problem.solve()
    expected = [[(0, 0), (0, 1)], [(1, 1), (1, 2)]]
    assert solution.tiling == expected


def test_solve_simple_with_negative():
    squares = [(0, -2), (0, -1), (1, -1), (1, 0)]
    problem = Irregular(squares).tile_with_many(DOMINO)
    solution = problem.solve()
    expected = [[(0, -2), (0, -1)], [(1, -1), (1, 0)]]
    assert solution.tiling == expected


def test_solve_simple_tileset_with_0():
    squares = [(0, 0), (0, 1), (1, 1), (1, 2)]
    tileset = many(DOMINO).and_repeated_exactly(0, MONOMINO)
    problem = Irregular(squares).tile_with_set(tileset)
    solution = problem.solve()
    expected = [[(0, 0), (0, 1)], [(1, 1), (1, 2)]]
    assert solution.tiling == expected


def test_solve_one_tile_problem():
    tile = TETROMINOS["T"]
    tileset = many(tile)
    board = Irregular(tile)
    problem = board.tile_with_set(tileset)
    solution = problem.solve()
    assert solution is not None


def test_one_tile_problem_is_correct():
    tile = TETROMINOS["T"]
    tileset = many(tile)
    board = Irregular(tile)
    problem = board.tile_with_set(tileset)
    problem.make_problem()
    a = problem.array
    assert a.shape == (1, 4)


def test_one_tile_problem_is_correct_with_heuristics():
    tile = TETROMINOS["T"]
    tileset = many(tile)
    board = Irregular(tile)
    problem = board.tile_with_set(tileset).with_heuristics()
    problem.make_problem()
    a = problem.array
    assert a.shape == (1, 4)


def test_solve_rotated_one_tile_problem():
    tile = TETROMINOS["T"]
    tileset = many(tile)
    board = Irregular([(1, 0), (0, 1), (1, 1), (1, 2)])
    problem = board.tile_with_set(tileset)
    solution = problem.solve()
    assert solution is not None


def test_rotated_one_tile_problem_is_correct():
    tile = TETROMINOS["T"]
    tileset = many(tile)
    board = Irregular([(1, 0), (0, 1), (1, 1), (1, 2)])
    problem = board.tile_with_set(tileset)
    problem.make_problem()
    a = problem.array
    assert a.shape == (1, 4)


def test_simple_problem_check_array():
    tile = TETROMINOS["T"]
    tileset = many(tile).and_repeated_exactly(3, MONOMINO)
    board = Rectangle(3, 5)
    problem = board.tile_with_set(tileset)
    problem.make_problem()
    a = problem.array
    assert a.shape == (65, 18)
    expected_sums = np.array([2] * 45 + [4] * 20)
    np.testing.assert_array_equal(a.sum(axis=1), expected_sums)


def test_simple_problem_biggest_first_check_array():
    tile = TETROMINOS["T"]
    tileset = many(tile).and_repeated_exactly(3, MONOMINO)
    board = Rectangle(3, 5)
    problem = board.tile_with_set(tileset)
    problem.biggest_pieces_first = True
    problem.make_problem()
    a = problem.array
    assert a.shape == (65, 18)
    expected_sums = np.array([4] * 20 + [2] * 45)
    np.testing.assert_array_equal(a.sum(axis=1), expected_sums)


def test_problem_with_no_mandatory_tiles():
    tileset = Tileset([], ALL_PENTOMINOS, [DOMINO])
    board = Rectangle(20, 20)
    problem = board.tile_with_set(tileset)
    problem.make_problem()
    a = problem.array
    assert a is not None


@settings(deadline=None, suppress_health_check=[HealthCheck.filter_too_much])
@given(integers(2, 10), integers(2, 25), integers(2, 25))
def test_right_number_of_tile_positions(length, x, y):
    assume(length < x and length < y)
    assume(x * y % length == 0)
    tile = [(0, i) for i in range(0, length)]
    tileset = many(tile)
    board = Rectangle(x, y)
    size = x * y
    n_positions = (x - length + 1) * y + x * (y - length + 1)
    problem = board.tile_with_set(tileset)
    problem.make_problem()
    a = problem.array
    assert a.shape == (n_positions, size)


def test_not_a_single_tile_fits():
    tile = [(0, 0), (1, 0), (2, 0), (3, 0)]
    tileset = many(tile)
    board = Rectangle(2, 2)
    with pytest.raises(PolyominoError):
        problem = board.tile_with_set(tileset)
        problem.make_problem()


@settings(deadline=None, suppress_health_check=[HealthCheck.filter_too_much])
@example([(0, 0), (1, 0), (2, 0), (3, 0)], 2, 2)
@given(polyominos, integers(2, 15), integers(2, 15))
def test_not_too_many_tile_positions(tile, x, y):
    assume(x * y % len(tile) == 0)
    tileset = many(tile)
    rectangle = Rectangle(x, y)
    board = Irregular(set(rectangle.squares + tile))
    assume(len(board.squares) % len(tile) == 0)
    expected_size = x * y
    max_positions = 4 * expected_size
    problem = board.tile_with_set(tileset)
    problem.make_problem()
    a = problem.array
    n_positions, size = a.shape
    assert size == expected_size
    assert n_positions <= max_positions


@given(polyominos)
def test_solve_arbitrary_one_tile_problem(tile):
    tile = TETROMINOS["T"]
    tileset = many(tile)
    board = Irregular(tile)
    problem = board.tile_with_set(tileset)
    solution = problem.solve()
    assert solution is not None


@given(polyominos)
def test_solve_arbitrary_two_tile_problem(tile):
    tile = TETROMINOS["T"]
    tileset = many(tile)
    board = Irregular(tile + [(x, y + 100) for x, y in tile])
    problem = board.tile_with_set(tileset)
    solution = problem.solve()
    assert solution is not None
