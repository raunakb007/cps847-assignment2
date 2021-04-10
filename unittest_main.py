import unittest

import main

class TestMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add_ints(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(main.subtract_ints(24, 20), 4)

    def test_multiply(self):
        self.assertEqual(main.multiply_ints(5, 5), 25)

    def test_divide(self):
        self.assertEqual(main.divide_ints(12, 3), 4.0)

    def test_is_greater_than_true(self):
        self.assertTrue(main.is_greater_than(100, 5))

    def test_is_greater_than_false(self):
        self.assertFalse(main.is_greater_than(10, 500))

if __name__ == '__main__':
    unittest.main()
