from swgo.psa import adaptive_sum


def test_adaptive_sum():
    x = [0.0] * 16
    assert adaptive_sum(x, 8, 0) == 0
    x[8] = 1.0
    assert adaptive_sum(x, 8, 0) == 1
    x[7] = 3.0
    assert adaptive_sum(x, 8, 0) == 4
    x[9] = 0.1
    assert adaptive_sum(x, 8, 0.1) == 4
