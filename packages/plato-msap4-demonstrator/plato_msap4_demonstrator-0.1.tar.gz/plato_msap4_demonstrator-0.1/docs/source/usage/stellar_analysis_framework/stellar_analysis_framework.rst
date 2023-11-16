Stellar analysis framework
==========================

This notebook provide an example of the full PLATO MSAP4 demonstrator
analysis: Lomb-Scargle periodogram, autocorrelation functions and
composite spectrum are used to produce a set of features exploited by an
existing instance of ROOSTER to return the final rotation period of the
analysed target. You will find that what is done here is very similar to
the previous tutorial notebook (``rooster_training_framework``, you
should run it before doing this tutorial), the only big difference is
actually that we will use here a pre-trained ROOSTER instance !

.. code:: ipython3

    import plato_msap4_demonstrator as msap4

A simple example
----------------

.. code:: ipython3

    import importlib
    import tqdm
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    
    if not os.path.exists ('stellar_analysis_features') :
        os.mkdir ('stellar_analysis_features')
    if not os.path.exists ('stellar_analysis_plots') :
        os.mkdir ('stellar_analysis_plots')    

Our working case is a KIC3733735, a well-known *Kepler* fast rotating
star.

.. code:: ipython3

    filename = msap4.get_target_filename (msap4.timeseries, '003733735')
    t, s, dt = msap4.load_resource (filename)

The first thing we have to do is run the analysis pipeline. In
particular, we can take a look at the plots made from the different
analysis methods.

.. code:: ipython3

    p_in = np.linspace (0, 100, 1000)
    (p_ps, p_acf, ps, acf, 
     cs, features, feature_names) = msap4.analysis_pipeline (t, s, periods_in=p_in, figsize=(8,10),
                                                             wavelet_analysis=False, plot=True,
                                                             filename='stellar_analysis_plots/003733735.png',
                                                             show=True)



.. image:: stellar_analysis_framework_files/stellar_analysis_framework_7_0.png


We then save the results to a csv file:

.. code:: ipython3

    fileout = 'stellar_analysis_features/003733735.csv'
    df = msap4.save_features (fileout, 3733735, features, feature_names)

As in the previous tutorial, let’s build a feature catalog. This is
actually not required here because we are analysing only one star, but
this step allows to ROOSTER-analyse several stars together with a simple
framework.

.. code:: ipython3

    df = msap4.build_catalog_features ('stellar_analysis_features')

Then, let’s load the ROOSTER instance that we have trained in the
previous tutorial:

.. code:: ipython3

    chicken = msap4.load_rooster_instance (filename='rooster_instances/rooster_tutorial')

As previously, let’s split the DataFrame into ROOSTER required inputs:

.. code:: ipython3

    target_id, p_candidates, features, feature_names = msap4.create_rooster_feature_inputs (df)

Here, we can see that there is actually (almost) nothing to do, as the
three methods have yielded the same :math:`P_\mathrm{rot}` estimate.
However, we need ROOSTER to provide us with the rotation score of the
target. ROOSTER will also select one of the three ``p_candidates`` as
the final estimate for our target.

.. code:: ipython3

    p_candidates




.. parsed-literal::

    array([[2.55994471, 2.59507401, 2.49252463]])



The ``analyseSet`` function implemented in ROOSTER allows to analyse the
features we extracted with the analysis pipeline. By providing
``feature_names``, we ensure that ROOSTER was trained with the same
features that those we extracted.

.. code:: ipython3

    rotation_score, prot = chicken.analyseSet (features, p_candidates, 
                                               feature_names=feature_names)

We finally get the rotation score and the final :math:`P_\mathrm{rot}`.
A rotation score above 0.5 means that the ROOSTER analysis favours a
detection of stellar surface rotation signal.

.. code:: ipython3

    rotation_score, prot




.. parsed-literal::

    (array([0.78]), array([2.55994471]))



Analysing a PLATO simulated light curves dataset
------------------------------------------------

In order to illustrate the pipeline features described above, we can
apply the pipeline to a larger dataset of 255 PLATO simulated light
curves in order to check what we recover.

.. code:: ipython3

    import plato_msap4_demonstrator_datasets.plato_sim_dataset as plato_sim_dataset
    
    if not os.path.exists ('plato_sim_features') :
        os.mkdir ('plato_sim_features')
    if not os.path.exists ('plato_sim_plots') :
        os.mkdir ('plato_sim_plots')

.. code:: ipython3

    list_id = msap4.get_list_targets (plato_sim_dataset)

