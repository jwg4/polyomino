import numpy as np

from polyomino.board import Chessboard
from polyomino.constant import TETROMINOS
from polyomino.constant import ALL_PENTOMINOS


def test_output_problem_array():
    result_filename = "tests/files/output/pentominos_chessboard.csv"
    expected_filename = "tests/files/expected/pentominos_chessboard.csv"

    tiles = ALL_PENTOMINOS + [TETROMINOS["Square"]]
    problem = Chessboard().tile_with(tiles)
    problem.set_name("Pentominos + square on chessboard")
    problem.output_array(result_filename)

    with open(result_filename) as f:
        result = f.read()
    with open(expected_filename) as f:
        expected = f.read()

    assert result == expected


def test_output_problem_array_round_trip():
    result_filename = "tests/files/output/pentominos_chessboard.csv"

    tiles = ALL_PENTOMINOS + [TETROMINOS["Square"]]
    problem = Chessboard().tile_with(tiles)
    problem.output_array(result_filename)

    result = np.genfromtxt(result_filename)
    np.testing.assert_array_equal(result, problem.array)
