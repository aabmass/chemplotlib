import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "chemplotlib",
    version = "0.0.1",
    author = "Aaron Abbott",
    author_email = "aabmass@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "BSD",
    keywords = "chemistry spectra",
    # url = "http://packages.python.org/an_example_pypi_project",
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],

    packages=['chemplotlib'],
    entry_points = {
        'gui_scripts': ['plot_ocean_optics=chemplotlib.plot_ocean_optics:main'],
    },
)
