import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from .correlation import *
from .wavelets import *
from .lomb_scargle import *
from scipy.interpolate import interp1d
from astropy.timeseries import LombScargle
import plato_msap4_demonstrator as msap4

'''
Function to compute the composite spectrum (CS)
and run the complete rotation pipeline
with WPS, ACF and CS.

This collection of functions combine the ability
if MSAP4-01 and MSAP4-02 to get the rotation periods
estimate from a given time series. Combined with
the ROOSTER implementation, they constitute
MSAP4-03.
'''

def compute_cs (ps, acf, p_acf=None, p_ps=None,
                normalise=False, smooth_cs=False,
                smooth_ps=False, index_prot_acf=-1) :
  '''
  Compute CS from PS (from wavelets or Lomb-Scargle) 
  and ACF (sampled at same periods by default). By default,
  the CS is normalised with its maximal value.
  '''
  #Renormalising step
  ps = ps / np.amax (ps)
  if index_prot_acf!=-1 :
    acf = acf / acf[index_prot_acf]
  else :
    acf = acf / np.amax (acf)

  if smooth_ps :
    glob_max = p_ps[np.argmax (ps)]
    sizebox = int (glob_max / np.median (-np.diff (p_ps)))
    ps = apply_smoothing (ps, sizebox)

  if p_acf is not None and p_ps is not None :
   fun = interp1d (p_ps, ps, fill_value=0, bounds_error=False)
   ps = fun (p_acf) 

  cs = ps * acf

  if smooth_cs :
    if p_acf is None :
      p_acf = np.arange (acf.size)
    glob_max = find_global_maximum (p_acf, cs)
    sizebox = int (glob_max / np.median (np.diff (p_acf)))
    cs = apply_smoothing (cs, sizebox)

  if normalise :
   cs /= np.amax (cs)

  return cs

def find_prot_cs (periods, cs) :
  '''
  Compute Prot from Lomb-Scargle periodogram
  as the maximum of the spectrum.

  Returns
  -------
    Tuple with ``prot`` and ``hcs``. 
  '''
  prot = periods[np.argmax (cs)]
  hcs = np.amax (cs)
  return prot, hcs

def plot_cs (periods, cs, ax=None, figsize=(8, 4),
             lw=1, filename=None, dpi=300, param_gauss=None,
             xlim=None) :
  '''
  Plot composite spectrum (CS).
  '''

  if ax is None :
    fig, ax = plt.subplots (1, 1, figsize=figsize)
  else :
    fig = None

  ax.plot (periods, cs, color='black', lw=lw)
  ax.set_xlabel ('Period (day)')
  ax.set_ylabel ('CS')

  if param_gauss is not None :
    n_gauss = param_gauss.shape[0]
    model = np.zeros (periods.size)
    for ii in range (n_gauss) :
      if param_gauss[ii,0]!=-1 :
        model += msap4.gauss (periods, *param_gauss[ii,:])
    ax.plot (periods, model, color='darkorange', lw=lw)

  if xlim is not None :
    ax.set_xlim (xlim)

  if filename is not None :
    plt.savefig (filename, dpi=dpi)
  
  return fig

