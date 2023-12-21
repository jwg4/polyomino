from collections import defaultdict

from .board import Irregular

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


def display(piece):
    board = Irregular(piece)

    return board.format_tiling([piece])
