# PyKOSMOS
<!-- [![Documentation Status](https://readthedocs.org/projects/kosmos/badge/?version=latest)](https://kosmos.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/199771667.svg)](https://zenodo.org/badge/latestdoi/199771667) -->

An easy to use reduction package for one-dimensional longslit spectroscopy. 

## Goals
This tool *should* be able to handle 90% of basic reduction needs from a longslit-style spectrograph.... there are many other smaller or more subtle goals for this project that will be outlined here.

There needs to be many worked examples available.


## Motivation
We need simple to use, standalone reduction tools that can handle most tasks automatically.

The predecessor was [PyDIS](https://github.com/StellarCartography/pydis), a semi-complete standalone reduction suite in Python that has been used for many instruments and [publications](https://ui.adsabs.harvard.edu/abs/2016zndo.....58753D/abstract) so far! Since then, many [astropy](https://www.astropy.org) components have advanced to better handle many of the tasks PyDIS attempted, but [specreduce](https://github.com/astropy/specreduce) is not complete yet (I share in this blame).

My [original blog post](https://jradavenport.github.io/2015/04/01/spectra.html) on the topic from 2015 still largely stands...

## Links
* [PyDIS](https://github.com/StellarCartography/pydis)
* [dtw_identify](https://github.com/jradavenport/dtw_identify/), automatic wavelength calibration using Dynamic Time Warping, developed in PyKOSMOS