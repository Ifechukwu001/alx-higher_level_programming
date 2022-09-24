#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_end(self):
        list = [1, 3, 5, 6, 7]
        self.assertEqual(max_integer(list), 7)

    def test_max_beginning(self):
        list = [9, 6, 4, 1, 0]
        self.assertEqual(max_integer(list), 9)

    def test_max_middle(self):
        list = [2, 4, 9, 6, 1]
        self.assertEqual(max_integer(list), 9)

    def test_max_minus(self):
        list = [4, 2, 7, -10, 1]
        self.assertEqual(max_integer(list), 7)

    def test_max_all_minus(self):
        list = [-1, -4, -9, -5, -7]
        self.assertEqual(max_integer(list), -1)

    def test_max_one(self):
        list = [6]
        self.assertEqual(max_integer(list), 6)

    def test_max_none(self):
        list = []
        self.assertEqual(max_integer(list), None)
