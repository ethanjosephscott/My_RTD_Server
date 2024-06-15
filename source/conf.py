# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test-project'
copyright = '2024, Ethan Scott'
author = 'Ethan Scott'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme','sphinx_copybutton','sphinx_code_tabs','sphinx_rtd_dark_mode','sphinx_search.extension']
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_dark_mode'
html_theme_options = {
	'logo_only': True,
	'collapse_naviagtion': True,
	'sticky_navigation': True,
	'includehidden': True,
	'navigation_depth': 4,
	'titles_only': False,
}

default_dark_mode = True

html_static_path = ['_static']

def setup(app):
	app.add_css_file("css/customWidth.css")
