from hypothesis import example, given
from hypothesis.strategies import just

from polyomino.transform import rotations


@given(just([(0, 0), (1, 0), (1, 1), (2, 0)]))
def test_rotation_conserves_order(tile):
    """
    We check order by comparing the (Manhattan) distance between
    each two squares (by index) before and after their rotation.
    """
    n = len(tile)
    for rotated in rotations(tile, False):
        for i in range(0, n):
            for j in range(0, i):
                d_orig = abs(tile[i][0] - tile[j][0]) + abs(tile[i][1] - tile[j][1])
                d_rot = abs(rotated[i][0] - rotated[j][0]) + abs(
                    rotated[i][1] - rotated[j][1]
                )
                assert d_orig == d_rot
