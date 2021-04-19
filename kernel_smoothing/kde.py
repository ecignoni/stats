
import numpy as np

def kde1D(X, bw=None, weights=None, gridmin=None, gridmax=None, bins=100,
          periodic=False, m=1.0, periodicity=2*np.pi):
    '''Weighted Kernel Density Estimation in one dimension with a Gaussian
    kernel (non-circular data) or a von Mises kernel (circular data).

    Arguments
    ---------
    X           : ndarray (N_samples,)
                Dataset
    bw          : float or None (default None)
                Kernel bandwidth. If None, Silverman's rule of thumb is used
                to guess the optimal bandwidth. Ignored if `periodic=True`.
    weights     : ndarray (N_samples) or None
                Sample weights. If None, equal weights are assigned to each point
    gridmin     : float (default None)
                Minimum value of the grid. If None, the value is guessed.
    gridmax     : float (default None)
                Maximum value of the grid. If None, the value is guessed.
    bins        : int (default 100)
                Number of bins of the grid.
    periodic    : bool (default False)
                Whether the data is circular. If True, a von Mises kernel is used.
    m           : float (default 1.0)
                Concentration parameter for the von Mises kernel. Ignored if
                `periodic=False`.
    periodicity : float (default 2*np.pi)
                Set the periodicity if `periodic=True`, ignored otherwise.

    Returns
    -------
    grid      : ndarray (bins,)
              Grid where the probability is dumped.
    kde       : ndarray (bins,)
              Probability density estimation.
    '''

    # Number of samples
    N = X.shape[0]

    if periodic is False:
    # =======================================================================
    # Use Gaussian Kernel Density Estimation if the variable is not periodic
    # =======================================================================

        # Guess the grid if not provided by the user
        if gridmin is None or gridmax is None:
            Xmin = X.min()
            Xmax = X.max()
            Xdel = (Xmax - Xmin) / 3
        if gridmin is None: gridmin = Xmin - Xdel
        if gridmax is None: gridmax = Xmax + Xdel

        grid = np.linspace(gridmin, gridmax, bins)
        if weights is None: weights = np.ones(N)
        sumw = weights.sum()
        if bw is None:
            # Bandwidth estimation using Silverman's rule of thumb
            iqr = np.subtract(*np.percentile(X, [75, 25]))
            std = np.std(X)
            bw = 0.9*np.min([std,iqr/1.349])/N**(1/5)
        norm = sumw*((2*bw**2*np.pi)**0.5)
        kde = (weights*np.exp(-((grid[:,None]-X[None,:])**2/(2*bw**2)))).sum(1) / norm


    elif periodic is True:
    # =======================================================================
    # Use von Mises Kernel Density Estimation for circular data
    # =======================================================================
        from scipy.special import i0

        # Guess the grid if not given
        if gridmin is None and gridmax is None:
            gridmin = -periodicity/2.
            gridmax = periodicity/2.
        elif gridmin is not None and gridmax is None:
            gridmax = gridmin + periodicity
        elif gridmin is None and gridmax is not None:
            gridmin = gridmax - periodicity

        grid = np.linspace(gridmin, gridmax, bins)
        if weights is None: weights = np.ones(N)
        sumw = weights.sum()
        norm = sumw*periodicity*i0(m)
        kde = (weights*np.exp(m*np.cos(((2*np.pi)/periodicity)*(grid[:,None]-X[None,:])))).sum(1) / norm

    return grid, kde

