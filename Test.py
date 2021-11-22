#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import multiply

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        x = 20
        y = 40
        result = multiply(x,y)
        self.assertEqual(result, 800)
        x = 0
        y = 451
        result = multiply(x,y)
        self.assertEqual(result, 0)
        x = 12
        y = 12
        result = multiply(x,y)
        self.assertEqual(result, 144)
        x = 6
        y = 5
        result = multiply(x,y)
        self.assertEqual(result, 30)
        x = 11
        y = 5
        result = multiply(x,y)
        self.assertEqual(result, 55)


if __name__ == '__main__':
    unittest.main()
