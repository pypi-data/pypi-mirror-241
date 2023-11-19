from swgo.psa import adaptive_sum

from numpy.testing import assert_allclose


def test_adaptive_sum_1d():
    x = [0.0] * 16
    assert adaptive_sum(x, 8, 0) == 0
    x[8] = 1.0
    assert adaptive_sum(x, 8, 0) == 1
    x[7] = 3.0
    assert adaptive_sum(x, 8, 0) == 4
    x[9] = 0.1
    assert adaptive_sum(x, 8, 0.1) == 4
    assert adaptive_sum([1, 0.1, 1], 1, 0.1) == 0.0


def test_adaptive_sum_2d():
    x = [
        [0.0, 1.0, 0.0, 0.0],
        [2.0, 0.0, 0.0, 0.0],
    ]
    assert_allclose(adaptive_sum(x, 1, 0), [1.0, 0.0])
    assert_allclose(adaptive_sum(x, [1, 0], 0), [1.0, 2.0])
