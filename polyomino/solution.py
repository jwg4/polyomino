class Solution(object):
    def __init__(self, tiles, board):
        self.tiles = tiles
        self.board = board

    def display(self):
        return self.board.format_tiling(self.tiles)
