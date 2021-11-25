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
import pathlib

from dotenv import loadenv

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

env_path = pathlib.Path('../../', '.env')
loadenv(dotenv_path=env_path)

# -- Project information -----------------------------------------------------

project = 'Hangman'
copyright = '2021, Nabil Adnan'
author = 'Nabil Adnan'

# The full version, including alpha/beta/rc tags
release = 'v2.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinxemoji.sphinxemoji',
    'sphinxcontrib.confluencebuilder',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Emoji styles
sphinxemoji_style = 'twemoji'


# Confluence
confluence_publish = True
confluence_page_hierarchy = True
confluence_space_name = os.getenv('CONFLUENCE_SPACE_NAME')
confluence_parent_page = os.getenv('CONFLUENCE_PARENT_PAGE')
confluence_server_url = os.getenv('CONFLUENCE_SERVER_URL')
confluence_server_user = os.getenv('CONFLUENCE_SERVER_USER')
confluence_server_pass = os.getenv('CONFLUENCE_SERVER_PASS')

