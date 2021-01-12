from polyomino.board import Rectangle, Irregular


def test_remove_from_rectangle():
    board = Rectangle(2, 3)
    assert set(board.squares) == set([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)])
    trimmed = board.remove((1, 1))
    assert set(trimmed.squares) == set([(0, 0), (1, 0), (0, 1), (0, 2), (1, 2)])


def test_remove_from_irregular():
    squares = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)]
    board = Irregular(squares)
    assert set(board.squares) == set(squares)
    trimmed = board.remove((1, 3))
    assert set(trimmed.squares) == set([(0, 0), (0, 1), (1, 1), (1, 2)])
