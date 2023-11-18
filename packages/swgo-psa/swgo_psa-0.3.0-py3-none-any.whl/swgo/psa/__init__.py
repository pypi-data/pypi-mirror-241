"""Pulse-shape analysis for SWGO."""

import numpy as np
import numpy.typing as npt
from scipy.signal import filtfilt
from scipy.ndimage import convolve1d

__all__ = [
    "adaptive_centroid",
    "adaptive_sum",
    "upsample",
    "differentiate",
    "deconvolve_pole_zero",
]


def adaptive_centroid(
    waveform: npt.ArrayLike, peak_index: int, rel_descend_limit: float
) -> float:
    """
    Calculates the centroid for all samples around peak_index down to rel_descend_limit * waveform[peak_index].

    Parameters
    ----------
    waveform : ArrayLike
        Waveform stored in a 1-dimensional list or numpy array.
    peak_index : int
        Peak index for each channel.
    rel_descend_limit : float
        Fraction of the peak value down to which samples are accumulated in the centroid calculation.

    Returns
    -------
    centroid : float
        Peak centroid in units "samples"; peak_index if centroid calculation failed.
    """
    n_samples = len(waveform)
    if n_samples == 0:
        return float(peak_index)

    if (peak_index > (n_samples - 1)) or (peak_index < 0):
        raise ValueError("peak_index must be within the waveform limits")

    peak_amplitude = waveform[peak_index]
    if peak_amplitude <= 0.0:
        return float(peak_index)

    descend_limit = rel_descend_limit * peak_amplitude

    sum_ = 0.0
    jsum = 0.0

    j = peak_index
    while j >= 0 and waveform[j] > descend_limit:
        sum_ += waveform[j]
        jsum += j * waveform[j]
        j -= 1

    j = peak_index + 1
    while j < n_samples and waveform[j] > descend_limit:
        sum_ += waveform[j]
        jsum += j * waveform[j]
        j += 1

    if sum_ != 0.0:
        return jsum / sum_

    return float(peak_index)


def adaptive_sum(
    waveform: npt.ArrayLike, peak_index: int, descend_limit: float
) -> float:
    """
    Calculates the sum of all samples around peak_index down to descend_limit.

    Parameters
    ----------
    waveform : ArrayLike
        Waveform stored in a 1-dimensional list or numpy array.
    peak_index : int
        Peak index for each channel.
    descend_limit : float
        Absolute value down to which samples are accumulated.

    Returns
    -------
    sample_sum : float
        Sum of samples; 0 if waveform[peak_index] <= descend_limit or len(waveform) == 0.
    """
    n_samples = len(waveform)
    if n_samples == 0:
        return 0.0

    if (peak_index > (n_samples - 1)) or (peak_index < 0):
        raise ValueError("peak_index must be within the waveform limits")

    sum_ = 0.0

    j = peak_index
    while j >= 0 and waveform[j] > descend_limit:
        sum_ += waveform[j]
        j -= 1

    j = peak_index + 1
    while j < n_samples and waveform[j] > descend_limit:
        sum_ += waveform[j]
        j += 1

    return sum_


def upsample(waveforms: npt.ArrayLike, upsampling: int) -> np.ndarray:
    """
    Applies simple upsampling by interpolating with a double moving average filter.

    Parameters
    ----------
    waveforms : ArrayLike of shape (n_channels, n_samples)
        Waveforms stored in a numpy array.
    upsampling : int
        Upsampling factor to use (>= 1); if > 1, the input waveforms are resampled at upsampling times their original sampling rate.

    Returns
    -------
    upsampled_waveforms : ndarray
        Upsampled waveforms stored in a numpy array.
        Shape: (n_channels, upsampling * n_samples)

    Notes
    -----
    See `scipy.signal.resample` and `scipy.signal.resample_poly` for more sophisticated algorithms.
    """

    if upsampling < 1:
        raise ValueError(f"upsampling must be > 0, got {upsampling}")

    if upsampling == 1:
        return np.array(waveforms)

    return filtfilt(
        np.ones(upsampling),
        upsampling,
        np.repeat(waveforms, upsampling, axis=-1),
    )


def differentiate(waveforms: npt.ArrayLike, upsampling: int = 1) -> np.ndarray:
    """
    Applies simple differentiation and optional upsampling with a double moving average filter (using `upsample()`).

    Parameters
    ----------
    waveforms : ArrayLike of shape (n_channels, n_samples)
        Waveforms stored in a numpy array.
    upsampling : int (default: 1)
        Upsampling factor to use (>= 1); if > 1, the input waveforms are resampled at upsampling times their original sampling rate.

    Returns
    -------
    differentiated_waveforms : ndarray
        Differentiated waveforms stored in a numpy array.
        Shape: (n_channels, upsampling * n_samples)
    """

    prepend = np.take(waveforms, 0, axis=-1)
    if len(prepend.shape) == 1:
        prepend = np.atleast_2d(prepend).T

    differentiated_waveforms = np.diff(waveforms, prepend=prepend, axis=-1)

    if upsampling > 1:
        return upsample(differentiated_waveforms, upsampling)

    return differentiated_waveforms


def deconvolve_pole_zero(
    waveforms: npt.ArrayLike,
    baselines: npt.ArrayLike,
    pole_zero: float,
    upsampling: int = 1,
) -> np.ndarray:
    """
    Applies pole-zero deconvolution and optional upsampling with a double moving average filter (using `upsample()`).

    Parameters
    ----------
    waveforms : ArrayLike of shape (n_channels, n_samples)
        Waveforms stored in a numpy array.
    baselines : ArrayLike of shape (n_channels, ) or scalar float
        Baseline estimates for each channel that are subtracted from the waveforms before deconvolution.
    pole_zero : float
        Deconvolution parameter.
    upsampling : int (default: 1)
        Upsampling factor to use (>= 1); if > 1, the input waveforms are resampled at upsampling times their original sampling rate.

    Returns
    -------
    deconvolved_waveforms : ndarray
        Deconvolved and upsampled waveforms stored in a numpy array.
        Shape: (n_channels, upsampling * n_samples)
    """
    deconvolved_waveforms = np.atleast_2d(waveforms) - np.atleast_2d(baselines).T
    deconvolved_waveforms[:, 1:] -= pole_zero * deconvolved_waveforms[:, :-1]
    deconvolved_waveforms[:, 0] = 0

    if upsampling > 1:
        return upsample(deconvolved_waveforms, upsampling)

    return deconvolved_waveforms
