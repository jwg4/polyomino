## Examples of fluid syntax to construct problems

```python
>>> from polyomino.board import Chessboard
>>> from polyomino.constant import MONOMINO, DOMINO
>>> from polyomino.tileset import many
```

```python
>>> Chessboard()
<polyomino.board.Chessboard object at ...>
```

```python
>>> Chessboard().tile_with_many(DOMINO)
<polyomino.problem.TilingProblem object at ...>
```

```python
>>> Chessboard().tile_with_set(many(DOMINO).and_repeated_exactly(2, MONOMINO))
<polyomino.problem.TilingProblem object at ...>
```

```python
>>> Chessboard().tile_with_set(many(DOMINO).and_repeated_exactly(2, MONOMINO)).with_heuristics()
<polyomino.problem.TilingProblem object at ...>
```