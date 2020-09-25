#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal_use(self):
        self.assertEqual(max_integer(list=[1, 2, 3, 4]), 4)

    def no_imput(self):
        self.assertFalse(max_integer())

    def empty_list(self):
        self.assertFalse(max_integer([]))

    def negative_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def duplicates(self):
        self.assertEqual(max_integer([1, 2, 4, 4]), 4)

    def one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def long_value(self):
        self.assertEqual(max_integer([1000, 10000, 100000,\
                                            1000000]), 1000000)

    def no_int_in_list(self):
        with self.assertRaises(TypeError):
            max_integer(["i", 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
