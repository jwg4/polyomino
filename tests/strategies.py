from hypothesis.strategies import builds, one_of, integers, sampled_from

from polyomino.constant import ALL_UP_TO_PENTOMINOS


def make_h_line(n):
    return [(i, 0) for i in range(0, n)]


def make_v_line(n):
    return [(0, i) for i in range(0, n)]


h_lines = builds(make_h_line, integers(1, 30))
v_lines = builds(make_v_line, integers(1, 30))


def make_box(x, y):
    return [(i, j) for i in range(0, x) for j in range(0, y)]


boxes = builds(make_box, integers(1, 10), integers(1, 10))


def make_v_shape(x, y):
    return [(0, i) for i in range(0, x)] + [(j, 0) for j in range(0, y)]


def make_j_shape(x, y):
    return [(0, i) for i in range(0, x + y)] + [(1, i) for i in range(x)]


v_shapes = builds(make_v_shape, integers(2, 10), integers(2, 10))
j_shapes = builds(make_j_shape, integers(2, 5), integers(2, 5))

simple_polyominos = one_of(h_lines, v_lines, boxes, v_shapes, j_shapes)

small_polyominos = sampled_from(ALL_UP_TO_PENTOMINOS)

polyominos = one_of(simple_polyominos, small_polyominos)
