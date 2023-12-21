from polyomino.piece import decode_pieces

TETROMINOES = '''
IIII  LLL  OO  TTT  ZZ
      L    OO   T    ZZ
'''

PENTOMINOES = '''
I
I     L      N                      Y
I  FF L  PP  N TTT       V   W  X  YY ZZ
I FF  L  PP NN  T  U U   V  WW XXX  Y  Z
I  F  LL P  N   T  UUU VVV WW   X   Y  ZZ
'''

def test_decode_pieces():
    tiles = decode_pieces(TETROMINOES)
    assert tiles
