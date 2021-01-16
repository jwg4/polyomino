from .error import CoverWithWrongSize, CoverWithWrongModulus
from .utils import gcd_list


class Tileset(object):
    def __init__(self, mandatory, optional, filler, reflections=False):
        self.mandatory = mandatory  # exactly 1
        self.optional = optional    # either 1 or 0
        self.filler = filler        # any nonnegative number
        self.reflections = reflections

    @property
    def fixed_total(self):
        return sum(len(tile) for tile in self.mandatory)

    @property
    def optional_total(self):
        return sum(len(tile) for tile in self.optional)

    @property
    def max_total(self):
        return self.fixed_total + self.optional_total

    @property
    def selector_size(self):
        return len(self.mandatory) + len(self.optional)

    @property
    def flex_gcd(self):
        return gcd_list(
            [len(tile) for tile in self.optional] + 
            [len(tile) for tile in self.filler]
        )
    
    def check(self, board):
        n = board.count
        if self.fixed_total > n:
            raise CoverWithWrongSize(n, self.fixed_total)
        if not self.filler:
            if self.max_total < n:
                raise CoverWithWrongSize(n, self.fixed_total)
        
        r = n - self.fixed_total
        g = self.flex_gcd
        if r != 0 and r % g != 0:
            raise CoverWithWrongModulus(n, self.fixed_total, g)

    def selector_vector(self, i):
        return [i == j for j in range(0, self.selector_size)]

    def empty_vector(self):
        return [False] * self.selector_size
 
    def vectors(self):
        i = 0
        for tile in self.mandatory:
            selector = self.selector_vector(i)
            yield tile, selector, False
            i = i + 1
        for tile in self.optional:
            selector = self.selector_vector(i)
            yield tile, selector, True
            i = i + 1
        for tile in self.filler:
            selector = self.empty_vector()
            yield tile, selector, False

    def and_repeated_exactly(self, count, tile):
        mandatory = self.mandatory + [tile] * count
        return Tileset(mandatory, self.optional, self.filler)

    def and_one(self, tile):
        return self.and_repeated_exactly(1, tile)

    def with_reflections(self):
        return Tileset(self.mandatory, self.optional, self.filler, True)


def many(tile):
    return Tileset([], [], [tile])     


def exactly(tiles):
    return Tileset(tiles, [], [])     


def repeated_exactly(count, tile):
    return Tileset([tile] * count, [], [])


def any_number_of(tiles):
    return Tileset([], [], tiles)
