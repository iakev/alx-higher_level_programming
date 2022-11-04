#!/usr/bin/python3
"""
A module that tests the Square class that inherits
from Rectangle class
"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestSquareClass(unittest.TestCase):
    """
    Class to test Square class
    """
    def test_rectangle_instance(self):
        """
        method to test that Square inherits from
        Rectangle class
        """

        sqr = Square(56, 0, 0, None)
        self.assertEqual((isinstance(sqr, Rectangle)
                          and type(sqr).__name__ != Rectangle.__name__) , True)

    def test_attributes_set(self):
        """
        Ensure that private attributes correctly set as arguments
        are passed
        """

        r = Square(6, 1, 5, 2)
        ls = [r.width, r.height, r.x, r.y, r.id]
        self.assertEqual(ls, [6, 6, 1, 5, 2])

    def test_attribute_type(self):
        """
        Ensure that attributes types are either int or floats
        """
        self.assertRaises(TypeError, Square, '12', 6, 0, 0)

    def test_heightsetter(self):
        """
        Ensure that height setters work well
        """

        r = Square(12, 6, 0)
        r.size = 18
        self.assertEqual(r.size, 18)

    def test_heightsetterassert(self):
        """
        Ensure that height setters assert work well
        """

        self.assertRaises(ValueError, Square, -10, 6, 0, 0)

    def test_widthsetters(self):
        """
        Ensure that height setters work well
        """

        r = Square(12, 0, 0)
        r.size = 36
        self.assertEqual(r.size, 36)

    def test_widthsetterassert(self):
        """
        Ensure that height setters assert work well
        """

        self.assertRaises(ValueError, Square, 10, -6, 0, 0)

    def test_xsetters(self):
        """
        Ensure that height setters work well
        """

        r = Square(12, 6, 0, 0)
        r.x = 9
        self.assertEqual(r.x, 9)

    def test_xsetterassert(self):
        """
        Ensure that height setters assert work well
        """

        self.assertRaises(ValueError, Square, 6, -1, 0)


    def test_ysetters(self):
        """
        Ensure that height setters work well
        """

        r = Square(12, 6, 0, 0)
        r.y = 3
        self.assertEqual(r.y, 3)

    def test_ysetterassert(self):
        """
        Ensure that height setters assert work well
        """

        self.assertRaises(ValueError, Square, 6, 0, -1)

    def test_area(self):
        """
        Ensure area method for Rectangle insances is working
        fine
        """

        r = Square(8,2)
        self.assertEqual(r.area(), 64)


    def test_update(self):
        """
        test update method of Rectangle
        """
        r1 = Square(10, 10, 10)
        r1.update(89, 2)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual([r1.id, r1.width, r1.height, r1.x, r1.y],
                         [89, 4, 2, 1, 3] )

if __name__ == '__main__':
    unittest.main()
