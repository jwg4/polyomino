TETROMINOES = '''
IIII  LLL  OO  TTT  ZZ
      L    OO   T    ZZ
'''

PENTOMINOES = '''
I
I     L      N                      Y
I  FF L  PP  N TTT       V   W  X  YY ZZ
I FF  L  PP NN  T  U U   V  WW XXX  Y  Z
I  F  LL P  N   T  UUU VVV WW   X   Y  ZZ
'''

from collections import defaultdict

_EMPTY = ' '

def decode_pieces(picture):
    """Given a "picture" of some polyominoes (in ASCII-art form), return a
    list of tuples (name, tiles) for each polyomino, where tiles are
    the coordinates (i, j) of its tiles.

    >>> sorted(decode_pieces(TETROMINOES))
    ... # doctest: +NORMALIZE_WHITESPACE
    [('I', ((1, 0), (1, 1), (1, 2), (1, 3))),
     ('L', ((1, 6), (1, 7), (1, 8), (2, 6))),
     ('O', ((1, 11), (1, 12), (2, 11), (2, 12))),
     ('T', ((1, 15), (1, 16), (1, 17), (2, 16))),
     ('Z', ((1, 20), (1, 21), (2, 21), (2, 22)))]

    """
    pieces = defaultdict(list)
    for i, row in enumerate(picture.split('\n')):
        for j, c in enumerate(row):
            if c != _EMPTY:
                pieces[c].append((i, j))
    return [(c, tuple(tiles)) for c, tiles in pieces.items()]

def solution_tiles(solution):
    """Generate all the tiles in a polyomino solution."""
    return (t for _, tiles in solution for t in tiles)

def solution_bounds(solution):
    """Return the bounds of the region covered by a polyomino solution."""
    h, w = map(max, zip(*solution_tiles(solution)))
    return h + 1, w + 1

def solution_string(solution):
    """Format a polyomino solution as a string."""
    h, w = solution_bounds(solution)
    grid = [[_EMPTY] * w for _ in range(h)]
    for c, tiles in solution:
        for i, j in tiles:
            grid[i][j] = c
    return '\n'.join(''.join(row) for row in grid)

from exactcover import ExactCover
from itertools import product

def polyomino(pieces, region, random=False):
    """Return an iterator that yields the solutions to a polyomino tiling
    problem.

    Required arguments:
    pieces -- an iterable of pieces, each being a tuple whose first
        element is the name of the piece and whose second element is a
        sequence of coordinates of the tiles in the piece (in an
        arbitrary coordinate system).
    region -- the region to fill (an iterable of coordinates x, y).

    Optional argument:
    random -- Generate solutions in random order? (Default: False.)

    >>> region = set(product(range(3), range(7))) - {(1, 2)}
    >>> sol = min(polyomino(decode_pieces(TETROMINOES), region))
    >>> print(solution_string(sol))
    OOTTTZZ
    OO TZZL
    IIIILLL

    """
    region = list(region)
    region_set = set(region)
    constraints = {}
    for c, tiles in pieces:
        # Origin of piece at the first tile.
        oi, oj = tiles[0]
        # Adjust tiles so that they are relative to the origin of the piece.
        tiles = [(ti - oi, tj - oj) for ti, tj in tiles]
        for (oi, oj), ri, rj, rk in product(region, (-1, +1), (-1, +1), (0, 1)):
            # Place origin of piece at oi, oj, reflecting vertically
            # if ri == -1, horizontally if rj == -1, and diagonally if
            # rk == 1.
            placing = []
            for t in tiles:
                p = ri * t[rk] + oi, rj * t[1-rk] + oj
                if p not in region_set:
                    break
                placing.append(p)
            else:
                placing = tuple(sorted(placing))
                choice = c, placing
                if choice not in constraints:
                    constraints[choice] = (c,) + placing
    return ExactCover(constraints=constraints, random=random)

from svgwrite import Drawing

