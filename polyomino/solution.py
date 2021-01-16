class Solution(object):
    def __init__(self, tiling, board):
        self.tiling = tiling
        self.board = board

    def display(self):
        return self.board.format_tiling(self.tiling)
