import unittest
from solution import slope_style_score

class TestSolution(unittest.TestCase):
	def test_slope_style_score_0(self):
		self.assertAlmostEqual(94.66, slope_style_score([94, 95, 95, 95, 90]))

	def test_slope_style_score_1(self):
		self.assertEqual(80.0, slope_style_score([60, 70, 80, 90, 100]))

	def test_slope_style_score_2(self):
		self.assertEqual(93.5, slope_style_score([96, 95.5, 93, 89, 92]))


if __name__ == '__main__':
	unittest.main()