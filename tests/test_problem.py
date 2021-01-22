import pytest

from polyomino.board import Irregular
from polyomino.constant import DOMINO, MONOMINO, TETROMINOS
from polyomino.error import PolyominoError
from polyomino.tileset import many


def test_solve_impossible():
    squares = [(0, 0), (0, 1), (1, 1)]
    with pytest.raises(PolyominoError):
        problem = Irregular(squares).tile_with_many(DOMINO)


def test_solve_impossible_not_wrong_modulus():
    squares = [(0, 0), (0, 1), (1, 1), (0, 2)]
    problem = Irregular(squares).tile_with_many(DOMINO)
    solution = problem.solve()
    assert solution == None


def test_solve_impossible_even_to_place_one_tile():
    squares = [(0, 0), (0, 1), (1, 0), (1, 1)]
    problem = Irregular(squares).tile_with_many(TETROMINOS['T'])
    with pytest.raises(PolyominoError):
        solution = problem.solve()


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
