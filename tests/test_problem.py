from polyomino.board import Irregular
from polyomino.constant import DOMINO


def test_solve_simple():
    squares = [(0, 0), (0, 1), (1, 1), (1, 2)]
    problem = Irregular(squares).tile_with_many(DOMINO)
    solution = problem.solve()
    expected = [[(0, 0), (0, 1)], [(1, 1), (1, 2)]]
    assert solution == expected
