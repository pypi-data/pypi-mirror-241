#!/usr/bin/env python

"""
pokewrap
A small Python wrapper for PokeAPI (https://pokeapi.co)

Usage:
>>> import pokewrap
>>> new_pokemon = pokewrap.ApiController("gengar")
>>> new_pokemon.name
'gengar'
"""

__author__ = "Jason Garvin"
__email__ = "jsongarvin@gmail.com"
__version__ = "1.0.8"
__copyright__ = "Copyright Jason Garvin 2023"
__license__ = "BSD"


from .api import API_URI_STUB, RESOURCE_ENDPOINTS, RESOURCE_TYPES
from .api import ApiController, ApiResourceList
from .wrappers import Pokemon
