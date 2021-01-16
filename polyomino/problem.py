import numpy as np

from exact_cover import get_exact_cover

from .solution import Solution


def selector_vector(n, i):
    return [i == j for j in range(0, n)]


def tiling_to_problem(tiles, shape):
    raise NotImplementedError()
    n = len(tiles)
    key = []
    data = []
    for i, tile in enumerate(tiles):
        selector = selector_vector(n, i)
        for translated in shape.positions(tile):
            key.append(translated)
            vector = selector + shape.bit_vector(translated)
            data.append(vector)
    return key, data


def tiling_to_array(tiles, shape):
    key, data = tiling_to_problem(tiles, shape)
    array = np.array(data, dtype=np.int32)
    return key, array


class TilingProblem(object):
    def __init__(self, board, tileset):
        self.board = board
        self.tileset = tileset

    def solve(self):
        key, array = tiling_to_array(self.tileset, self.board)
        solution = get_exact_cover(array)
        tiling = [key[s] for s in solution]
        if tiling:
            return Solution(tiling, self.board)
