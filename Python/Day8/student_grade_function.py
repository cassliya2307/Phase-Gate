
def get_number_of_students(student):
	students = []
	for num in range(student):
		students.append(student)
	return students


def calculate_the_sum_of_grades(grade):
	additions = []
	for num in grade:
		sum = 0
		for digit in num:
			sum += digit
			
		additions.append(sum)		
	return additions

def calculate_average_of_grades(calculate_the_sum_of_grades , subject):
	sum = calculate_the_sum_of_grades 
	average_list = []
	for num in sum:
		average = 0
		average = f"{num / subject:.1f}"
		
		average_list.append(float(average))
	return average_list

def get_subject_list(list , subject):
	list2 = []
	count = 0
	for number in range(subject):
		new_list = []
		for num in range(len(list)):
			new_list.append(list[num][count])
		list2.append(new_list)
		count += 1
	return list2


def calculate_highest(my_list):
	highest = my_list[0]
	for num in my_list:
		if num > highest:
			highest = num

	return highest
		
def get_highest_in_each_subject(subject):
	sub_list = []
	
	for numbers in subject:
		sub_list.append(calculate_highest(numbers))
	return sub_list

def calculate_lowest_list(my_list):
	lowest = my_list[0]
	for digits in my_list:
		if digits < lowest:
			lowest = digits
	return lowest

def get_lowest_in_each_subjects(subject):
	sub_list = []
	for num in subject:
		sub_list.append(calculate_lowest_list(num))
	return sub_list

def total_of_each_subject_score(sub_list , subject):
	total = []
	
	
	for number in sub_list:
		sum = 0
		for num in number:
			sum += num
		total.append(sum)
		
	return total


	
def get_average_of_each_subject(sub_list , subject):
	total = total_of_each_subject_score(sub_list , subject)
	average_list = []
	for num in total:
		average = f"{num / subject:.1f}"
		
		average_list.append(float(average))

	return average_list


def get_pass(my_list, average):
	passes = 0
	for number in my_list:
		if number >= average:
			passes += 1
	return passes
def get_total_pass(my_list, my_list_average):
	new_list = []
	count = 0;
	for numbers in my_list:
		new_list.append(get_pass(numbers, my_list_average[count]))
		count += 1
	return new_list





def get_fail(my_list, average):
	fails = 0
	for number in my_list:
		if number < average:
			fails += 1
	return fails
def get_total_fails(my_list, my_list_average):
	new_list = []
	count = 0;
	for numbers in my_list:
		new_list.append(get_fail(numbers, my_list_average[count]))
		count += 1
	return new_list


def get_hardest_subject(fail_list):
	hardest = fail_list[0]
	for numbers in fail_list:
		if numbers > hardest:
			hardest = numbers
	return hardest , fail_list.index(hardest) + 1
		

def get_easiest_subject(pass_list):
	easiest = pass_list[0]
	for numbers in pass_list:
		if numbers > easiest:
			easiest = numbers
	return easiest , pass_list.index(easiest) + 1
		

	

def get_highest_sum_of_subjects(total_list):
	first_total = total_list[0]
	for numbers in total_list:
		if numbers > first_total:
			first_total = numbers
	return first_total , total_list.index(first_total) + 1



def calculate_the_highest_total(grade):
	total = calculate_the_sum_of_grades(grade)
	highest = total[0]
	for num in total:
		if num > highest:
			highest = num
	return highest , total.index(highest) + 1


def calculate_the_lowest_total(grade):
	total = calculate_the_sum_of_grades(grade)
	lowest = total[0]
	for num in total:
		if num < lowest:
			lowest = num
	return lowest , total.index(lowest) + 1

def calculate_overall_class_total(my_list):
	sum = 0
	for num in my_list:
		sum += num
	return sum
	


