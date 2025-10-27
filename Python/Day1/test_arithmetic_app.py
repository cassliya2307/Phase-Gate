import unittest

from arithmetic_app_function import*


class TestArithmeticDisplayApp(unittest.TestCase):


	def test_for_invalid_input(self):
		wrong_input = 12.8
		wrong_input = "name"	
		self.assertRaises(TypeError, wrong_input, wrong_input)

	def test_for_invalid_return_type(self):
		wrong_return = "anime"
		wrong_return = [2, 7]
		self.assertRaises(TypeError, wrong_return, wrong_return)
	


	#def test_that_the_solution_does_not_generate_negative_number(self):
		#wrong_value = -1
		#self.assertRaises(ValueError, wrong_value)


	