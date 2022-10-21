#!/usr/bin/python3
"""
A module that serves as a unit test for
a function that finds the maximum value
in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class that defines methods to test
    the 'max_integer' class
    """

    def test_empty(self):
        """
        Assures that function returns None on
        empty list
        """
        self.assertEqual(max_integer(), None, "Should be None")

    def test_list1(self):
        """
        tests for list = [1, 2, 3, 4]
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Should be 4")

    def test_list2(self):
        """
        test for list = [1, 3, 4, 2]
        """
        self.assertEqual(max_integer([1, 3, 4, 2]), 4, "Should be 4")
