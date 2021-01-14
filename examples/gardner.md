These examples are taken from chapter 13 of 'Mathematical Puzzles and Diversions' by Martin Gardner.

>>> from polyomino.board import Chessboard, Rectangle
>>> from polyomino.constant import DOMINO


> ...
> In Chapter 3 (problem 3) we considered a polyomino problem dealing with the placing of dominoes on a mutilated chessboard.

(We can't solve this problem within a doctest because it takes too long.)
>>> Chessboard().remove((0, 0)).remove((7, 7)).tile_with_many(DOMINO)
<polyomino.problem.TilingProblem object at ...>

>>> Rectangle(4, 4).remove((0, 0)).remove((3, 3)).tile_with_many(DOMINO).solve()

>>> Chessboard().remove((0, 0)).remove((0, 7)).tile_with_many(DOMINO).solve().tiles
[[(0, 1), (0, 2)], [(0, 3), (0, 4)], [(0, 5), (0, 6)], [(1, 0), (1, 1)], [(1, 2), (1, 3)], [(1, 4), (1, 5)], [(1, 6), (1, 7)], [(2, 0), (2, 1)], [(2, 2), (2, 3)], [(2, 4), (2, 5)], [(2, 6), (2, 7)], [(3, 0), (3, 1)], [(3, 2), (3, 3)], [(3, 4), (3, 5)], [(3, 6), (3, 7)], [(4, 0), (4, 1)], [(4, 2), (4, 3)], [(4, 4), (4, 5)], [(4, 6), (4, 7)], [(5, 0), (5, 1)], [(5, 2), (5, 3)], [(5, 4), (5, 5)], [(5, 6), (5, 7)], [(6, 0), (6, 1)], [(7, 0), (7, 1)], [(6, 2), (6, 3)], [(7, 2), (7, 3)], [(6, 4), (6, 5)], [(7, 4), (7, 5)], [(6, 6), (6, 7)], [(7, 6), (7, 7)]]