def solutions_svg(solutions, filename, columns=1, size=25, padding=5,
                  colour=lambda _: "white", stroke_colour="black",
                  stroke_width=3):
    """Format polyomino tilings as an SVG image.

    Required arguments:
    solutions -- iterable of solutions to the tiling problem, each of
        which is a sequence of piece placements, each of which is a
        tuple whose first element is the name of the piece, and whose
        second element is a sequence of pairs (i, j) giving the
        locations of the tiles in the piece.
    filename -- where to save the SVG drawing.

    Optional arguments:
    columns -- number of solutions per row (default: 1).
    size -- width and height of each tile (default: 25).
    padding -- padding around the image (default: 5)
    colour -- function taking a piece name and returning its colour
        (default: a function returning white for each piece).
    stroke -- stroke colour (default: black).
    stroke_width -- width of strokes between pieces (default: 3).

    """
    solutions = list(solutions)
    h, w = solution_bounds(solutions[0])
    rows = (len(solutions) + columns - 1) // columns
    drawing_size = (2 * padding + (columns * (w + 1) - 1) * size,
                    2 * padding + (rows    * (h + 1) - 1) * size)
    drawing = Drawing(debug=False, filename=filename, size=drawing_size)
    for i, solution in enumerate(solutions):
        y, x = divmod(i, columns)
        oj = padding + (x * (w + 1)) * size
        oi = padding + (y * (h + 1)) * size
        group = drawing.g(stroke=stroke_colour, stroke_linecap="round",
                          stroke_width=0.25)
        drawing.add(group)
        grid = [[_EMPTY] * w for _ in range(h)]
        for c, placing in solution:
            piece = drawing.g(fill=colour(c))
            group.add(piece)
            for i, j in placing:
                grid[i][j] = c
                piece.add(drawing.rect((j * size + oj, i * size + oi),
                                       (size, size)))
        edges = drawing.path(stroke_width=stroke_width)
        group.add(edges)
        for i, j in product(range(h + 1), range(w)):
            if ((_EMPTY if i == 0 else grid[i-1][j])
                != (_EMPTY if i == h else grid[i][j])):
                edges.push(['M', j * size + oj, i * size + oi, 'l', size, 0])
        for i, j in product(range(h), range(w + 1)):
            if ((_EMPTY if j == 0 else grid[i][j-1])
                != (_EMPTY if j == w else grid[i][j])):
                edges.push(['M', j * size + oj, i * size + oi, 'l', 0, size])
    drawing.save()

# Colours by R. A. Nonenmacher from
# https://en.wikipedia.org/wiki/File:Pentomino_Naming_Conventions.svg

COLOURS = dict(I="#EEAAAA", F="#DDBB99", L="#CCCC88",
               P="#BBDD99", N="#AAEEAA", T="#99DDBB",
               U="#88CCCC", V="#99BBDD", W="#AAAAEE",
               X="#BB99DD", Y="#CC88CC", Z="#DD99BB")

COMPACT_PENTOMINOES = '''
 I       L      N
 I   FF  L  PP  N TTT
 I  FF   L  PP NN  T
 I   F   LL P  N   T
 I               Y
      V   W  X  YY ZZ
U U   V  WW XXX  Y  Z
UUU VVV WW   X   Y  ZZ
'''

def build_article():
    pieces = decode_pieces(COMPACT_PENTOMINOES.strip('\n'))
    solutions_svg([pieces], 'pentominoes.svg', colour=COLOURS.get)

from itertools import starmap

def canonical(solution):
    """Return a canonical version of a polyomino tiling solution."""
    h, w = solution_bounds(solution)
    all_tiles = sorted(solution_tiles(solution))
    orientations = [(False, True)] * 3
    if sorted((h - i - 1, j) for i, j in all_tiles) != all_tiles:
        # Can't reflect vertically.
        orientations[0] = (False,)
    if sorted((i, w - j - 1) for i, j in all_tiles) != all_tiles:
        # Can't reflect horizontally.
        orientations[1] = (False,)
    if sorted((j, i) for i, j in all_tiles) != all_tiles:
        # Can't reflect diagonally.
        orientations[2] = (False,)
    solution = sorted(solution)
    def oriented(ri, rj, rk):
        oriented_solution = []
        for c, tiles in solution:
            oriented_tiles = []
            for i, j in tiles:
                if ri: i = h - i - 1 # reflect vertically
                if rj: j = w - j - 1 # reflect horizontally
                if rk: i, j = j, i   # reflect diagonally
                oriented_tiles.append((i, j))
            oriented_solution.append((c, tuple(sorted(oriented_tiles))))
        return tuple(oriented_solution)
    return min(starmap(oriented, product(*orientations)))
