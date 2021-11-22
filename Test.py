#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import multiply

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        #x = 20
        #y = 40
        result = multiply(20,40)
        self.assertEqual(result, 800)
        #x = 0
        #y = 451
        result = multiply(451,0)
        self.assertEqual(result, 0)
        #x = 12
        #y = 12
        result = multiply(12,12)
        self.assertEqual(result, 144)
        #x = 6
        #y = 5
        result = multiply(6,5)
        self.assertEqual(result, 30)
        result = multiply(5,11)
        self.assertEqual(result, 45)


if __name__ == '__main__':
    unittest.main()
