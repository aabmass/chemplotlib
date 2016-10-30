import numpy as np
import matplotlib.pyplot as pl
import re

def read_ocean_optics_spectrometer(fname):
    """Returns numpy array with lambda, signal for an ocean optics spectrum
    
    Give the filename to an ocean optics collected spectrum (tab delimited), this
    reads the file and gives a numpy array back. This method will detect if
    there is a header and skip over it
    """

    # regex to match on lines when reading in data to skip headers
    r = re.compile(r'^[0-9]+\.[0-9]+\t+')

    with open(fname, 'r') as spectrum_file:
        data = [tuple(float(val.strip()) for val in line.split('\t'))
                for line in spectrum_file if r.match(line)]

        # return a numpy array
        return np.array(data).T

def normalize_spectrum(spectrum):
    """Normalize a spectrum of the form x, y over y
    
    Gives back a numpy array of the same data with y term normalized
    """
    x, y = spectrum
    return np.array([x, y / np.max(y)])

def stacked_spectra_plot(fnames, labels=None, offset=1.1, show=False):
    """Create a stacked spectrum plot for several ocean optics spectra
    
    Given an iterable of filenames to ocean optics spectra, this will
    stack all of them into a relative intensity plot in the order given.

    Change offset to vary the vertical spacing between each spectrum. The
    label parameter, if given is an iterable of labels to go in the legend

    If show=True, the plot will be displayed.
    """

    spectra = map(read_ocean_optics_spectrometer, fnames)

    # normalize if offset is nonzero, for not-to-scale visuals

    if offset != 0:
        spectra = map(normalize_spectrum, spectra)

    for i, spectrum in enumerate(spectra):
        x, y = spectrum
        pl.plot(
            x,
            y + offset * i,
            label=labels[i] if labels else 'Spectrum {}'.format(i)
        )

    pl.xlim(xmin=250)

    # If the offset is 0, then don't get rid of the y axis (signal)
    # units. If the offset is nonzero, then get rid of them since they
    # no long have any meaning

    if offset != 0:
        pl.yticks((), ())
        pl.ylim(ymin=-0.2)

    pl.legend(fontsize=16)
    pl.xlabel('$\lambda$ (nm)', fontsize=16)
    pl.ylabel('Normalized Absorbance', fontsize=16)

    if show: pl.show()

