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

src_root = os.path.abspath('../..')
sys.path.insert(0, src_root)

# noinspection PyUnresolvedReferences
import recommonmark
# noinspection PyUnresolvedReferences
import sphinx_rtd_theme

from xcube_geodb.version import version

# -- Project information -----------------------------------------------------


project = 'geodb'
copyright = '2019, Brockmann Consult GmbH'
author = 'Brockmann Consult GmbH'

# The full version, including alpha/beta/rc tags
release = version

# Title of the document
doc_title = 'geodb Toolkit Documentation'

# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md', '.ipynb']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'sphinx_gallery.gen_gallery',
    'nbsphinx',
    'recommonmark',
]

sphinx_gallery_conf = {
    'examples_dirs': 'examples',   # path to your example scripts
    'gallery_dirs': '_auto_examples',  # path to where to save gallery generated output
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Generate automatic links to the documentation of objects in other projects.
intersphinx_mapping = {
    'matplotlib': ('http://matplotlib.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'geopandas': ('http://geopandas.org/', None),
    'python': ('https://docs.python.org/3/', None),
    'xarray': ('http://xarray.pydata.org/en/stable/', None),
    'zarr': ('https://zarr.readthedocs.io/en/stable/', None),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {

    # General options
    'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': 'white',
    #  WARNING: unsupported theme option 'vcs_pageview_mode' given
    # 'vcs_pageview_mode': '',
    #  WARNING: unsupported theme option 'github_url' given
    # 'github_url': 'https://github.com/dcs4cop/xcube',

    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = project + '-docs'

html_logo = '_static/logo.png'

# -- Options for Autodoc output -------------------------------------------------

autoclass_content = 'class'
autodoc_member_order = 'bysource'
autodoc_inherit_docstrings = True
autodoc_typehints = 'signature'
autodoc_mock_imports = [
    'geopandas',
    'psycopg2',
    'pandas',
    'shapely',
    'dotenv'
]
