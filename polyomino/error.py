class PolyominoError(Exception):
    pass


class CoverWithWrongSize(PolyominoError):
    def __init__(self, board_size, cover_size):
        self.board_size = board_size
        self.cover_size = cover_size


class CoverWithWrongModulus(PolyominoError):
    def __init__(self, board_size, fixed_size, counts):
        self.board_size = board_size
        self.cover_size = fixed_size
        self.counts = counts
