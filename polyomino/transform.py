def rotations(tile, and_reflections=True):
    if and_reflections:
        return rotate_and_reflect(tile)
    else:
        return rotate(tile)


ROTATIONS = [
    [[1, 0], [0, 1]],
    [[0, -1], [1, 0]],
    [[-1, 0], [0, -1]],
    [[0, 1], [-1, 0]]
]


ROTATIONS_AND_REFLECTIONS = [
    [[1, 0], [0, 1]],
    [[0, -1], [1, 0]],
    [[-1, 0], [0, -1]],
    [[0, 1], [-1, 0]],
    [[-1, 0], [0, 1]],
    [[0, -1], [-1, 0]],
    [[1, 0], [0, -1]],
    [[0, 1], [1, 0]]
]


def rotate_and_reflect(tile):
    return unique_after_transform(tile, ROTATIONS_AND_REFLECTIONS)


def rotate(tile):
    return unique_after_transform(tile, ROTATIONS)


def unique_after_transform(tile, transforms):
    s = set()
    for m in transforms:
        rotated = [
            (m[0][0] * t[0] + m[0][1] * t[1], m[1][0] * t[0] + m[1][1] * t[1])
            for t in tile
        ]
        mx = min(s[0] for s in rotated)
        my = min(s[1] for s in rotated)
        shifted = [(t[0] - mx, t[1] - my) for t in rotated]
        key = tuple(sorted(shifted))
        if key not in s:
            yield shifted
            s.add(key)
