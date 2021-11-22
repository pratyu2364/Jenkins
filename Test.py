#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation, multiply

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [23, 31]
        result = summation(data)
        self.assertEqual(result, 54)
        x = 20
        y = 40
        result = multiply(x,y)
        self.assertEqual(result, 800)
        print("Test 2 completed")
        x = 0
        y = 451
        result = multiply(x,y)
        self.assertEqual(result, 0)
        x = 12
        y = 12
        result = multiply(x,y)
        self.assertEqual(result, 144)


if __name__ == '__main__':
    unittest.main()
