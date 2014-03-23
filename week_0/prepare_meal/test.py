import unittest
from solution import prepare_meal

class TestSolution(unittest.TestCase):
	def test_prepare_meal_0(self):
		self.assertEqual('spam ', prepare_meal(3))

	def test_prepare_meal_1(self):
		self.assertEqual('spam spam spam ', prepare_meal(27))

	def test_prepare_meal_2(self):
		self.assertEqual('', prepare_meal(7))

	def test_prepare_meal_3(self):
		self.assertEqual('spam spam and eggs', prepare_meal(45))


	
if __name__ == '__main__':
	unittest.main()
