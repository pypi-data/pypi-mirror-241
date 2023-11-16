__author__ = 'Sylvain N. Breton'
__uri__ = 'https://gitlab.com/sybreton/plato_rotation_pipeline.git'
__license__ = 'CeCILL'
__version__ = '0.1'
__description__ = 'PLATO MSAP4 demonstrator'
__email__ = 'sylvain.breton@cea.fr'

from .rotation_pipeline import *

from .wavelets import *

from .correlation import *

from .lomb_scargle import *

from .rooster import *

from .aux import *

from .background import *

import plato_msap4_demonstrator.timeseries 

import plato_msap4_demonstrator.catalogs 

import plato_msap4_demonstrator.rooster_instances 
