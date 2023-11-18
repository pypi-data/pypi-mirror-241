from swgo.psa import differentiate, upsample

import numpy as np
from numpy.testing import assert_allclose


def test_differentiate_1d():
    x = [0.0, 1.0, 1.0, 0.0]
    dx = np.diff(x, prepend=x[0])
    assert_allclose(differentiate(x, 1), dx)
    assert_allclose(differentiate(x, 2), upsample(dx, 2))


def test_differentiate_2d():
    x = [
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 1.0, 0.0],
    ]
    dx = np.diff(x, prepend=[[x[0][0]], [x[1][0]]], axis=-1)
    assert_allclose(differentiate(x, 1), dx)
    assert_allclose(
        differentiate(x, 2), [differentiate(x[0], 2), differentiate(x[1], 2)]
    )
