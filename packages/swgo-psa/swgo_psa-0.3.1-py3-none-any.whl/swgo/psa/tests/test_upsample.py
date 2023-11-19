from swgo.psa import upsample

from numpy.testing import assert_allclose


def test_upsample_1d():
    x = [0.0, 1.0, 1.0, 0.0]
    assert_allclose(upsample(x, 1), x)
    assert_allclose(upsample(x, 2), [0.0, 0.25, 0.75, 1.0, 1.0, 0.75, 0.25, 0.0])


def test_upsample_2d():
    x = [
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
    ]
    assert_allclose(upsample(x, 1), x)
    assert_allclose(upsample(x, 2), [upsample(x[0], 2), upsample(x[1], 2)])
