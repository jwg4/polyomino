import numpy as np

from exact_cover import get_exact_cover
from exact_cover.error import NoSolution

from .error import CantPlaceSinglePiece
from .solution import Solution


def tiling_to_problem(tileset, shape):
    key = []
    data = []
    for tile, selector, optional in tileset.vectors():
        for translated in shape.positions(tile, tileset.reflections):
            key.append(translated)
            vector = np.concatenate([selector, shape.bit_vector(translated)])
            data.append(vector)
        if optional:
            key.append([])
            vector = np.concatenate([selector, shape.bit_vector([])])
            data.append(vector)
    return key, data


def tiling_to_array(tileset, shape):
    key, data = tiling_to_problem(tileset, shape)
    array = np.array(data, dtype=np.int32)
    return key, array


def tiling_to_array_order_biggest(tileset, shape):
    key, array = tiling_to_array(tileset, shape)
    row_sums = array.sum(axis=1) * -1
    sort_args = np.argsort(row_sums)
    sorted_array = array[sort_args, :]
    sorted_key = [key[i] for i in sort_args]
    return sorted_key, sorted_array


class TilingProblem(object):
    biggest_pieces_first = False
    _name = ""
    array = None
    key = None

    def __init__(self, board, tileset):
        self.board = board
        self.tileset = tileset

    def make_problem(self):
        if self.array is not None and self.key is not None:
            return
        if self.biggest_pieces_first:
            self.key, self.array = tiling_to_array_order_biggest(
                self.tileset, self.board
            )
        else:
            self.key, self.array = tiling_to_array(self.tileset, self.board)
        if self.array.ndim < 2:
            raise CantPlaceSinglePiece(self.board, self.tileset)

    def solve(self):
        self.make_problem()
        try:
            solution = get_exact_cover(self.array)
        except NoSolution:
            return None
        tiling = [self.key[s] for s in solution]
        if tiling:
            return Solution(tiling, self.board)

    def with_heuristics(self):
        self.biggest_pieces_first = True
        return self

    def output_array(self, filename):
        self.make_problem()
        np.savetxt(filename, self.array, fmt="%d", header=self.header)

    def set_name(self, name):
        self._name = name

    @property
    def size(self):
        self.make_problem()
        return self.array.shape

    @property
    def name(self):
        if self._name:
            return self._name
        else:
            return "Tiling problem"

    @property
    def header(self):
        x, y = self.size
        return "%s, %d x %d" % (self.name, x, y)
