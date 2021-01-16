from .error import CoverWithWrongSize, CoverWithWrongModulus
from .utils import gcd_list


class Tileset(object):
    def __init__(self, mandatory, optional, filler):
        self.mandatory = mandatory  # exactly 1
        self.optional = optional    # either 1 or 0
        self.filler = filler        # any nonnegative number

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


def many(tile):
    return Tileset([], [], [tile])     


def exactly(tiles):
    return Tileset(tiles, [], [])     
