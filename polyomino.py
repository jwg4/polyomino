import numpy as np

from exact_cover_np import get_exact_cover


PENTOMINOS = {
    'F': [(0, 1), (1, 0), (1, 1), (2, 1), (2, 2)],
    'I': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
    'L': [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)],
    'N': [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)],
    'P': [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)],
    'T': [(0, 1), (1, 1), (2, 0), (2, 1), (2, 2)],
    'U': [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)],
    'V': [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)],
    'W': [(0, 2), (0, 1), (1, 1), (1, 0), (2, 0)],
    'X': [(0, 1), (1, 0), (1, 1), (2, 1), (1, 2)],
    'Y': [(0, 2), (1, 0), (1, 1), (1, 2), (1, 3)],
    'Z': [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]
}


class Rectangle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def squares(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                yield (i, j)

    def is_in(self, square):
        return 0 <= square[0] < self.x and 0 <= square[1] < self.y

    def is_contained(self, tile):
        return all(self.is_in(sq) for sq in tile)

    def positions(self, tile):
        reference = tile[0]
        for sq in self.squares:
            for rotated in rotate(tile):
                translated = [
                    (x - reference[0] + sq[0], y - reference[1] + sq[1])
                    for x, y in rotated
                ]
                if self.is_contained(translated):
                    yield translated

    def bit_vector(self, tile):
        return [sq in tile for sq in self.squares]

    def format_row_sides(self, row):
        return " ".join("|" if r else " " for r in row)

    def format_row_upper(self, row):
        return "+" + "+".join("-" if r else " " for r in row) + "+"

    def format_tiling_lines(self, h, v):
        for i in range(0, self.y):
            yield self.format_row_upper(h[i])
            yield self.format_row_sides(v[i])
        yield self.format_row_upper(h[self.y])

    def calculate_tiling(self, tiling):
        h = [[True] * self.x for i in range(0, self.y + 1)]
        v = [[True] * (self.x + 1) for i in range(0, self.y)]

        for tile in tiling:
            for sq_a in tile:
                for sq_b in tile:
                    a, b = sorted([sq_a, sq_b])
                    if (a[1] == b[1]) and (a[0] + 1 == b[0]):
                        v[a[1]][b[0]] = False
                        pass
                    if (a[0] == b[0]) and (a[1] + 1 == b[1]):
                        h[b[1]][a[0]] = False
        
        return h, v

    def format_tiling(self, tiling):
        h, v = self.calculate_tiling(tiling)
        return "\n".join(self.format_tiling_lines(h, v))


def rotate(tile):
    s = set()
    for m in [[[1, 0], [0, 1]], [[0, -1], [1, 0]], [[-1, 0], [0, -1]], [[0, 1], [-1, 0]]]:
        rotated = [
            (m[0][0] * t[0] + m[0][1] * t[1], m[1][0] * t[0] + m[1][1] * t[1])
            for t in tile
        ]
        mx = min(s[0] for s in rotated)
        my = min(s[1] for s in rotated)
        shifted = [(t[0] - mx, t[1] - my) for t in rotated]
        shifted.sort()
        if tuple(shifted) not in s:
            yield shifted
            s.add(tuple(shifted))


def selector_vector(n, i):
    return [i == j for j in range(0, n)]


def tiling_to_problem(tiles, shape):
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


if __name__ == '__main__':
    board = Rectangle(8, 8)
    SQUARE = [(0, 0), (1, 0), (1, 1), (0, 1)]
    TILES = list(PENTOMINOS.values()) + [SQUARE]
    key, array = tiling_to_array(TILES, board)
    solution = get_exact_cover(array)
    tiles = [key[s] for s in solution]
    print(board.format_tiling(tiles))

