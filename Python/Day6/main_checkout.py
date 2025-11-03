from checkout_function import*
product_list = []
price_list = []

while True:
	product = input("Enter product name (or stop): ").lower()
	if product == "stop":
		produce = get_products(product_list)
		cost =  get_price(price_list)
		subtotal = calculate_price(get_price(price_list))
		VAT_total = calculate_VAT(calculate_price(get_price(price_list)))
		final_amount = final_cost(calculate_price(get_price(price_list)) , calculate_VAT(calculate_price(get_price(price_list))))
		count = 0	
		print("			--INVOICE--")		
		for items in range(len(produce)):
			receipt = f"""
		|{produce[count]} : {cost[count]}|
			"""
			count += 1
			print(receipt)	
		receipt2 = f"""
		|Subtotal : N{subtotal}    |
		|VAT(7.5%): N{VAT_total}   |
		|Total    : N{final_amount}|
			"""
		print(receipt2)

		index = 0 
		payment = float(input("Enter payment: "))
		while payment < final_amount:
			print("Your payment is less than the goods bougth")
			payment = float(input("Enter payment: "))
			balance = get_balance(payment , final_amount)


		balance = get_balance(payment , final_amount)

		print("			--PAYMENT RECEIPT--")
		for items in range(len(produce)):
			receipt = f"""
		|{produce[index]} : {cost[index]}|
			"""
			index += 1
			print(receipt)	
		receipt2 = f"""
		|Total Paid  : N{payment}     |
		|Grand Total : N{final_amount}|
		|Balance     : N{balance}     |
			"""
		print(receipt2)
		print("Thanks for shopping!!")

		break

	else:	
		product_list.append(product)
		price = float(input("Enter price of " + product + " : "))
		price_list.append(price)
	
	
	


	