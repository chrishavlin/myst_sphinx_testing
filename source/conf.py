# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os
sys.path.append(os.path.abspath('_extension'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'yt-project'
copyright = '2024, yt development team'
author = 'yt development team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_nb",
              "sphinx_design",  # for cards, grids,
              ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {
    "logo": {
        "text": "yt Project",
        "image_light": "_static/yt_logo.svg",
        "image_dark": "_static/yt_logo.svg",
    },
    "external_links": [
          {"name": "Data hub", "url": "https://hub.yt/"},
          {"name": "yt blog", "url": "https://blog.yt-project.org/"},
      ],
    "icon_links": [
            {
                "name": "GitHub",
                "url": "https://github.com/yt-project",
                "icon": "fa-brands fa-square-github",
                "type": "fontawesome",
            },
    ]
}
