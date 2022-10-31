#!/usr/bin/python3
"""
A module that tests the Rectngle class that inherits
from Base class
"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangleClass(unittest.TestCase):
    """
    Class that defines methods to test functionality
    of Rectangle class
    """

    def test_base_instance(self):
        """
        method to test that rectangle inherits from
        Base class
        """

        rec = Rectangle(10, 56, 0, 0, None)
        self.assertEqual((isinstance(rec, Base)
                          and type(rec).__name__ != Base.__name__) , True)

    def test_rectangle_id(self):
        """
        Ensure Rectangle id is correctly set using
        Base class __init__ magin method
        """

        r1 = Rectangle(10, 10, 0, 0)
        r2 = Rectangle(12, 12, 0, 0)
        r3 = Rectangle(23, 89, 0, 0, 12)
        r4 = Rectangle(45, 90, 0, 0)
        ls = [r1.id, r2.id, r3.id, r4.id]
        self.assertEqual(ls, [5, 6, 12, 7], "__init__ malfunctioned")

    def test_attributes_set(self):
        """
        Ensure that private attributes correctly set as arguments
        are passed
        """

        r = Rectangle(12, 6, 1, 5, 2)
        ls = [r.width, r.height, r.x, r.y, r.id]
        self.assertEqual(ls, [12, 6, 1, 5, 2])

    def test_attribute_type(self):
        """
        Ensure that attributes types are either int or floats
        """
        self.assertRaises(TypeError, Rectangle, '12', 6, 0, 0)

    def test_heightsetter(self):
        """
        Ensure that height setters work well
        """

        r = Rectangle(12, 6, 0, 0)
        r.height = 18
        self.assertEqual(r.height, 18)

    def test_heightsetterassert(self):
        """
        Ensure that height setters assert work well
        """

        self.assertRaises(ValueError, Rectangle, -10, 6, 0, 0)

    def test_widthsetters(self):
        """
        Ensure that height setters work well
        """

        r = Rectangle(12, 6, 0, 0)
        r.width = 36
        self.assertEqual(r.width, 36)

    def test_widthsetterassert(self):
        """
        Ensure that height setters assert work well
        """

        self.assertRaises(ValueError, Rectangle, 10, -6, 0, 0)

    def test_xsetters(self):
        """
        Ensure that height setters work well
        """

        r = Rectangle(12, 6, 0, 0)
        r.x = 9
        self.assertEqual(r.x, 9)

    def test_xsetterassert(self):
        """
        Ensure that height setters assert work well
        """

        self.assertRaises(ValueError, Rectangle, 10, 6, -1, 0)


    def test_ysetters(self):
        """
        Ensure that height setters work well
        """

        r = Rectangle(12, 6, 0, 0)
        r.y = 3
        self.assertEqual(r.y, 3)

    def test_ysetterassert(self):
        """
        Ensure that height setters assert work well
        """

        self.assertRaises(ValueError, Rectangle, 10, 6, 0, -1)

    def test_area(self):
        """
        Ensure area method for Rectangle insances is working
        fine
        """

        r = Rectangle(8,7)
        self.assertEqual(r.area(), 56)

if __name__ == '__main__':
    unittest.main()
