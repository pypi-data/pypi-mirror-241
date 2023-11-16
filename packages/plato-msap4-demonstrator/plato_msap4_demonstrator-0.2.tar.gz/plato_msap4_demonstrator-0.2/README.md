# PLATO MSAP4 demonstrator

## Getting Started

### Prerequisites

The PLATO MSAP4 demonstrator package is written in Python 3.
The following Python package are necessary to use it : 
- numpy
- scipy
- pandas
- matplotlib
- numba
- astropy
- tqdm
- scikit-learn

### Installing

You can also install the most recent version of apollinaire by cloning the GitLab repository

`git clone https://gitlab.com/sybreton/plato_rotation_pipeline.git`

and installing it directly by going to the root of the cloned repository

`pip install .` 

Some of the tutoriels notebook require additional datasets to be properly run, you can access them through an auxiliary repository

`git clone https://gitlab.com/sybreton/plato_msap4_demonstrator_datasets.git`

that you will also have to install through

`pip install .`

In the future, we plan to provide packaged versions of the pipeline through PyPi and conda-forge.

## Authors

* **Sylvain N. Breton** - Maintainer - (INAF -Catania)
* **Antonino F. Lanza** - Developer - (INAF Catania)
* **Sergio Messina** - Developer - (INAF Catania)
* **Yassine Dhifaoui** - Developer - (CEA Saclay/Université Clermont-Auvergne)

## Acknowledgements 

If you use the PLATO MSAP4 demonstrator in your work, please provide a link to
the GitLab repository.  

The *Kepler* light curves included in the datasets were calibrated with the KEPSEISMIC
method, if you use them, please cite [García et al. 2011](https://ui.adsabs.harvard.edu/abs/2011MNRAS.414L...6G/abstract),
[García et al. 2014](https://ui.adsabs.harvard.edu/abs/2014A%26A...568A..10G/abstract) 
and [Pires et al. 2015](https://ui.adsabs.harvard.edu/abs/2015A%26A...574A..18P/abstract).

The PLATO simulated light curves included in the datasets were produced and detrended
by Suzanne Aigrain and Oscar Barragan. If you make any use of these light curves,
please acknowledge them and cite [Aigrain et al. 2015](https://ui.adsabs.harvard.edu/abs/2015MNRAS.450.3211A/abstract).
For more information about the light curves, a readme file written by S. Aigrain is included.
