import unittest
from parking_lot_function import*

class TestParkingLot(unittest.TestCase):
	
	def test_that_function_get_available_spaces_returns_correct_value_if_number_is_one(self):
		actual = get_available_spaces( 1 , 2 , [1, 2 ,3,4,5,6,7,8,9,10])
		expected = [1,3,4,5,6,7,8,9,10]
		self.assertEqual(actual, expected)


	def test_that_function_get_available_spaces_returns_correct_value_if_number_is_two(self):
		actual = get_available_spaces( 2 , 2 , [1, 3, 4, 5])
		expected = [1, 2, 3, 4, 5]
		self.assertEqual(actual, expected)

	def test_if_the_type_inputted_in_function_get_available_spaces_by_the_user_is_an_integer(self):
		wrong_value = "input"

		wrong_value2 = 7.9
		self.assertRaises(TypeError, wrong_value, wrong_value2)

	def test_function_compute_taken_space_returns_correct_value_if_number_is_one(self):
		actual = compute_taken_space(1 , 2 , [0, 0, 0])
		expected = [0,  1 , 0]
		self.assertEqual(actual, expected)

	def test_function_compute_taken_space_returns_correct_value_if_number_is_two(self):
		actual = compute_taken_space(2 , 2 , [0, 0, 0])
		expected = [0,  0 , 0]
		self.assertEqual(actual, expected)

	
	def test_if_the_type_inputted_in_function_compute_taken_space_by_the_user_is_an_integer(self):
		wrong_value = "output"

		wrong_value2 = 9.0
		self.assertRaises(TypeError, wrong_value, wrong_value2)

