from swgo.psa import adaptive_centroid

from numpy.testing import assert_allclose


def test_adaptive_centroid_1d():
    x = [0.0] * 16
    assert adaptive_centroid(x, 8, 0) == 8
    x[8] = 1.0
    assert adaptive_centroid(x, 8, 0) == 8
    x[7] = 3.0
    assert adaptive_centroid(x, 8, 0) == 7.25
    x[9] = 0.1
    assert adaptive_centroid(x, 8, 0.1) == 7.25


def test_adaptive_centroid_2d():
    x = [
        [0.0, 1.0, 0.0, 0.0],
        [2.0, 0.1, 0.0, 0.0],
    ]
    assert_allclose(adaptive_centroid(x, 1, 0.1), [1.0, 0.1 / 2.1])
    assert_allclose(adaptive_centroid(x, [1, 0], 0.1), [1.0, 0.0])
