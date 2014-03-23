import unittest
from solution import nth_fibonacci


class TestSolution(unittest.TestCase):
    """docstring for NthFibonacciTest"""
    def test_nth_fibonacci_0(self):
        self.assertEqual(1, nth_fibonacci(2))
    def test_nth_fibonacci_1(self):
        self.assertEqual(55, nth_fibonacci(10))

if __name__ == '__main__':
    unittest.main()
