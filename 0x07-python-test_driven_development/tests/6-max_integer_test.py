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

    def test_list3(self):
        """
        test for list = [-9, -90, -7, -65]
        """
        self.assertEqual(max_integer([-9, -90, -7, -65]), -7, "Should be -7")

    def test_list4(self):
        """
        test for list = [[3]]
        """
        self.assertEqual(max_integer([3]), 3, "should be 3")

    def test_list5(self):
        """
        test for list = [1234, 7, -8, 9]
        """
        self.assertEqual(max_integer([1234, 7, -8, 9]), 1234, "should be 1234")
