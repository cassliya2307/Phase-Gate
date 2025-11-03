import unittest

from checkout_function import*

class TestCheckoutSystem(unittest.TestCase):

	def test_if_get_products_is_returning_a_list(self):
		actual = get_products(["wine"])
		expected = (["wine"])
		self.assertEqual(actual, expected)

	def test_if_get_price_is_returning_a_list(self):
		actual = get_price([2.8])
		expected = ([2.8])
		self.assertEqual(actual, expected)

	def test_that_the_calculate_price_function_is_returning_the_sum_of_the_prices(self):
		actual = calculate_price([200.0 , 900.0])
		expected = (1100.0)
		self.assertEqual(actual, expected)


	def test_that_the_fuction_to_calculate_the_VAT_is_returning_correctly(self):
		actual = calculate_VAT(700.0)
		expected = (52.5)
		self.assertEqual(actual, expected)

	def test_that_final_cost_is_returning_the_overall_price_of_good_inputted_by_the_user(self):
		actual = final_cost(700.0 , 52.5)
		expected = (752.5)
		self.assertEqual(actual, expected)

	def test_that_get_balance_is_returning_the_balance(self):
		actual = get_balance(1000 , 752.5)
		expected = (247.5)
		self.assertEqual(actual, expected)
