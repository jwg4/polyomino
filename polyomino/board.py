import numpy as np

from pretty_poly import make_ascii

from .jupyter import board_to_png
from .problem import TilingProblem
from .tileset import exactly, many
from .transform import rotations


class Shape(object):
    bit_masks = None

    def is_contained(self, tile):
        return all(self.is_in(sq) for sq in tile)

    @property
    def count(self):
        return len(self.squares)

    def positions(self, tile, with_reflections=False):
        for sq in self.squares:
            for rotated in rotations(tile, with_reflections):
                reference = rotated[0]
                translated = [
                    (x - reference[0] + sq[0], y - reference[1] + sq[1])
                    for x, y in rotated
                ]
                if self.is_contained(translated):
                    yield translated

    def bit_vector(self, tile):
        if not tile:
            return self.bit_mask(None)
        return np.sum([self.bit_mask(sq) for sq in tile], axis=0)

    def bit_mask(self, sq):
        if not self.bit_masks:
            self.bit_masks = dict()
        if sq not in self.bit_masks:
            self.bit_masks[sq] = np.array(
                [s == sq for s in self.squares], dtype=np.int32
            )
        return self.bit_masks[sq]

    def remove(self, square):
        if square not in self.squares:
            raise Exception(
                "Tried to remove a square %s which was not present in the board"
                % (square,)
            )
        return Irregular([sq for sq in self.squares if sq != square])

    def remove_all(self, squares):
        for square in squares:
            if square not in self.squares:
                raise Exception(
                    "Tried to remove a square %s which was not present in the board"
                    % (square,)
                )
        return Irregular([sq for sq in self.squares if sq not in squares])

    def tile_with(self, tiles):
        return self.tile_with_set(exactly(tiles))

    def tile_with_many(self, tile):
        return self.tile_with_set(many(tile))

    def tile_with_set(self, tileset):
        tileset.check(self)
        return TilingProblem(self, tileset)

    def display(self):
        return make_ascii([self.squares])

    def format_tiling(self, pieces):
        squares_in_pieces = (sq for piece in pieces for sq in piece)
        remainder = set(self.squares) - set(squares_in_pieces)
        return make_ascii(pieces + [remainder])

    def _repr_png_(self):
        return board_to_png(self)


class Irregular(Shape):
    _adjusted = None

    def __init__(self, squares):
        self._squares = list(squares)
        self.min_x = min(x for x, y in self.squares)
        self.min_y = min(y for x, y in self.squares)
        self.max_x = max(x for x, y in self.squares)
        self.max_y = max(y for x, y in self.squares)

    @property
    def squares(self):
        return self._squares

    @property
    def adjusted(self):
        if self._adjusted is None:
            self._adjusted = [(x - self.min_x, y - self.min_y) for x, y in self.squares]
        return self._adjusted

    def is_in(self, square):
        return square in self._squares


class DeletedRectangle(Irregular):
    def __init__(self, whole, deleted):
        self.whole = whole
        self.deleted = deleted
        super().__init__([sq for sq in self.whole.squares if not sq in self.deleted])

    def remove(self, square):
        if square not in self.squares:
            raise Exception(
                "Tried to remove a square %s which was not present in the board"
                % (square,)
            )
        return DeletedRectangle(self.whole, self.deleted + [square])

    def remove_all(self, squares):
        for square in squares:
            if square not in self.squares:
                raise Exception(
                    "Tried to remove a square %s which was not present in the board"
                    % (square,)
                )
        return DeletedRectangle(self.whole, self.deleted + squares)

    @property
    def interior_deleted(self):
        return (
            (x, y)
            for x, y in self.deleted
            if x > self.min_x and x < self.max_x and y > self.min_y and y < self.max_y
        )

    def format_row_sides(self, row, row_y):
        line = list(super().format_row_sides(row))
        for x, y in self.interior_deleted:
            if y == row_y:
                line[2 * x + 1] = "X"
        return "".join(line)

    def format_tiling_lines(self, h, v):
        for i in range(self.min_y, self.max_y + 1):
            yield self.format_row_upper(h[i])
            yield self.format_row_sides(v[i - self.min_y], i)
        yield self.format_row_upper(h[self.max_y - self.min_y + 1])


class Rectangle(Shape):
    _squares_cache = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def squares(self):
        if self._squares_cache is None:
            self._squares_cache = list(self.gen_squares())
        return self._squares_cache

    def gen_squares(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                yield (i, j)

    def is_in(self, square):
        return 0 <= square[0] < self.x and 0 <= square[1] < self.y

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

    def remove(self, square):
        if square not in self.squares:
            raise Exception(
                "Tried to remove a square %s which was not present in the board"
                % (square,)
            )
        return DeletedRectangle(self, [square])

    def remove_all(self, squares):
        for square in squares:
            if square not in self.squares:
                raise Exception(
                    "Tried to remove a square %s which was not present in the board"
                    % (square,)
                )
        return DeletedRectangle(self, squares)


class Chessboard(Rectangle):
    x = 8
    y = 8

    def __init__(self):
        pass
