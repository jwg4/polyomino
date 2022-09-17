```python
>>> from polyomino.constant import *
>>> from polyomino.piece import display
```

```python
>>> print(display(TETROMINOS['T']))
+-+-+-+
|     |
+-+ +-+
  | |
  +-+
```

```python
>>> print(display(TETROMINOS['J']))
+-+-+
|   |
+-+ +
  | |
  + +
  | |
  +-+
```

```python
>>> print(display(TETROMINOS['Square']))
+-+-+
|   |
+   +
|   |
+-+-+
```

```python
>>> print(display(TETROMINOS['Line']))
+-+-+-+-+
|       |
+-+-+-+-+
```

```python
>>> print(display(TETROMINOS['S']))
+-+-+
|   |
+-+ +-+
  |   |
  +-+-+
```

```python
>>> print(display(ONESIDED_TETROMINOS['L']))
+-+-+
|   |
+ +-+
| |
+ +
| |
+-+
```

```python
>>> print(display(ONESIDED_TETROMINOS['Z']))
  +-+-+
  |   |
+-+ +-+
|   |
+-+-+
```