import numpy as np

from exact_cover import get_exact_cover

from .error import CantPlaceSinglePiece
from .solution import Solution


def tiling_to_problem(tileset, shape):
    key = []
    data = []
    for tile, selector, optional in tileset.vectors():
        for translated in shape.positions(tile, tileset.reflections):
            key.append(translated)
            vector = selector + shape.bit_vector(translated)
            data.append(vector)
        if optional:
            key.append([])
            vector = selector + shape.bit_vector([])
            data.append(vector)
    return key, data


def tiling_to_array(tileset, shape):
    key, data = tiling_to_problem(tileset, shape)
    array = np.array(data, dtype=np.int32)
    return key, array


class TilingProblem(object):
    def __init__(self, board, tileset):
        self.board = board
        self.tileset = tileset

    def make_problem(self):
        self.key, self.array = tiling_to_array(self.tileset, self.board)

    def solve(self):
        self.make_problem() 
        if self.array.ndim < 2:
            raise CantPlaceSinglePiece(self.board, self.tileset)
        solution = get_exact_cover(self.array)
        tiling = [self.key[s] for s in solution]
        if tiling:
            return Solution(tiling, self.board)