def plot_analysis (t, s, periods, ps, acf, cs, wps=None, coi=None,
                   p_ps=None, figsize=(6, 12), filename=None, lw=1,
                   cmap='Blues', dpi=200, vmin=None, vmax=None,
                   normscale='linear', show=False, param_gauss_cs=None,
                   param_profile_ps=None, xlim=None, show_kepler_quarters=False,
                   tref=0) :
   '''
   Plot pipeline analysis results.
   '''
   if xlim is None :
     xlim = (0, 100)

   if wps is not None :
     gs_kw = dict(width_ratios=[3, 1])
     fig, axs = plt.subplots (4, 2, figsize=figsize, gridspec_kw=gs_kw)
     plot_wps (t, periods, wps, ps, coi,
                cmap=cmap, shading='gouraud',
                color_coi='black', ylogscale=False,
                ax1=axs[1,0], ax2=axs[1,1], lw=lw, param_gauss=param_profile_ps,
                normscale=normscale, vmin=vmin, vmax=vmax, 
                show_kepler_quarters=show_kepler_quarters, tref=tref)
   else :
     gs_kw = dict(width_ratios=[3, 0])
     fig, axs = plt.subplots (4, 2, figsize=figsize, gridspec_kw=gs_kw)
     axs[1,1].axis ('off')
     plot_ls (p_ps, ps, ax=axs[1,0], lw=lw, param_profile=param_profile_ps,
              logscale=False)
     axs[1,0].set_yscale ('log')
     axs[1,0].set_xlim (xlim)

   axs[0,0].plot (t, s, lw=lw, color='black')
   if show_kepler_quarters :
     start, _ = msap4.get_kepler_quarters ()
     for elt in start :
       axs[0,0].axvline(elt - tref, 
                        color='grey', ls='--')
   axs[0,0].set_xlim (t[0], t[-1])
   axs[0,0].set_xlabel ('Time (day)')
   axs[0,0].set_ylabel ('Flux (ppm)')
   plot_acf (periods, acf, ax=axs[2,0], lw=lw)
   plot_cs (periods, cs, ax=axs[3,0], lw=lw,  
            param_gauss=param_gauss_cs)
    
   axs[0,1].axis ('off')
   axs[2,1].axis ('off')
   axs[3,1].axis ('off')

   axs[2,0].set_xlim (xlim)
   axs[3,0].set_xlim (xlim)

   fig.tight_layout ()

   if filename is not None :
     plt.savefig (filename, dpi=dpi)

   if not show :
     plt.close ()

   return fig

def compute_sph (t, s, prot, 
                 return_timeseries=False) :
  '''
  Compute photometric activity index
  of the light curve. See Mathur et al. (2014).

  Returns
  -------
    Sph computed according to the provided ``prot``
    value.
  '''
  if prot==-1 :
    return -1
  dt = np.median (np.diff (t))
  size_slice = int (5 * prot / dt)
  n_slice = s.size // size_slice
  if n_slice==0 :
    return np.std (s)
  list_sph = []
  list_t = []
  for ii in range (n_slice) :
    list_sph.append (np.std (s[ii*size_slice:(ii+1)*size_slice]))
    list_t.append (np.mean (t[ii*size_slice:(ii+1)*size_slice]))
  # Only use the last slice if it is arbitrary large enough
  # compared to prot
  if (s.size - n_slice*size_slice)*dt > 2 * prot :
    list_sph.append (np.std (s[n_slice*size_slice:]))
    list_t.append (np.mean (t[n_slice*size_slice:]))
  list_sph = np.array (list_sph)
  list_t = np.array (list_t)
  sph = np.mean (list_sph)
  if return_timeseries :
    return sph, list_t, list_sph
  else :
    return sph

