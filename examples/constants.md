>>> from polyomino.constant import *
>>> from polyomino.piece import display

>>> print(display(TETROMINOS['T']))
+-+-+-+
|     |
+-+ +-+
  | |
+ +-+ +

>>> print(display(TETROMINOS['J']))
+-+-+
|   |
+-+ +
  | |
+ + +
  | |
+ +-+

>>> print(display(TETROMINOS['Square']))
+-+-+
|   |
+ + +
|   |
+-+-+

>>> print(display(TETROMINOS['Line']))
+-+-+-+-+
|       |
+-+-+-+-+


>>> print(display(TETROMINOS['S']))
+-+-+ +
|   |
+-+ +-+
  |   |
+ +-+-+

>>> print(display(ONESIDED_TETROMINOS['L']))
+-+-+
|   |
+ +-+
| |
+ + +
| |
+-+ +

>>> print(display(ONESIDED_TETROMINOS['Z']))
+ +-+-+
  |   |
+-+ +-+
|   |
+-+-+ +
