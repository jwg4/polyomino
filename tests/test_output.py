import csv

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


def test_output_problem_array_explicit_numpy():
    result_filename = "tests/files/output/pentominos_chessboard.csv"
    expected_filename = "tests/files/expected/pentominos_chessboard.csv"

    tiles = ALL_PENTOMINOS + [TETROMINOS["Square"]]
    problem = Chessboard().tile_with(tiles)
    problem.set_name("Pentominos + square on chessboard")
    problem.output_array(result_filename, numpy=True)

    with open(result_filename) as f:
        result = f.read()
    with open(expected_filename) as f:
        expected = f.read()

    assert result == expected


def test_output_problem_array_round_trip_explicit_numpy():
    result_filename = "tests/files/output/pentominos_chessboard.csv"

    tiles = ALL_PENTOMINOS + [TETROMINOS["Square"]]
    problem = Chessboard().tile_with(tiles)
    problem.output_array(result_filename, numpy=True)

    result = np.genfromtxt(result_filename)
    np.testing.assert_array_equal(result, problem.array)


def test_output_problem_array_not_numpy():
    result_filename = "tests/files/output/pentominos_chessboard_vanilla.csv"
    expected_filename = "tests/files/expected/pentominos_chessboard_vanilla.csv"

    tiles = ALL_PENTOMINOS + [TETROMINOS["Square"]]
    problem = Chessboard().tile_with(tiles)
    problem.set_name("Pentominos + square on chessboard")
    problem.output_array(result_filename, numpy=False)

    with open(result_filename) as f:
        result = f.read()
    with open(expected_filename) as f:
        expected = f.read()

    assert result == expected


def test_output_problem_array_round_trip_not_numpy():
    def read_csv(filename):
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            return [[int(x) for x in row] for row in reader]

    result_filename = "tests/files/output/pentominos_chessboard.csv"

    tiles = ALL_PENTOMINOS + [TETROMINOS["Square"]]
    problem = Chessboard().tile_with(tiles)
    problem.output_array(result_filename, numpy=False)

    result = read_csv(result_filename)
    np.testing.assert_array_equal(result, problem.array)
