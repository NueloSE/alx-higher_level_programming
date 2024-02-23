#!/usr/bin/python3
"""
Unittest for max_integer([ ... ])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A test case class for testing the max_integer function.

    Methods:
        test_normal_list: Test cases for normal integer lists.
        test_mix_character: Test cases
        for lists containing mix of integers and characters.
        test_all_character: Test cases for lists containing only characters.
        test_one_element: Test cases for lists containing only one element.
        test_max_begin: Test cases for lists
        where the maximum integer is at the beginning.
    """
    def test_normal_list(self):
        """
        Test cases for normal integer lists.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, 0, -4]), 0)
        self.assertEqual(max_integer([1, 2, -5, 4.3]), 4.3)
        self.assertEqual(max_integer([1.3, 2.4, 5.1, 3.4, 4.3]), 5.1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_mix_character(self):
        """
        Test case for lists containing mix of integers and characters.
        """
        with self.assertRaises(TypeError):
            max_integer([1, 3, '2'])

    def test_all_character(self):
        """
        Test case for lists containing only characters
        """
        self.assertEqual(max_integer(['a', 'c', 'b']), 'c')

    def test_one_element(self):
        """
        Test cases for lists containing only one element
        """
        self.assertEqual(max_integer([5]), 5)

    def test_max_begin(self):
        """
        Test case for lists wehre the maximum is at the beginning
        """
        self.assertEqual(max_integer([4, 2, 1]), 4)

    def test_list_lists(self):
        """
        Test case when a list contains another list
        """
        with self.assertRaises(TypeError):
            max_integer([2, 1, [4, 5, 6], 5, 3])
