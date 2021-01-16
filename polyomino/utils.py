from math import gcd


def gcd_list(values):
    if not values:
        return 0
    return gcd(values[0], gcd_list(values[1:]))
