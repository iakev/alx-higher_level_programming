#!/usr/bin/python3
"""
Module that unit tests the script
at models/bas.py
"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    A class that defines methods to test
    the base class
    """

    def test_public_attribute_id(self):
        """
        Ensure that id is type int
        """
        self.assertEqual(str(type(Base().id)), "<class 'int'>", "should be an integer")

    def test_initialization(self):
        """
        Test initialization function works
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        ls = [b1.id, b2.id, b3.id, b4.id]
        self.assertEqual(ls, [1, 2, 12, 3], "__init__ malfunctioned")

if __name__ == '__main__':
    unittest.main()
