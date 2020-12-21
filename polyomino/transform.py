def rotate(tile):
    s = set()
    for m in [[[1, 0], [0, 1]], [[0, -1], [1, 0]], [[-1, 0], [0, -1]], [[0, 1], [-1, 0]]]:
        rotated = [
            (m[0][0] * t[0] + m[0][1] * t[1], m[1][0] * t[0] + m[1][1] * t[1])
            for t in tile
        ]
        mx = min(s[0] for s in rotated)
        my = min(s[1] for s in rotated)
        shifted = [(t[0] - mx, t[1] - my) for t in rotated]
        shifted.sort()
        if tuple(shifted) not in s:
            yield shifted
            s.add(tuple(shifted))
