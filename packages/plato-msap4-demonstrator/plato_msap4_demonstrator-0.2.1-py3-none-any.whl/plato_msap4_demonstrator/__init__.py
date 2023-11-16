from importlib.metadata import version

__version__ = version ('plato_msap4_demonstrator')

from .rotation_pipeline import *

from .wavelets import *

from .correlation import *

from .lomb_scargle import *

from .rooster import *

from .aux import *

from .background import *

from .morphology import *

import plato_msap4_demonstrator.timeseries 

import plato_msap4_demonstrator.catalogs 

import plato_msap4_demonstrator.rooster_instances 

import plato_msap4_demonstrator.constants 
