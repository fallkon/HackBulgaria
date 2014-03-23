import unittest
from solution import count_vowels

class TestSolution(unittest.TestCase):
	def test_count_volwest_0(self):
		self.assertEqual(2, count_vowels("Python"))

	def test_count_volwest_1(self):
		self.assertEqual(5, count_vowels("alohaloha"))

	def test_count_volwest_2(self):
		self.assertEqual(7, count_vowels("aaaaaaa"))


if __name__ == '__main__':
	unittest.main()