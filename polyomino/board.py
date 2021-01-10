import numpy as np

from .transform import rotate


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
