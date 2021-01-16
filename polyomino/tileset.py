from .error import CoverWithWrongSize, CoverWithWrongModulus
from .utils import gcd_list


class Tileset(object):
    def __init__(self, tile_rules):
        self.tile_rules = tile_rules

    @property
    def fixed_rules(self):
        for tile, count in self.tile_rules:
            if count > 0:
                yield tile, count

    @property
    def fixed_total(self):
        return sum(len(tile) * count for tile, count in self.fixed_rules)

    @property
    def flex_rules(self):
        for tile, count in self.tile_rules:
            if count <= 0:
                yield tile, count

    @property
    def flex_gcd(self):
        return gcd_list([len(tile) for tile, count in self.flex_rules])
    
    def check(self, board):
        n = board.count
        r = n - self.fixed_total
        if r < 0:
            raise CoverWithWrongSize(n, self.fixed_total)
        if r > 0 and not list(self.flex_rules):
            raise CoverWithWrongSize(n, self.fixed_total)
        g = self.flex_gcd
        if g != 0 and r % g != 0:
            counts = [len(tile) for tile, count in self.flex_rules]
            raise CoverWithWrongModulus(n, self.fixed_total, counts)

def many(tile):
    return Tileset([(tile, 0)])     
