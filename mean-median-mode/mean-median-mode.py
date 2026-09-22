from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Compute mean and median using numpy, converting back to float
    mean_val = float(np.mean(x))
    median_val = float(np.median(x))

    # Count frequencies of each element
    counts = Counter(x)
    max_freq = max(counts.values())

    # Find all candidates that match the max frequency and select the minimum
    mode_candidates = [val for val, count in counts.items() if count == max_freq]
    mode_val = float(min(mode_candidates))

    return {"mean": mean_val, "median": median_val, "mode": mode_val}