#!/usr/bin/python3

"""
Unittest for max_integer()
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class for test cases of the function max_integer
    """

    def test_list_of_ints(self):
        """
        Tests with a list of integers
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_list_of_floats(self):
        """
        Tests with a list of floats
        """
        self.assertEqual(max_integer([1.5, 2.4, 3.1]), 3.1)

    def test_empty_list(self):
        """
        Tests with an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_list_of_strings(self):
        """
        Tests with a list of strings
        """
        self.assertEqual(max_integer(['-1.5', '-2.4', '-3.1']), '-3.1')

    def test_list_of_booleans(self):
        """
        Tests with a list of booleans
        """
        self.assertEqual(max_integer([True, False]), True)

    def test_none_argumenet(self):
        """
        Tests with None argument
        """
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
