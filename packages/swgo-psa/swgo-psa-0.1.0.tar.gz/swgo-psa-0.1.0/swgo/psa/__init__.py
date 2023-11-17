"""Pulse-shape analysis for SWGO."""

import numpy as np

__all__ = ["adaptive_centroid"]


def adaptive_centroid(waveform, peak_index, rel_descend_limit):
    """
    Calculates the centroid for all samples around peak_index down to rel_descend_limit * waveform[peak_index].

    Parameters
    ----------
    waveform : ndarray
        Waveform stored in a numpy array.
    peak_index : int
        Peak index for each pixel.
    rel_descend_limit : float
        Fraction of the peak value down to which samples are accumulated in the centroid calculation.

    Returns
    -------
    centroid : ndarray
        Peak centroid in units "samples"; peak_index if centroid calculation failed.
    """
    n_samples = waveform.size
    if n_samples == 0:
        return peak_index

    if (peak_index > (n_samples - 1)) or (peak_index < 0):
        raise ValueError("peak_index must be within the waveform limits")

    peak_amplitude = waveform[peak_index]
    if peak_amplitude <= 0.0:
        return peak_index

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

    return peak_index
