import pytest

from polyomino.board import Rectangle, Irregular


def test_remove_from_rectangle():
    board = Rectangle(2, 3)
    assert set(board.squares) == set([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)])
    trimmed = board.remove((1, 1))
    assert set(trimmed.squares) == set([(0, 0), (1, 0), (0, 1), (0, 2), (1, 2)])


def test_error_if_removing_not_present():
    board = Rectangle(2, 3)
    assert set(board.squares) == set([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)])
    with pytest.raises(Exception):
        board.remove((2, 4))


def test_remove_from_irregular():
    squares = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)]
    board = Irregular(squares)
    assert set(board.squares) == set(squares)
    trimmed = board.remove((1, 3))
    assert set(trimmed.squares) == set([(0, 0), (0, 1), (1, 1), (1, 2)])


def test_remove_from_irregular_gen():
    squares = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)]

    def gen_sq():
        for sq in squares:
            yield sq

    board = Irregular(gen_sq())
    assert set(board.squares) == set(squares)
    trimmed = board.remove((1, 3))
    assert set(trimmed.squares) == set([(0, 0), (0, 1), (1, 1), (1, 2)])


def test_tile_with_many_size_check():
    board = Rectangle(8, 8).remove((0, 0))
    with pytest.raises(Exception):
        board.tile_with_many([(0, 0), (1, 0)])


def test_adjusted_square_irregular():
    squares = [(3, -2), (3, -1), (4, -1), (4, 0), (4, 1)]
    board = Irregular(squares)
    expected = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)]
    assert board.adjusted == expected