Note that in the current version of the demonstrator, we have to apply a
55-day high-pass finite impulse response filter to the simulated light
curves in order to remove low-frequency systematics while preserving at
most the signature of stellar activity in the data. In the future, data
product calibrated specifically for the MSAP4 needs will allow to
significantly improve the analysis performances.

.. code:: ipython3

    for elt in tqdm.tqdm (list_id) :
        str_elt = str (elt).zfill (3)
        fileout = 'plato_sim_features/{}.csv'.format(str_elt)
        filename = msap4.get_target_filename (plato_sim_dataset, str_elt, filetype='csv')
        if not os.path.exists (fileout) :
            t, s, dt = msap4.load_resource (filename)
            (p_ps, p_acf, ps, acf, 
             cs, features, feature_names) = msap4.analysis_pipeline (t, s, periods_in=p_in,
                                                                     wavelet_analysis=False, plot=True,
                                                                     filename='plato_sim_plots/{}.png'.format(str_elt),
                                                                     figsize=(10,16),
                                                                     lw=1, dpi=300, smooth_acf=True)
            df = msap4.save_features (fileout, str_elt, features, feature_names)


.. parsed-literal::

    100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 255/255 [00:00<00:00, 18153.15it/s]


We can now analyse the obtained features with ROOSTER to provide our
final results.

.. code:: ipython3

    df = msap4.build_catalog_features ('plato_sim_features')
    target_id, p_candidates, features, feature_names = msap4.create_rooster_feature_inputs (df)
    rotation_score, prot = chicken.analyseSet (features, p_candidates, 
                                               feature_names=feature_names)
    df




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>prot_ps</th>
          <th>prot_acf</th>
          <th>prot_cs</th>
          <th>e_prot_ps</th>
          <th>E_prot_ps</th>
          <th>e_prot_acf</th>
          <th>E_prot_acf</th>
          <th>e_prot_cs</th>
          <th>E_prot_cs</th>
          <th>sph_ps</th>
          <th>sph_acf</th>
          <th>sph_cs</th>
          <th>h_ps</th>
          <th>fa_prob_ps</th>
          <th>hacf</th>
          <th>gacf</th>
          <th>hcs</th>
        </tr>
        <tr>
          <th>target_id</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>43.384664</td>
          <td>32.228960</td>
          <td>87.711426</td>
          <td>20.246176</td>
          <td>14.461555</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>6.292977</td>
          <td>6.292977</td>
          <td>754.547891</td>
          <td>751.571755</td>
          <td>723.483590</td>
          <td>0.243752</td>
          <td>0.000000e+00</td>
          <td>-0.169809</td>
          <td>0.369845</td>
          <td>0.008731</td>
        </tr>
        <tr>
          <th>1</th>
          <td>33.054982</td>
          <td>31.728964</td>
          <td>2.830888</td>
          <td>17.964664</td>
          <td>16.527491</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>2.274565</td>
          <td>2.274565</td>
          <td>196.002432</td>
          <td>197.555022</td>
          <td>148.933715</td>
          <td>0.016114</td>
          <td>0.000000e+00</td>
          <td>-0.013504</td>
          <td>0.257683</td>
          <td>0.001063</td>
        </tr>
        <tr>
          <th>2</th>
          <td>17.353865</td>
          <td>19.222099</td>
          <td>19.243691</td>
          <td>3.470773</td>
          <td>17.353865</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>2.404119</td>
          <td>2.404119</td>
          <td>130.530199</td>
          <td>131.031710</td>
          <td>131.184711</td>
          <td>0.083866</td>
          <td>0.000000e+00</td>
          <td>0.200975</td>
          <td>0.585560</td>
          <td>0.013326</td>
        </tr>
        <tr>
          <th>3</th>
          <td>21.034988</td>
          <td>21.020699</td>
          <td>20.929529</td>
          <td>4.891858</td>
          <td>10.517494</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>0.723093</td>
          <td>0.723093</td>
          <td>107.469907</td>
          <td>107.480934</td>
          <td>107.611707</td>
          <td>0.152170</td>
          <td>0.000000e+00</td>
          <td>0.599156</td>
          <td>1.246466</td>
          <td>0.089680</td>
        </tr>
        <tr>
          <th>4</th>
          <td>28.923109</td>
          <td>28.228986</td>
          <td>29.242286</td>
          <td>21.123619</td>
          <td>20.659364</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>1.413489</td>
          <td>1.413489</td>
          <td>156.269982</td>
          <td>156.835282</td>
          <td>155.995558</td>
          <td>0.011790</td>
          <td>4.780577e-250</td>
          <td>0.083945</td>
          <td>0.153275</td>
          <td>0.000970</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>250</th>
          <td>31.552483</td>
          <td>30.333139</td>
          <td>31.276773</td>
          <td>9.160398</td>
          <td>11.832181</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>4.148271</td>
          <td>4.148271</td>
          <td>215.787517</td>
          <td>203.448456</td>
          <td>216.580554</td>
          <td>0.160314</td>
          <td>0.000000e+00</td>
          <td>0.631596</td>
          <td>1.252152</td>
          <td>0.097334</td>
        </tr>
        <tr>
          <th>251</th>
          <td>20.416312</td>
          <td>19.722096</td>
          <td>19.781832</td>
          <td>5.647065</td>
          <td>11.136170</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>1.618168</td>
          <td>1.618168</td>
          <td>184.403461</td>
          <td>184.567798</td>
          <td>184.507623</td>
          <td>0.160625</td>
          <td>0.000000e+00</td>
          <td>0.290968</td>
          <td>0.777965</td>
          <td>0.044405</td>
        </tr>
        <tr>
          <th>252</th>
          <td>36.534454</td>
          <td>38.041423</td>
          <td>38.926519</td>
          <td>8.768269</td>
          <td>21.311765</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>4.445496</td>
          <td>4.445496</td>
          <td>1353.429169</td>
          <td>1378.403355</td>
          <td>1391.107551</td>
          <td>0.250936</td>
          <td>0.000000e+00</td>
          <td>0.839154</td>
          <td>1.670667</td>
          <td>0.204054</td>
        </tr>
        <tr>
          <th>253</th>
          <td>17.353865</td>
          <td>18.722102</td>
          <td>18.369722</td>
          <td>4.256609</td>
          <td>12.826770</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>2.325352</td>
          <td>2.325352</td>
          <td>163.173697</td>
          <td>165.172826</td>
          <td>161.430852</td>
          <td>0.078761</td>
          <td>0.000000e+00</td>
          <td>0.234943</td>
          <td>0.619113</td>
          <td>0.015210</td>
        </tr>
        <tr>
          <th>254</th>
          <td>18.760936</td>
          <td>36.840042</td>
          <td>43.380813</td>
          <td>3.991688</td>
          <td>17.773518</td>
          <td>-1.0</td>
          <td>-1.0</td>
          <td>1.799967</td>
          <td>1.799967</td>
          <td>1162.545259</td>
          <td>1175.131698</td>
          <td>1207.042243</td>
          <td>0.253955</td>
          <td>0.000000e+00</td>
          <td>0.375552</td>
          <td>0.893571</td>
          <td>0.024259</td>
        </tr>
      </tbody>
    </table>
    <p>255 rows × 17 columns</p>
    </div>



