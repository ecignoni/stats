# Kernel Smoothing Methods

Kernel smoothing of various kind.

* kde1D.py : Kernel Density Estimation (KDE) for 1-dimensional feature vectors. Allows for assigning weights to each data point and 
perform a weighted KDE. A Gaussian kernel is used for non-circular data, and a von Mises kernel for circular data. Guesses a grid if
no grid specifications are given (useful for a quick plot). If the bandwidth of the Gaussian kernel is not given, it is guessed using
the Silverman's rule of thumb. Currently, a rule-of-thumb of the concentration parameter of the von Mises kernel is not implemented.

