#!/usr/bin/env python

"""
Basic unit tests to ensure stability in the pokebase classes
and ensure variables haven't changed at the endpoint level.

Note that using unittest requires creating classes to run the tests
by inheriting from unittest.TestCase and prefers using its own assert
methods instead of the regular assert() call.

As bugs are reported, the test suite will grow more robust.
"""

import unittest
import sys
import os
import requests

# Import api_modules/api using paths to ensure directory is found
sys.path.append(".")

import pokewrap as api

# Set up a test instance of ApiController for use in testing
TEST_NUM = 94
TEST_POKEMON = "gengar"
TEST_OBJECT = api.ApiController("pokemon", TEST_POKEMON)


class TestApi(unittest.TestCase):
    """Basic tests to confirm variables and setup
    of pokewrap are functional and up to date
    """

    # --- Test globals ---
    def test_api_uri(self):
        """Api uri stub in module == correct PokeAPI url
        """
        api_uri = api.API_URI_STUB
        self.assertEqual(api_uri, "https://pokeapi.co/api/v2")

    # --- Test instantiation of ApiController objects ---
    def test_correct_cache_path(self):
        """Tests that cache path loaded correctly
        into ApiController object
        """
        cwd = os.getcwd()
        cache_path = os.path.join(cwd, "cache.json")
        self.assertEqual(TEST_OBJECT.cache_path, cache_path)

    def test_correct_url(self):
        """Tests that the resource url inside ApiController
        object is generated correctly
        """
        real_url = "/".join(("https://pokeapi.co/api/v2",
                             "pokemon",
                             TEST_POKEMON))
        self.assertEqual(TEST_OBJECT.url, real_url)

    def test_id_exists(self):
        """Tests if id value is generated correctly in ApiController

        Also confirms that _convert_id_to_name and
        _convert_name_to_id internal methods are working
        """
        self.assertEqual(TEST_OBJECT.id, TEST_NUM)

    def test_is_resources_empty(self):
        """Tests that the ApiController object gets instantiated
        correctly and generates the right values
        """
        self.assertNotEqual(TEST_OBJECT.content_dict, {})

    def test_name_exists(self):
        """Tests if name value is generated correctly in ApiController

        Also confirms that _convert_id_to_name and
        _convert_name_to_id internal methods are working
        """
        self.assertEqual(TEST_OBJECT.name, TEST_POKEMON)

    def test_object_type_matches(self):
        """Tests that the type of resource brought into ApiController
        exists inside RESOURCE_TYPE tuple
        """
        self.assertIn(TEST_OBJECT.resource, api.RESOURCE_TYPES)

    # --- Test API calls ---
    def test_endpoint_validity(self):
        """Tests whether all endpoints in RESOURCE_TYPES
        are valid and return 200 code
        """
        try:
            response = requests.get(api.API_URI_STUB, timeout=10)
            response.raise_for_status()
            key_set = response.json().keys()

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

        self.assertTrue(set(key_set).issuperset(set(api.RESOURCE_TYPES)))


if __name__ == "__main__":
    unittest.main()
