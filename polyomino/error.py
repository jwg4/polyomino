class PolyominoError(Exception):
    pass


class CoverWithWrongSize(PolyominoError):
    def __init__(self, board_size, cover_size):
        self.board_size = board_size
        self.cover_size = cover_size


class CoverWithWrongModulus(PolyominoError):
    def __init__(self, board_size, fixed_size, gcd):
        self.board_size = board_size
        self.fixed_size = fixed_size
        self.gcd = gcd


class CantPlaceSinglePiece(PolyominoError):
    def __init__(self, board, tileset):
        self.board = board
        self.tileset = tileset
