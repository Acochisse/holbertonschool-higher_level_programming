#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_use(self):
        self.assertEqual(max_integer(list=[1, 2, 3, 4]), 4)

    def test_no_imput(self):
        self.assertFalse(max_integer())

    def test_empty_list(self):
        self.assertFalse(max_integer([]))

    def test_negative_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicates(self):
        self.assertEqual(max_integer([1, 2, 4, 4]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_long_value(self):
        self.assertEqual(max_integer([1000, 10000, 100000,\
                                            1000000]), 1000000)

    def test_no_int_in_list(self):
        with self.assertRaises(TypeError):
            max_integer(["i", 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
