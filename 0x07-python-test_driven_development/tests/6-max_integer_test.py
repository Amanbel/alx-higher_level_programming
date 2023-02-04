#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TetsMaxInteger(unittest.TestCase):
    """class with the unittests"""


    def test_result(self):
        """function to test the result of the function"""
        self.assertAlmostEqual(max_integer([1, 2, 4, 44]), 44)
        self.assertAlmostEqual(max_integer([2, 88, 74, 5]), 88)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([-1, -4, -77]), -1)

    def test_value(self):
        """function to test the value input in the function"""
        self.assertRaises(TypeError, max_integer, [1, 'e', 4, 5])
        self.assertRaises(TypeError, max_integer, [1, "max", 3, 4])
