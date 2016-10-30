"""Module to plot an ocean optics spectrum quickly"""

from . import chemplotlib

import numpy as np
import matplotlib.pyplot as pl
import matplotlib.style

def quick_plot(fnames):
    """Quickly plots an ocean optics spectrum and displays it via matplotlib"""
    
    # make it pretty...
    matplotlib.style.use('ggplot')

    for f in fnames:
        wvln, signal = chemplotlib.read_ocean_optics_spectrometer(f)
        pl.plot(wvln, signal, label=f)

    pl.legend()
    pl.show()

def main():
    """the entry point provided for setuptools"""
    import sys

    # expect file names in sys.argv[1]
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: plot_ocean_optics <spectrum_file 1> ' +
                         '[spectrum_file 2 [, spectrum_file ... n]]\n')
        sys.exit(1)

    quick_plot(sys.argv[1:])

