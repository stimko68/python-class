"""
Example module for running unit tests against other modules you've written. It uses Python's
built-in unittest library which contains a nice toolset for writing unit tests.

To execute your unit tests, install a library called nose using pip

    `pip install nose`

Then execute by using the command "nosetests"

    `nosetests -v -w test`

The -w parameter is the path to the folder that contains your unit test modules. Nose will
execute all of your unit tests and then
"""
import unittest

import lesson_2.star_wars_character_manager as sw_char_mgr

class SWCharacterManagerTest(unittest.TestCase):

    def setUp(self):
        """
        Perform setup tasks for the unit tests
        """
        self.swdbmgr = sw_char_mgr.StarWarsCharacterManager()

    def test_add_new_character(self):
        """
        Add a new character
        """


    def test_get_pk(self):
        """
        Retrieve the primary key of a DB object
        """
        table = 'player'
        query_params = {'name': 'C3PO'}

        pk = self.swdbmgr.get_pk(table, **query_params)
        self.assertIsNotNone(pk)
        self.assertEqual(pk, 1)

    def test_get_pk_returns_None(self):
        """
        Retrieve primary key for a non-existent object
        """
        table = 'player'
        query_params = {'name': 'Barry White'}

        pk = self.swdbmgr.get_pk(table, **query_params)
        self.assertIsNone(pk)