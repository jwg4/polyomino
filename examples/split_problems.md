To make computation more tractable, a tiling problem can be split into two or more sub-problems. Each solution to the original problem is also the solution to exactly one of the sub-problems.

```
>>> from polyomino.board import Chessboard
>>> from polyomino.constant import TETROMINOS, ALL_PENTOMINOS

```

First a problem which involves no repeated tiles. It can be solved without splitting, but let us look at how splitting works:
```
>>> problem = Chessboard().tile_with(ALL_PENTOMINOS + [TETROMINOS['Square']])
>>> subproblems = problem.split(at_least=2)
>>> len(subproblems)
3
>>> example = subproblems[0]
>>> example
<polyomino.problem.TilingSubProblem object at ...>
>>> print(example.display())
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
>>> sub_solution = example.solve()
>>> sub_solution
<polyomino.solution.Solution object at ...>
>>> example.is_solution(sub_solution.array)
True
>>> sub_solution.tiling
[[(0, 0), (1, 1), (1, 0), (2, 0)], [(0, 3), (1, 2), (0, 2), (0, 1)], [(3, 3), (2, 2), (2, 3), (1, 3)], [(3, 0), (2, 1), (3, 1), (3, 2)]]
>>> sub_solution.display()
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
>>> solution = example.original_solution(sub_solution)
>>> solution
<polyomino.solution.Solution object at ...>
>>> problem.is_solution(solution.array)
True
>>> solution.tiling
[[(0, 0), (1, 1), (1, 0), (2, 0)], [(0, 3), (1, 2), (0, 2), (0, 1)], [(3, 3), (2, 2), (2, 3), (1, 3)], [(3, 0), (2, 1), (3, 1), (3, 2)]]
>>> solution.display()
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
