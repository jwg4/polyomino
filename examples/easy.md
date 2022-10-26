# Easy example

This shows a simple example of how to use the module.

```python
>>> from polyomino.constant import TETROMINOS
>>> from polyomino.board import Rectangle
>>> tile = TETROMINOS['T']
>>> board = Rectangle(4, 4)
>>> problem = board.tile_with_many(tile)
>>> solution = problem.solve()
>>> solution.tiling
[[(0, 0), (1, 1), (1, 0), (2, 0)], [(0, 3), (1, 2), (0, 2), (0, 1)], [(3, 3), (2, 2), (2, 3), (1, 3)], [(3, 0), (2, 1), (3, 1), (3, 2)]]
>>> print(solution.display())
+-+-+-+-+
|     | |
+-+ +-+ +
| | |   |
+ +-+-+ +
|   | | |
+ +-+ +-+
| |     |
+-+-+-+-+

```
