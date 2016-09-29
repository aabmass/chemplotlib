"""Module to plot an ocean optics spectrum quickly"""

from . import chemplotlib

import numpy as np
import matplotlib.pyplot as pl
import matplotlib.style

def quick_plot(fname):
    """Quickly plots an ocean optics spectrum and displays it via matplotlib"""
    
    # make it pretty...
    matplotlib.style.use('ggplot')

    wvln, signal = chemplotlib.read_ocean_optics_spectrometer(fname)
    
    # plot wavelength vs signal, be it absorbance or intensity
    pl.plot(wvln, signal)
    pl.show()

def main():
    """the entry point provided for setuptools"""
    import sys

    # expect file name in sys.argv[1]
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: plot_ocean_optics <spectrum_file>\n')
        sys.exit(1)

    quick_plot(sys.argv[1])

