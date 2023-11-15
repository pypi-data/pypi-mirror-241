"""
Sets up the package for distribution.
Links necessary files and attaches version information,
package description, and author data.
"""

import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = "1.0.8"
PACKAGE_NAME = "pokewrap"
AUTHOR = "Jason Garvin"
AUTHOR_EMAIL = "jsongarvin@gmail.com"
URL = "https://github.com/jasongarvin/pokewrap"

LICENSE = "MIT License"
DESCRIPTION = """A wrapper library for the PokeAPI making it easier
                 to retrieve and use data from the API endpoint."""
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ["requests"]
SETUP_REQUIRES = ["requests"]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      setup_requires=SETUP_REQUIRES,
      packages=find_packages()
      )
