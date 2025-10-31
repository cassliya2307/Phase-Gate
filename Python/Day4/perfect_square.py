def get_perfect_square(numbers):
	divisor = 2
	new_list = numbers
	index = 0
	length = 0
	for num in numbers:
		length += 1
		#print(length)
	
	for num in range(length):
		#print(numbers[num])
		if numbers[num] == 1:
			new_list[index] = True
			index += 1
		else:
			while(numbers[num] % divisor != 0):
				divisor += 1

			base = numbers[num] // divisor
			if(base * base == numbers[num]):
				new_list[index] = True
		
	
			else:
				new_list[index] = False
				
			index += 1
	return new_list


numbers = [1, 4 , 9, 49 , 8 , 100]
print(get_perfect_square(numbers))