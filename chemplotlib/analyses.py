import numpy as np
from scipy import stats

def fit_line(x, y):
    """fit_line

    Convenience function for performing linear regression on data. Given x and
    y data, returns a numpy poly1d for result and the R^2 value.

    :param x:
    :param y:
    """
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    r_squared = r_value ** 2
    f = np.poly1d([slope, intercept])

    return f, r_squared

def fourier_bandpass_filter(x, threshold_percent=0.10):
    fft = np.fft.fft
    ifft = np.fft.ifft
    
    fft_signal = fft(x)
    threshold = max(np.absolute(fft_signal)) * (1 - threshold_percent)
    fft_denoise = np.array([freq if np.absolute(freq) > threshold else 0 for
        freq in fft_signal])

    return ifft(fft_denoise)
