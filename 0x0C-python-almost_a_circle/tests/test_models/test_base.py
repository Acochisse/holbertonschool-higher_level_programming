#!/usr/bin/python3
"""
unit test for base class
"""
import os
import unittest
import json
from models import base
from models import rectangle
from models import square
Base = base.Base

class TestBase(unittest.TestCase):
    """contains test cases for class base"""

    def test_normal_use(self):
        b = Base(21)
        self.assertEqual(b.id, 21)
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_negative(self):
        b = Base(-3)
        self.assertEqual(b.id, -3)

        b = Base(-23)
        self.assertEqual(b.id, -23)

    def test_float(self):
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

    def test_neg_float(self):
        b = Base(-3.14)
        self.assertEqual(b.id, -3.14)

    def test_complex(self):
        b = Base(2.1e0)
        self.assertEqual(b.id, 2.1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_id_none(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)

    def test_id_string(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")
        b = Base("hello2")
        self.assertEqual(b.id, "hello2")

    def test_type(self):
        b = Base()
        self.assertTrue(type(b) is Base)

    def test_to_json_string(self):
        Base._nb__objects = 0
        d1 = {"id": 1, "width": 3, "height": 4, "x": 5, "y": 6}
        d2 = {"id": 2, "width": 5, "height": 6, "x": 3, "y": 4}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_from_json_string(self):
        Base._nb__objects = 0
        d1 = {"id": 1, "width": 3, "height": 4, "x": 5, "y": 6}
        d2 = {"id": 2, "width": 5, "height": 6, "x": 3, "y": 4}
        json_s = Base.to_json_string([d1, d2])
        json_l = Base.from_json_string(json_s)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0], {'id': 1, 'width': 3, 'height': 4, 'x': 5, 'y': 6})
        self.assertEqual(json_l[1], {'id': 2, 'width': 5, 'height': 6, 'x': 3, 'y': 4})
