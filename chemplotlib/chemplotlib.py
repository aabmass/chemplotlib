import numpy as np
import matplotlib.pyplot as pl

def read_ocean_optics_spectrometer(fname):
    """Returns numpy array with lambda, signal for an ocean optics spectrum
    
    Give the filename to an ocean optics collected spectrum (tab delimited), this
    reads the file and gives a numpy array back
    """

    with open(fname, 'r') as spectrum_file:
        data = [tuple(float(val.strip()) for val in line.split('\t'))
                for line in spectrum_file]

        # return a numpy array
        return np.array(data).T

def normalize_spectrum(spectrum):
    """Normalize a spectrum of the form x, y over y
    
    Gives back a numpy array of the same data with y term normalized
    """
    x, y = spectrum
    return np.array([x, y / np.max(y)])

def stacked_spectra_plot(ocean_optics_spectra_fnames, show=False):
    """Create a stacked spectrum plot for several ocean optics spectra
    
    Given an iterable of filenames to ocean optics spectra, this will
    stack all of them into a relative intensity plot in the order given

    Note that this function does not call show unless show=True (parameter),
    allowing you to further customize the output via pyplot before displaying
    it. e.g. pl.title('My title'); show()
    """

    spectra = map(read_ocean_optics_spectrometer, ocean_optics_spectra_fnames)

    normalized = map(normalize_spectrum, spectra)

    for i, spectrum in enumerate(normalized):
        x, y = spectrum
        pl.plot(x, y + 1.1 * i, label='Spectrum {}'.format(i))

    pl.xlim(xmin=250)

    pl.yticks((), ())
    pl.ylim(ymin=-0.2)

    pl.legend(fontsize=12)
    pl.xlabel('$\lambda$ (nm)', fontsize=16)
    pl.ylabel('Normalized Absorbance', fontsize=16)

    if show: pl.show()

