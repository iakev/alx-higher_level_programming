#!/usr/bin/python3
"""
A module that tests the Rectangle class that inherits
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


    def test_update(self):
        """
        test update method of Rectangle
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual([r1.id, r1.width, r1.height, r1.x, r1.y],
                         [89, 4, 2, 1, 3] )

if __name__ == '__main__':
    unittest.main()
