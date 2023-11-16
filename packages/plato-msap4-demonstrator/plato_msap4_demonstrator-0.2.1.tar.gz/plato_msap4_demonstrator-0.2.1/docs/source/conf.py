# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution("plato_msap4_demonstrator").version
except DistributionNotFound:
    __version__ = "unknown version"
sys.path.insert(0, os.path.abspath('.'))

autodoc_mock_imports = ['numpy', 'scipy', 'matplotlib', 'pymc3',
                        'corner', 'emcee', 'pandas', 'astropy',
                        'george', 'tqdm', 'dill', 'pathos',
                        'h5py', 'numba', 'statsmodels',
                        'sklearn', 'apollinaire', 'numdifftools',
                        'skimage', 'ssqueezepy']

# -- Project information -----------------------------------------------------

project = 'plato_msap4_demonstrator'
copyright = '2022, Sylvain N. Breton'
author = 'Sylvain N. Breton'
master_doc = 'index'
source_suffix = ".rst"

# The full version, including alpha/beta/rc tags
release = __version__
version = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.mathjax',
              'sphinx_book_theme',
              'IPython.sphinxext.ipython_console_highlighting']

napoleon_numpy_docstring = True


# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = "PLATO MSAP4 demonstrator"
html_logo = "plato_logo_320x320.png"
html_theme_options = {
     "path_to_docs": "docs",
     "repository_url": "https://gitlab.com/sybreton/plato_rotation_pipeline/",
     "use_repository_button": True,
     "use_download_button": True,
     }
html_sidebars = {
    "**": [
     "navbar-logo.html",
     "search-field.html",
     "sbt-sidebar-nav.html",
          ]
     }
numpydoc_show_class_members = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