def compute_lomb_scargle_sph (t_sph, sph) :
  '''
  Compute the Lomb-Scargle periodogram of the provided Sph
  time series.

  Returns
  -------
    tuple with the periods and the power vectors
  '''

  dt_sph = np.median (np.diff (t_sph)) 
  ps_object = LombScargle(t_sph*86400, sph, center_data=True, fit_mean=False)
  res = t_sph[-1] - t_sph[0]
  freq = np.linspace (0, 1/(dt_sph*86400*2), (t_sph.size+1)//2)
  freq = freq[freq!=0]
  ps_object.power_standard_norm = ps_object.power(freq, normalization='standard',
                                                  method='slow', assume_regular_frequency=True)
  ls = ps_object.power_standard_norm
  p_ps = 1 / (freq*86400)
  return p_ps, ls

def create_feature_from_fitted_param (param, method='CS') :
  '''
  Create feature array from fitted param 
  obtained with the different methods. The function
  expect the three first parameters for each fitted
  profile to be, in this order, amplitude, central period
  (or frequency) and fwhm.
  '''
  param = param[:,:3]
  features =  np.ravel (param)
  n = param.shape[0]
  feature_names = []
  for ii in range (n) :
    feature_names.append ('{}_{}_1'.format (method, ii)) 
    feature_names.append ('{}_{}_2'.format (method, ii)) 
    feature_names.append ('{}_{}_3'.format (method, ii)) 

  feature_names = np.array (feature_names)

  return features, feature_names

def analysis_pipeline (t, s, periods_in=None, 
                       wavelet_analysis=True, plot=True, show=False, 
                       filename=None, figsize=(6,12),
                       cmap='Blues', normscale='linear',
                       vmin=None, vmax=None, lw=1, mother=None, xlim=None,
                       dpi=200, smooth_acf=True, fit_lomb_scargle=True,
                       show_kepler_quarters=False, tref=0,
                       add_profile_parameters_to_features=False) : 
   '''
   Analysis pipeline combining Lomb-Scargle (or wavelet analysis), ACF and CS.

   The pipeline compute Lomb-Scargle periodogram (or Wavelet Power Spectrum and Global 
   Wavelet Power Spectrum), Auto-Correlation function, and Composite spectrum of 
   the provided light curves, as well as a set of relevant features for each method
   of analysis.  

   Parameters
   ----------
   t : ndarray
     timestamps 

   s : ndarray
     timeseries

   period_in : ndarray
     value which will be used as input to compute
     the ACF lags. A ``periods`` vector corresponding
     to the exact position of the lags will be returned
     by the function.  
     If ``None``, a ``lags`` vector (and corresponding period
     vector) from ``0`` to ``s.size`` will be generated.
     Optional, default ``None``. 

   wavelet_analysis : bool
     if set to ``True`` the timeseries will be analysed
     with a wavelet analysis. Otherwise the Lomb-Scargle
     periodogram will be computed and used to compute
     the composite spectrum

   plot : bool
     if set to ``True`` a summary plot will be made.
     Optional, default ``None``. 

   filename : str
     the ``filename`` under which the summary plot will
     be saved. Optional, default ``None``.

   figsize : tuple 
     Figure size for the summary plot. Optional, default
     ``(10, 16)``.

   mother : object
     mother wavelet to consider. Optional, if set
     to ``None``, ``pycwt.Morlet (6)`` will be used.

   fit_lomb_scargle : bool
     if set to ``True``, the rotation peaks in the 
     Lomb-Scargle periodograms will be fitted using
     a Lorentzian profile.

   show_kepler_quarters : bool 
     start time of Kepler quarters will be shown on 
     the light curves and WPS (if ``wavelet_analysis`` is ``True``)

   tref : float
     reference time to use for the start of the series 
     when showing Kepler quarters.

   add_profile_parameters_to_features : bool
     if set to ``True``, the parameters of the fitted profiles
     for the PS and CS will be included in ``features``.
     The corresponding ``feature_names`` are named
     with the following pattern: ``CS_i_j`` or ``PS_i_j``,
     with ``i`` is an integer greater or equal to zero denoting
     the profile index.  
     with ``j=1`` for the amplitude parameter of the profile
     ``j=2`` for the central period (CS) or frequency (PS)
     and ``j=3`` for the fwhm parameter of the profile.

   Returns
   -------
   tuple
     Tuple of arrays containing output ``periods``, ``gwps``, 
     ``wps``, ``acf``, ``cs``, ``coi``, ``features``, and ``feature_names``
     arrays if ``wavelet_analysis`` is set to ``True``, ``periods``, ``ps``, 
     ``acf``, ``cs``, ``features``, and ``feature_names``,
     otherwise.
   '''
   dt = np.median (np.diff (t))
   p_acf, acf = compute_acf (s, dt, periods_in, normalise=True,
                               smooth=smooth_acf)
   # In the future, it will be possible to use the
   # additional outputs of find_period_acf to make
   # features for ROOSTER.
   prot_acf, hacf, gacf, index_prot_acf, _, _ = find_period_acf (p_acf, acf)
   if wavelet_analysis :
     p_ps, wps, gwps, coi = compute_wps (s, dt*86400, p_acf, mother=mother)
     ps = gwps
     prot_ps = find_prot_gwps (p_ps, gwps)
     # Setting to minus -1 parameters that are not computed
     # when using the wavelets
     h_ps, fa_prob_ps = -1, -1
     prot_ps, E_prot_ps, param_profile_ps = compute_prot_err_gaussian_fit (p_ps, gwps, verbose=False,
                                                                         n_profile=5, threshold=0.1)
     # Setting symmetric errors
     e_prot_ps = E_prot_ps
   else :
     p_ps, ps_object = compute_lomb_scargle (t, s)
     ps = ps_object.power_standard_norm
     prot_ps, e_prot_ps, E_prot_ps, fa_prob_ps, h_ps = find_prot_lomb_scargle (p_ps, 
                                                                ps_object, return_uncertainty=True)
     if fit_lomb_scargle :
       prot, e_prot_ps, E_prot_ps, param_profile_ps, list_h_ps = compute_prot_err_gaussian_fit_chi2_distribution (p_ps, ps,
                                                                                                n_profile=5, threshold=0.1)
   cs = compute_cs (ps, acf, p_acf=p_acf, p_ps=p_ps, index_prot_acf=index_prot_acf) 
   prot_cs, hcs = find_prot_cs (p_acf, cs)
   prot_cs, E_prot_cs, param_gauss_cs = compute_prot_err_gaussian_fit (p_acf, cs, verbose=False,
                                                                       n_profile=5, threshold=0.1)

   # Compute sph for different methods
   sph_ps = compute_sph (t, s, prot_ps)
   sph_acf = compute_sph (t, s, prot_acf)
   sph_cs = compute_sph (t, s, prot_cs)

   if plot :
     if wavelet_analysis :
       fig = plot_analysis (t, s, p_acf, ps, acf, cs, wps=wps, coi=coi,
                            figsize=figsize, cmap=cmap, lw=lw,
                            filename=filename, dpi=dpi, vmin=vmin,
                            vmax=vmax, normscale=normscale, show=show, xlim=xlim,
                            param_gauss_cs=param_gauss_cs, param_profile_ps=param_profile_ps,
                            show_kepler_quarters=show_kepler_quarters, tref=tref)
     else :
       fig = plot_analysis (t, s, p_acf, ps, acf, cs, p_ps=p_ps, 
                            figsize=figsize, cmap=cmap, lw=lw,
                            filename=filename, dpi=dpi, show=show,
                            param_gauss_cs=param_gauss_cs, xlim=xlim,
                            param_profile_ps=param_profile_ps)

   features = np.array ([prot_ps, prot_acf, prot_cs,
                         e_prot_ps, E_prot_ps, 
                         -1, -1, 
                         E_prot_cs, E_prot_cs,
                         sph_ps, sph_acf, sph_cs, 
                         h_ps, fa_prob_ps, hacf, gacf, hcs])
   feature_names = np.array(['prot_ps', 'prot_acf', 'prot_cs',
                             'e_prot_ps', 'E_prot_ps', 
                             'e_prot_acf', 'E_prot_acf',
                             'e_prot_cs', 'E_prot_cs',
                             'sph_ps', 'sph_acf', 'sph_cs',
                             'h_ps', 'fa_prob_ps', 
                             'hacf', 'gacf', 'hcs'])
   if add_profile_parameters_to_features :
     feat_cs, name_cs = create_feature_from_fitted_param (param_gauss_cs, method='CS')
     feat_ps, name_ps = create_feature_from_fitted_param (param_profile_ps, method='PS')
     features = np.concatenate ((features, feat_ps, feat_cs))
     feature_names = np.concatenate ((feature_names, name_ps, name_cs))
   if wavelet_analysis :
     return p_acf, gwps, wps, acf, cs, coi, features, feature_names
   else : 
     return p_ps, p_acf, ps, acf, cs, features, feature_names

def save_features (filename, star_id, features, feature_names) :
  '''
  Save feature and corresponding names to 
  a dedicated csv file. 

  Returns
  -------
  The pandas DataFrame that has been saved as a
  csv file. 
  '''

  df = pd.DataFrame (index=[star_id], 
                     data=features.reshape ((1, -1)), 
                     columns=feature_names)
  df.to_csv (filename, index_label='target_id')
  return df

def build_catalog_features (dirFeatures) :
  '''
  Read the csv files stored in the provided
  ``dirFeatures`` directory to build a csv 
  catalog summarising the feature of all 
  targets. The procedure will fail if any of 
  the available csv file does not have the 
  correct feature format.
  '''
  list_csv = glob.glob (os.path.join (dirFeatures, '*.csv'))
  list_df = []
  for csv in list_csv :
    list_df.append (pd.read_csv (csv, index_col='target_id')) 
  df = pd.concat (list_df)
  df = df.sort_index ()

  return df

def compute_delta_prot (prot, diffrot_candidates, diffrot_err,
                        delta_min=1/3, delta_max=3) :
  '''
  Analyse list of differential rotation period
  candidates.

  Only candidate values verifying 
  ``delta_min < candidate/prot < delta_max``
  are retained.
  '''
  cond = (diffrot_candidates / prot > delta_min) & (diffrot_candidates / prot < delta_max)
  diffrot_validated = diffrot_candidates[cond]
  diffrot_err_validated = diffrot_err[cond]
  
  return diffrot_validated, diffrot_err_validated
