# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project: str   = 'V-Plate_detection'
copyright: str = '2022, Herusp'
author: str    = 'Herusp'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions: list[str] = ["sphinx.ext.autodoc",
                         "sphinx.ext.viewcode",
                         "sphinx.ext.napoleon",]
templates_path, exclude_patterns = ['_templates'], []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme: str = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# thus a file named "default.css" will overwrite the builtin "default.css".
html_static_path: list[str] = []
master_doc: str = 'index'

autoclass_content: str          = 'both'
autodoc_mock_imports: list[str] = ["views", "utils", "controller", "model", "yolo_config"]
html_show_sourcelink: bool      = False

autodoc_default_flags: list[str] = ['members']
autodoc_member_order: str        = 'bysource'
autodoc_default_options: dict[str, bool] = {
    'undoc-members':    True,
    "show-inheritance": True
}

add_module_names: bool     = False
autosummary_generate: bool = True

if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath('controller'))
