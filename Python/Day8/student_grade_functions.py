def subject_score_space(subjects):
	subject_list = []
	for letters in range(len(subjects)):
		subject_list.append([])
	return subject_list

def get_student_score_in_each_subject(sub_list):
	rows = len(sub_list)
	column = len(sub_list[0])
	new_list = []
	for index in range(column):
		new_inner_list = []
		for row in range(rows):
			new_inner_list.append(sub_list[row][index])
		new_list.append(new_inner_list)
	return new_list


def get_subject_total_for_each_student(sub_list):
	sums_list = []
	for num in sub_list:
		sum = 0
		for number in num:
			sum += number 
		sums_list.append(sum)
	return sums_list


def get_subject_average_for_each_student(sub_list):
	total = get_subject_total_for_each_student(sub_list)
	new_list = []
	for num in total:
		average = f"{num / len(total):.1f}"
		new_list.append(average)
	return new_list

def get_student_records(sub_list ,name_list, subject_list):
	total = get_subject_total_for_each_student(sub_list)
	average = get_subject_average_for_each_student(sub_list)
	record_list = []
	for num in range(len(name_list)):
		new_list = []
		new_list.append(name_list[num])
		for number in range(len(subject_list)):
			new_list.append(sub_list[num][number])
		new_list.append(total[num])
		new_list.append(average[num])
		record_list.append(new_list)
	return record_list


def get_number_of_passes(sub_list):
	pass_list = []
	for num in sub_list:
		passes = 0
		for number in num:
			if number >= 40.0:
				passes += 1
		pass_list.append(passes)
	return pass_list

def get_number_of_failes(sub_list):
	fails_list = []
	for num in sub_list:
		fails = 0
		for number in num:
			if number < 40.0:
				fails += 1
		fails_list.append(fails)
	return fails_list

def get_hardest_subject(sub_list):
	fails = get_number_of_failes(sub_list)
	hardest = fails[0]
	for num in fails:
		if num > hardest:
			hardest = num
		return hardest , fails.index(hardest)

def get_easiest_subject(sub_list):
	passes = get_number_of_passes(sub_list)
	easiest = passes[0]
	for num in passes:
		if num > easiest:
			hardest = num
	return easiest , passes.index(easiest) + 1









