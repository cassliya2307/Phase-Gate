def get_products(product):
	
		
	return product


def get_price(price):
	
		
	return price

def calculate_price(get_price):
	prices = get_price
	sum_of_prices = 0
	for item in prices:
		sum_of_prices += item

	return sum_of_prices

def calculate_VAT(calculate_price):
	cost = calculate_price
	VAT_price = 0.075 * cost
	return VAT_price

def final_cost(calculate_price , calculate_VAT):
	price = calculate_price
	cost = calculate_VAT
	total_cost = price + cost
	return total_cost

def get_balance(payment , final_cost):
	cost = final_cost
	total = payment - cost
	return total
	