import unittest
from perfect_square import*

class TestPerfectTest(unittest.TestCase):
	def test_that_the_function_is_returning_a_list(self):
		actual = get_perfect_square([4])
		expected = [True]
		self.assertEqual(actual , expected)



	def test_that_the_element_is_3_return_false(self):
		actual = get_perfect_square([3])
		expected = [False]
		self.assertEqual(actual , expected)


