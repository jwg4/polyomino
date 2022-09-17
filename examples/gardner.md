These examples are taken from chapter 13 of 'Mathematical Puzzles and Diversions' by Martin Gardner.

```python
>>> from polyomino.board import Chessboard, Rectangle
>>> from polyomino.constant import MONOMINO, DOMINO
>>> from polyomino.constant import RIGHT_TROMINO, STRAIGHT_TROMINO
>>> from polyomino.constant import ONESIDED_TETROMINOS
>>> from polyomino.constant import TETROMINOS, ALL_PENTOMINOS
>>> from polyomino.tileset import many, repeated_exactly, any_number_of

```
>[...]  
>In Chapter 3 (problem 3) we considered a polyomino problem dealing with the placing of dominoes on a mutilated chessboard.

(We can't solve this problem within a doctest because it takes too long.)

```python
>>> Chessboard().remove((0, 0)).remove((7, 7)).tile_with_many(DOMINO)
<polyomino.problem.TilingProblem object at ...>

```

[An impossible tiling will give the solution `None`.]

```python
>>> Rectangle(4, 4).remove((0, 0)).remove((3, 3)).tile_with_many(DOMINO).solve()

```

```python
>>> Chessboard().remove((0, 0)).remove((0, 7)).tile_with_many(DOMINO).solve().tiling
[[(0, 1), (0, 2)], [(0, 3), (0, 4)], [(0, 5), (0, 6)], [(1, 0), (1, 1)], [(1, 2), (1, 3)], [(1, 4), (1, 5)], [(1, 6), (1, 7)], [(2, 0), (2, 1)], [(2, 2), (2, 3)], [(2, 4), (2, 5)], [(2, 6), (2, 7)], [(3, 0), (3, 1)], [(3, 2), (3, 3)], [(3, 4), (3, 5)], [(3, 6), (3, 7)], [(4, 0), (4, 1)], [(4, 2), (4, 3)], [(4, 4), (4, 5)], [(4, 6), (4, 7)], [(5, 0), (5, 1)], [(5, 2), (5, 3)], [(5, 4), (5, 5)], [(5, 6), (5, 7)], [(6, 0), (6, 1)], [(7, 0), (7, 1)], [(6, 2), (6, 3)], [(7, 2), (7, 3)], [(6, 4), (6, 5)], [(7, 4), (7, 5)], [(6, 6), (6, 7)], [(7, 6), (7, 7)]]

```

```python
>>> print(Chessboard().remove((0, 0)).remove((0, 7)).tile_with_many(DOMINO).solve().display())
  +-+-+-+-+-+-+-+
  | | | | | | | |
+-+ + + + + + + +
| | | | | | | | |
+ +-+-+-+-+-+-+-+
| | | | | | | | |
+-+ + + + + + + +
| | | | | | | | |
+ +-+-+-+-+-+-+-+
| | | | | | | | |
+-+ + + + + + + +
| | | | | | | | |
+ +-+-+-+-+-+-+-+
| | | | | | | | |
+-+ + + + + + + +
  | | | | | | | |
  +-+-+-+-+-+-+-+
```

```python
>>> print(Chessboard().remove((2, 2)).tile_with_many(STRAIGHT_TROMINO).solve().display())
+-+-+-+-+-+-+-+-+
| | |     | | | |
+ + +-+-+-+ + + +
| | |     | | | |
+ + +-+-+-+ + + +
| | |X| | | | | |
+-+-+-+ + +-+-+-+
| | | | | | | | |
+ + + + + + + + +
| | | | | | | | |
+ + + +-+-+ + + +
| | | | | | | | |
+-+-+-+ + +-+-+-+
|     | | |     |
+-+-+-+ + +-+-+-+
|     | | |     |
+-+-+-+-+-+-+-+-+
```

```python
>>> print(Chessboard().tile_with_set(many(STRAIGHT_TROMINO).and_one(MONOMINO)).solve().display())
+-+-+-+-+-+-+-+-+
| | | | | | | | |
+ + + + + + + + +
| | | | | | | | |
+ + + + + + + + +
| | | | | | | | |
+-+-+-+-+-+-+-+-+
| | | | | |     |
+ + + + + +-+-+-+
| | | | | |     |
+ + + + + +-+-+-+
| | | | | | | | |
+-+-+-+-+-+-+ + +
|     |     | | |
+-+-+-+-+-+-+ + +
|     |     | | |
+-+-+-+-+-+-+-+-+
```

```python
>>> Chessboard().remove((2, 3)).tile_with_many(STRAIGHT_TROMINO).solve()
```

```python
>>> print(Chessboard().remove((4, 5)).tile_with_many(RIGHT_TROMINO).solve().display())
+-+-+-+-+-+-+-+-+
| |   | |   |   |
+ +-+ + +-+ + +-+
|   | |   | | | |
+-+-+-+-+-+-+-+ +
| |   | |   |   |
+ +-+ + +-+ +-+-+
|   | |   | |   |
+-+-+-+-+-+-+-+ +
| |   |   |   | |
+ +-+ + +-+ +-+-+
|   | | |X| |   |
+-+-+-+-+-+-+-+ +
| |   | |   | | |
+ +-+ + +-+ + +-+
|   | |   | |   |
+-+-+-+-+-+-+-+-+
```

```python
>>> [name for name in ONESIDED_TETROMINOS if Chessboard().tile_with_many(ONESIDED_TETROMINOS[name]).solve() is None]
['S', 'Z']

```

As mentioned on p118, there is an easy argument to show that this is impossible - naive search is computationally intractable.

```python
>>> Chessboard().tile_with_set(any_number_of([ONESIDED_TETROMINOS['L'], ONESIDED_TETROMINOS['J']]).and_one(TETROMINOS['Square']))
<polyomino.problem.TilingProblem object at ...>
```

```python
>>> print(Chessboard().tile_with(ALL_PENTOMINOS + [TETROMINOS['Square']]).solve().display())
+-+-+-+-+-+-+-+-+
| |         |   |
+ +-+-+-+-+-+   +
|     |     |   |
+-+ +-+ +-+-+-+-+
| | |   | |     |
+ +-+-+-+ +-+-+ +
|       |     | |
+-+-+-+-+-+-+ + +
|   |       | | |
+-+ +-+-+ +-+-+-+
| |   | | | |   |
+ +-+ + +-+ +-+ +
|   | | |     | |
+   +-+ +-+ +-+ +
|   |     | |   |
+-+-+-+-+-+-+-+-+

```