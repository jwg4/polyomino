from polyomino.utils import gcd_list


def test_gcd_list():
    assert 0 == gcd_list([])
    assert 1 == gcd_list([1])
    assert 2 == gcd_list([2])
    assert 1 == gcd_list([2, 3, 4])
    assert 3 == gcd_list([3, 3, 3, 9])
    assert 2 == gcd_list([4, 2, 10, 1000])