Next, let’s load the reference catalog for these simulated light curves
in order to compare the results from our pipeline with what was injected
in the data.

.. code:: ipython3

    prot_ref = msap4.get_prot_ref (target_id, catalog='plato-sim')
    cond_0 = (rotation_score>0.5)
    cond_1 = (np.abs (prot - prot_ref) < 0.1 * prot_ref) 
    cond_2 = (np.abs (prot - prot_ref) < 0.1 * prot_ref) & (rotation_score>0.5)
    score_0 = target_id[cond_0].size / target_id.size
    score_1 = target_id[cond_1].size / target_id.size
    score_2 = target_id[cond_2].size / target_id.size
    score_0, score_1, score_2




.. parsed-literal::

    (0.8196078431372549, 0.615686274509804, 0.5803921568627451)



The score computed here means that we were able to successfully detect a
rotation signal and recover the correct rotation period for about **59%
of the stars** in the sample. We can take a look at histograms to check
the rotation score of our population and to compare the input rotation
periods distribution to the one we recover.

.. code:: ipython3

    fig, (ax1, ax2) = plt.subplots (1, 2, figsize=(10, 4))
    
    bins = np.linspace (0, 1, 20, endpoint=False)
    ax1.hist (rotation_score, bins=bins, color='darkorange')
    ax1.axvline (0.5, ls='--', color='blue', lw=2)
    bins = np.linspace (0, 80, 20, endpoint=False)
    ax2.hist (prot, bins=bins, color='darkorange')
    ax2.hist (prot_ref, bins=bins, facecolor='none',
             edgecolor='black', label='Ref')
    
    ax1.set_ylabel (r'Number of stars')
    ax1.set_xlabel (r'Rotation score')
    ax2.set_xlabel (r'$P_\mathrm{rot}$ (day)')
    
    ax1.set_xlim (0, 1)
    ax2.set_xlim (0, 80)




.. parsed-literal::

    (0.0, 80.0)




.. image:: stellar_analysis_framework_files/stellar_analysis_framework_32_1.png


