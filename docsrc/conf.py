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
# import UsrIntel.R1
import os
import sys

# sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0, '/usr/intel/pkgs/python3/3.7.4/modules/r1/lib/python3.7/site-packages')
sys.path.insert(0, '/nfs/pdx/disks/dts_cds_fe_81/hls/virtualenvs/sphinx/lib/python3.8/site-packages')
for p in sys.path:
    print(p)
    
# -- Project information -----------------------------------------------------

project = 'SmartRun Feature Sets for Machine Learning '
copyright = '2023, Bob Condon'
author = 'Bob Condon'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel',
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosummary',
              'sphinx.ext.mathjax',
              'sphinx.ext.todo'
              ]
        #  ,
        #  'sphinxcontrib.wavedrom',
        #  'sphinxcontrib.plantuml',
        #  'sphinxcontrib.images',
        #  'breathe',
        #  'hieroglyph'
# breathe_default_project = "HLSTraining"
import sys

source_parsers = {
    '.md' : 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#html_theme = 'groundwork'
#html_logo = 'cheetah.png'
#html_favicon = 'cheetah.ico'

#html_theme_options = {
#    "sidebar_width": '60px',
#    "stickysidebar": True,
#    "stickysidebarscrollable": True,
#    "contribute": False,
#}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

todo_include_todos = True


