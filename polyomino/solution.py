from pretty_poly import make_ascii


class Solution(object):
    def __init__(self, tiling, board):
        self.tiling = tiling
        self.board = board

    def display(self):
        return make_ascii(self.tiling)

    def python(self):
        return "\n".join(self._gen_python())

    def _gen_python(self):
        yield "TILING = %s" % (repr(self.tiling),)
