#!/usr/bin/python3

"""
Unittest for console.py
"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Test the console.py file"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "This test only work in Filestorage")
    def test_filestorage_create(self):
        """
        Tests create command in filestorage
        """

        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd("create City name=\"San Francisco\"")
            city_id = f.getvalue().strip()
            self.assertIn('City.{}'.format(city_id), storage.all().keys())
            console.onecmd('show City {}'.format(city_id))
            self.assertIn("'name': 'San Francisco'", f.getvalue().strip())
            console.onecmd('create User name="Betty" age=89 height=5.7')
            user_id = f.getvalue().strip()
            self.assertIn('User.{}'.format(user_id), storage.all().keys())
            console.onecmd('show User {}'.format(user_id))
            self.assertIn("'name': 'James'", f.getvalue().strip())
            self.assertIn("'age': 17", f.getvalue().strip())
            self.assertIn("'height': 5.9", f.getvalue().strip())
