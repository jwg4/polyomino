import numpy as np


def selector_vector(n, i):
    return [i == j for j in range(0, n)]


def tiling_to_problem(tiles, shape):
    n = len(tiles)
    key = []
    data = []
    for i, tile in enumerate(tiles):
        selector = selector_vector(n, i)
        for translated in shape.positions(tile):
            key.append(translated)
            vector = selector + shape.bit_vector(translated)
            data.append(vector)
    return key, data


def tiling_to_array(tiles, shape):
    key, data = tiling_to_problem(tiles, shape)
    array = np.array(data, dtype=np.int32)
    return key, array
