"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = ""
__version__ = ""

import unittest
from shape.shape import Shape
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init_valid_inputs__attributes_set(self):
        rec = Rectangle("Blue", 2, 1)

        self.assertEqual("Blue", rec._color)
        self.assertEqual(2, rec._Rectangle__length)
        self.assertEqual(1, rec._Rectangle__width)


    def test_init_invalid_inputs_blank_color(self):
        
        with self.assertRaises(ValueError):
            rec = Rectangle("", 3, 4)


    def test_init_invalid_inputs_invalid_length(self):
        
        with self.assertRaises(ValueError):
            rec = Rectangle("Red", "a", 4)


    def test_init_invalid_inputs_invalid_width(self):
        
        with self.assertRaises(ValueError):
            rec = Rectangle("Red", 3, "a")


    def test_str_return(self):

        rec = Rectangle("red", 3, 4)
        strreturn = rec.__str__()
        expect = ("The shape color is red.\n"
                "This rectangle has four sides with lengths of 3, 4, 3 and 4 centimeters.")
        self.assertEqual(strreturn, expect)
    

    def test_calculate_area(self):
        rec = Rectangle("red", 3, 4)
        calarea = rec.calculate_area
        expectarea = 12.0
        self.assertEqual(calarea, expectarea)

    def test_calculate_perimeter(self):
        rec = Rectangle("red", 3, 4)
        calperimeter = rec.calculate_perimeter
        expectperimeter = 14.0
        self.assertEqual(calperimeter, expectperimeter)