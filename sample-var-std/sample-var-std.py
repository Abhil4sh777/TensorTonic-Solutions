import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x_arr = np.array(x, dtype=float)

    # Compute unbiased sample variance (ddof=1 applies Bessel's correction)
    variance = float(np.var(x_arr, ddof=1))
    std_dev = float(np.sqrt(variance))

    return {"variance": variance, "standard_deviation": std_dev}