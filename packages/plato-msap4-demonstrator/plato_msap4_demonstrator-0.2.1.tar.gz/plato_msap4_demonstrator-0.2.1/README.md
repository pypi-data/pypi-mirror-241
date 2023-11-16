# PLATO MSAP4 demonstrator

The [PLATO](https://platomission.com/) Module for Stellar Analysis Pipeline 4,
currently under development, will be responsible for the analysis of surface
rotation and activity of solar-type stars observed by the mission. 
The present demonstrator provides a complete API to implement the algorithms
that will be part of the pipeline. Several tutorials are included in order 
to help new users to discover the code. 


Some functions of the modules implement algorithms that are currently 
out of the MSAP4 baseline but can provide useful complementary diagnostics.

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
- scikit-image 
- ssqueezepy

### Installing

You can also install the most recent version of the module by cloning the GitLab repository

`git clone https://gitlab.com/sybreton/plato_rotation_pipeline.git`

and installing it directly by going to the root of the cloned repository

`pip install .` 

Some of the tutoriels notebook require additional datasets to be properly run, you can access them through an auxiliary repository

`git clone https://gitlab.com/sybreton/plato_msap4_demonstrator_datasets.git`

that you will also have to install through

`pip install .`

In the future, we plan to provide packaged versions of the pipeline through PyPi and conda-forge.

### Documentation

API Documentation and tutorials are available [here](https://plato-rotation-pipeline.readthedocs.io/en/latest/).

## Authors

* **Sylvain N. Breton** - Maintainer & head developer - (INAF-OACT, Catania, Italy)

Active contributors:

* **Antonino F. Lanza** - Responsible PLATO WP122 - (INAF-OACT, Catania, Italy)
* **Sergio Messina** - Responsible PLATO WP122300 - (INAF-OACT, Catania, Italy)
* **Rafael A. García** - Contributor (CEA Saclay, France) 
* **S. Mathur** - Contributor (IAC Tenerife, Spain) 
* **Angela R.G. Santos** - Contributor (Universidade do Porto, Portugal) 
* **L. Bugnet** - Contributor (ISTA Vienna, Austria) 
* **E. Corsaro** - Contributor (INAF-OACT, Catania, Italy) 

Former contributors:

* **Emile Carinos** - Developer - (CEA Saclay, France)
* **Yassine Dhifaoui** - Developer - (CEA Saclay/Université Clermont-Auvergne, France)

## Acknowledgements 

If you use the PLATO MSAP4 demonstrator in your work, please provide a link to
the GitLab repository. 

You will find references for most of the methods implemented in this module in 
[Breton et al. 2021](https://ui.adsabs.harvard.edu/abs/2021A%26A...647A.125B/abstract) and
in [Santos et al. 2019](https://ui.adsabs.harvard.edu/abs/2019ApJS..244...21S/abstract), if you
make use of the code in view of a scientific publication, please take a look at these two papers 
in order to provide the relevant citations. 

The [*Kepler*](https://www.nasa.gov/mission_pages/kepler/overview/index.html) light curves 
included in the datasets were calibrated with the KEPSEISMIC
method, if you use them, please cite [García et al. 2011](https://ui.adsabs.harvard.edu/abs/2011MNRAS.414L...6G/abstract),
[García et al. 2014](https://ui.adsabs.harvard.edu/abs/2014A%26A...568A..10G/abstract) 
and [Pires et al. 2015](https://ui.adsabs.harvard.edu/abs/2015A%26A...574A..18P/abstract).

The PLATO simulated light curves included in the datasets were produced and detrended
by Suzanne Aigrain and Oscar Barragán. If you make any use of these light curves,
please acknowledge them and cite [Aigrain et al. 2015](https://ui.adsabs.harvard.edu/abs/2015MNRAS.450.3211A/abstract).
For more information about the light curves, a readme file written by S. Aigrain is included.
