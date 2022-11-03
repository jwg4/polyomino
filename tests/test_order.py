from polyomino.order import has_order_greater_than


def test_rectangle():
    tile = [(0, 0), (0, 1), (0, 2)]

    predicate, n, tiling = has_order_greater_than(tile, 1)
    assert not predicate
    assert n == 1
    assert tiling == [tile]

    predicate, n, tiling = has_order_greater_than(tile, 2)
    assert not predicate
    assert n == 1
    assert tiling == [tile]

    predicate, n, tiling = has_order_greater_than(tile, 3)
    assert not predicate
    assert n == 1
    assert tiling == [tile]


def test_t_tetromino():
    tile = [(0, 0), (0, 1), (0, 2), (1, 1)]

    predicate, n, tiling = has_order_greater_than(tile, 1)
    assert predicate
    assert n is None
    assert tiling is None

    predicate, n, tiling = has_order_greater_than(tile, 2)
    assert predicate
    assert n is None
    assert tiling is None

    predicate, n, tiling = has_order_greater_than(tile, 3)
    assert predicate
    assert n is None
    assert tiling is None

    predicate, n, tiling = has_order_greater_than(tile, 4)
    assert not predicate
    assert n == 4
    assert len(tiling) == 4

    predicate, n, tiling = has_order_greater_than(tile, 5)
    assert not predicate
    assert n == 4
    assert len(tiling) == 4

    predicate, n, tiling = has_order_greater_than(tile, 6)
    assert not predicate
    assert n == 4
    assert len(tiling) == 4
