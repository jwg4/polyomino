## Examples of fluid syntax to construct problems

>>> from polyomino.board import Chessboard
>>> from polyomino.constant import MONOMINO, DOMINO
>>> from polyomino.tileset import many

>>> Chessboard()
<polyomino.board.Chessboard object at ...>

>>> Chessboard().tile_with_many(DOMINO)
<polyomino.problem.TilingProblem object at ...>

>>> Chessboard().tile_with_set(many(DOMINO).and_exactly(2, MONOMINO))
<polyomino.problem.TilingProblem object at ...>
