"""Metrics used when reporting reconstruction experiments."""

import math


def psnr(mse: float, data_range: float = 1.0) -> float:
    """Compute peak signal-to-noise ratio from mean squared error."""
    if mse < 0:
        raise ValueError("mse must be non-negative")
    if data_range <= 0:
        raise ValueError("data_range must be positive")
    if mse == 0:
        return float("inf")
    return 10.0 * math.log10((data_range**2) / mse)
