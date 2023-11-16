# Configuration file for the Sphinx documentation builder
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import tomllib
from datetime import date
from importlib.metadata import version as get_version

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

with open('../pyproject.toml', 'rb') as f:
    project_metadata = tomllib.load(f)['project']

project = 'PyGrates'
author = ', '.join(a['name'] for a in project_metadata['authors'])
copyright = f'2022-{date.today().year} {author}'
release = get_version('pygrates')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

exclude_patterns = ['build']
default_role = 'py:obj'
doctest_global_setup = 'import pygrates as pg'
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
