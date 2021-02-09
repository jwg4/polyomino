class Solution(object):
    def __init__(self, tiling, board):
        self.tiling = tiling
        self.board = board

    def display(self):
        return self.board.format_tiling(self.tiling)

    def python(self):
        return "\n".join(self._gen_python())

    def _gen_python(self):
        yield "TILING = %s" % (repr(self.tiling), )
