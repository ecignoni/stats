# Kernel Smoothing Methods

Kernel smoothing of various kind.

* kde1D : Kernel Density Estimation (KDE) for 1-dimensional feature vectors. Allows for assigning weights to each data point and 
performing a weighted KDE. A Gaussian kernel is used for non-circular data, and a von Mises kernel for circular data. Guesses a grid if
no grid specifications are provided (useful for a quick plot). If the bandwidth of the Gaussian kernel is not given, it is guessed using
the Silverman's rule of thumb. Currently, a rule-of-thumb for the concentration parameter of the von Mises kernel is not implemented.

