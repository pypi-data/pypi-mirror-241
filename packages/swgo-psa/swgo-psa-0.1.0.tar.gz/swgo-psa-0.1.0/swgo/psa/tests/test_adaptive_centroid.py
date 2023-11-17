import numpy as np

from swgo.psa import adaptive_centroid


def test_adaptive_centroid():
    x = np.zeros(16)
    assert adaptive_centroid(x, 8, 0) == 8
    x[8] = 1.0
    assert adaptive_centroid(x, 8, 0) == 8
    x[7] = 3.0
    assert adaptive_centroid(x, 8, 0) == 7.25
    x[9] = 0.1
    assert adaptive_centroid(x, 8, 0.1) == 7.25
