import numpy as np
import matplotlib.pyplot as plt
import numba
import pandas as pd
from scipy.signal import correlate

'''
Functions to compute correlation
and autocorrelation functions.

This collection of functions are dedicated
to achieve the task of the PLATO module
MSAP4-02.
'''

def period_to_lag (dt, size, periods_in=None) :
  '''
  Compute from sampling and input periods
  closest lag index in the data and 
  corresponding output periods.

  Parameters 
  ----------
  
  dt : float
    sampling, in day

  periods_in : ndarray
    input periods, in day
  '''

  if periods_in is None :
    lags = np.arange (0, size)
  else :
    lags = np.rint (periods_in/dt).astype (int)
  lags = np.unique (lags)
  periods_out = lags * dt
  periods_out = periods_out[lags<size]
  lags = lags[lags<size]
    
  return lags, periods_out

@numba.jit
def cross_correlation (y1, y2, lag) :
  '''
  Compute cross correlation value between two 
  vectors of same size for a given lag.
  '''

  y1 = y1[:y1.size-lag]
  y2 = y2[lag:]

  ccorr = np.sum (y1*np.conj (y2))

  return ccorr 

@numba.jit
def compute_ccf (y1, y2, lags) :
  '''
  Wrapper to compute cross correlation
  for an ensemble of lags.
  ''' 

  ccf = np.zeros (lags.size)
  for ii, lag in enumerate (lags) :
    ccf[ii] = cross_correlation (y1, y2, lag)

  return ccf

def compute_acf (s, dt, periods_in=None, normalise=True,
                 use_scipy_correlate=True, smooth=False,
                 pcutoff=None, pthresh=None) :
  '''
  Compute autocorrelation function for 
  a uniformly sampled timeseries.
  '''
  lags, periods_out = period_to_lag (dt, s.size, periods_in)
  if not use_scipy_correlate :
    acf = compute_ccf (s, s, lags)
  else :
    acf = correlate(s, s, mode='full', method='fft')
    acf = acf[s.size-1:]
    acf = acf[lags] 
  if smooth :
    glob_max = find_global_maximum (periods_out, acf,
                                    pcutoff=pcutoff, pthresh=pthresh)
    dt = np.median (np.diff (periods_out))
    sizebox = int (glob_max / dt)
    if sizebox > 0 :
      acf = apply_smoothing (acf, sizebox)
  if normalise :
    acf = acf / np.amax (acf) 
  
  return periods_out, acf  

def plot_acf (periods, acf, ax=None, figsize=(8, 4),
              lw=1, filename=None, dpi=300,
              prot=None, xlim=None) :
  '''
  Plot autocorrelation function (ACF).
  '''

  if ax is None :
    fig, ax = plt.subplots (1, 1, figsize=figsize)
  else :
    fig = None

  ax.plot (periods, acf, color='black', lw=lw)
  ax.set_xlabel ('Period (day)')
  ax.set_ylabel ('ACF')
  if prot is not None :
    ax.axvline (prot, color='grey', lw=lw, ls='--')

  if xlim is not None :
    ax.set_xlim (xlim)

  if filename is not None :
    fig.savefig (filename, dpi=dpi)

  return fig

def apply_smoothing (a, sizebox, win_type='triang') :
  '''
  Smoothing function. Uses triangle smoothing by default

  Parameters
  ----------
  vector: ndarray 
    vector to smooth.

  smoothing: int
    size of the rolling window used for the smooth.

  win_type: str 
    see ``scipy.signal.windows``. Optional, default ``triang``.

  Returns
  -------
  smoothed vector
  '''
  smoothed = pd.Series (data=a)
  smoothed = smoothed.rolling (sizebox, min_periods=1,
                               center=True, win_type=win_type).mean ()
  return smoothed.to_numpy ()

def find_global_maximum (p_acf, acf, 
                         pcutoff=None, pthresh=None) :
  """
  Find period of the global maximum of an ACF
  function (ignoring the zero-lag maximum 
  and first decreasing slope)
  """ 
  if pcutoff is not None :
    acf = acf[p_acf<pcutoff]
    p_acf = p_acf[p_acf<pcutoff]
  if pthresh is not None :
    acf = acf[p_acf>pthresh]
    p_acf = p_acf[p_acf>pthresh]

  if np.any (acf<0) :
    indexes = np.nonzero (acf<0)[0]
    index_max = np.argmax (acf[indexes[0]:]) + acf[:indexes[0]].size
  else :
    index_max = np.argmax (acf)
  glob_max = p_acf[index_max]
  return glob_max

def find_local_extrema (data) : 
  """
  Find the maxima and minima in a given array.

  Parameters
  −−−−−−−−−−
  
  data : ndarray
    input array to explore

  Returns 
  −−−−−−−
  a_min, a_max : tuple of ndarray
    maxima and minima of the array
  """
  a_min = (np.diff(np.sign(np.diff(data))) > 0).nonzero()[0] + 1 # local min
  a_max = (np.diff(np.sign(np.diff(data))) < 0).nonzero()[0] + 1 # local max
  return a_min, a_max

def find_period_acf (periods, acf,
                     pcutoff=None, pthresh=None) : 
  """
  Parameters 
  −−−−−−−−−− 

  periods : ndarray
     Period value on which the autocorrelation
     function has been computed.

  acf : ndarray
     Autocorrelation function. 

  Returns 
  −−−−−−−
  Tuple with ``prot``, ``hacf``, ``gacf``, ``all_prots``, ``all_hacf``
  
  """
  a_min, a_max = find_local_extrema (acf)
  if a_max.size > 0 and a_min.size > 1 :
    hacf = acf[a_max[0]]
    a1 = acf[a_max[0]] - acf[a_min[0]] 
    a2 = acf[a_max[0]] - acf[a_min[1]]
    gacf = (a1 + a2) / 2 
    index_prot = a_max[0]
    prot = periods[index_prot] 
    all_prots = periods[a_max]
    all_hacf = acf[a_max]
    if pcutoff is not None :
      if prot > pcutoff :
        prot, hacf, gacf = -1, -1, -1
      all_hacf = all_hacf[all_prots<pcutoff]
      all_prots = all_prots[all_prots<pcutoff]
    if pthresh is not None :
      if prot < pthresh :
        prot, hacf, gacf = -1, -1, -1
      all_hacf = all_hacf[all_prots>pthresh]
      all_prots = all_prots[all_prots>pthresh]
    return prot, hacf, gacf, index_prot, all_prots, all_hacf
  else :
    return -1, -1, -1, -1, np.array ([-1]), np.array([-1])

if __name__=='__main__' :

  y1 = np.zeros (6)
  y2 = np.zeros (6)
  y1[0] = 1
  y2[3] = 1
  ccorr = cross_correlation (y1, y2, 3)
  assert ccorr==1
  ccorr = cross_correlation (y1, y2, 2)
  assert ccorr==0
  lags = np.array ([1, 2, 3])
  ccf = compute_ccf (y1, y2, lags) 
  print (ccf)
