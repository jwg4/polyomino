These examples are taken from chapter 13 of 'Mathematical Puzzles and Diversions' by Martin Gardner.

>>> from polyomino.board import Chessboard
>>> from polyomino.constant import DOMINO


> ...
> In Chapter 3 (problem 3) we considered a polyomino problem dealing with the placing of dominoes on a mutilated chessboard.

>>> Chessboard().remove((0, 0)).remove((7, 7)).tile_with_many(DOMINO).solve()
None

