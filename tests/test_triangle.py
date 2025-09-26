"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Lichao Huang"
__version__ = "1.0.0"

import unittest
from abc import ABC, abstractmethod
from shape.shape import Shape
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_init_valid_inputs_attributes_set(self):
        tri = Triangle("Blue", 3, 4, 5)

        self.assertEqual("Blue", tri._color)
        self.assertEqual(3, tri._Triangle__side_1)
        self.assertEqual(4, tri._Triangle__side_2)
        self.assertEqual(5, tri._Triangle__side_3)

    def test_init_invalid_inputs_blank_color(self):
        
        with self.assertRaises(ValueError):
            tri = Triangle("",3 , 4, 5)


    def test_init_invalid_inputs_invalid_side_1(self):
        
        with self.assertRaises(ValueError):
            tri = Triangle("Red","a" , 4, 5)


    def test_init_invalid_inputs_invalid_side_2(self):
        
        with self.assertRaises(ValueError):
            tri = Triangle("Red",3 , "a", 5)


    def test_init_invalid_inputs_invalid_side_3(self):
        
        with self.assertRaises(ValueError):
            tri = Triangle("Red",3 , 4, "a")


    def test_str_return(self):

        tri = Triangle("red", 3, 4, 5)
        strreturn = tri.__str__()
        expect = ("The shape color is red.\n"
                "This triangle has three sides with lengths of 3, 4 and 5 centimeters.")
        self.assertEqual(strreturn, expect)
    

    def test_calculate_area(self):
        tri = Triangle("red", 3, 4, 5)
        calarea = tri.calculate_area
        expectarea = 6.0
        self.assertEqual(calarea, expectarea)

    def test_calculate_perimeter(self):
        tri = Triangle("red", 3, 4, 5)
        calperimeter = tri.calculate_perimeter
        expectperimeter = 12.0
        self.assertEqual(calperimeter, expectperimeter)