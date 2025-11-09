from student_grade_functions import*
name_list = []
subject_list = []

print("===========SC School Register===========")
while True:
	print(" 						")
	students = input("Enter student name (or stop): ").upper()
	if students == "STOP":
		break
	name_list.append(students)
	
while True:
	print(" 						")
	subjects = input("Enter subject names (or stop): ").upper()
	if subjects == "STOP":
		break
	subject_list.append(subjects)
grade_list = subject_score_space(subject_list)


for score in range(len(subject_list)):
	for num in range(len(name_list)):
		scores = float(input(f"Enter {name_list[num]} score in {subject_list[score]}: "))
		
		while scores < 0 or scores > 100: 
			print("Invalid Input score cannot be outside range (1 - 100)")
			scores =  float(input(f"Enter {name_list[num]} score in {subject_list[score]}: "))

		grade_list[score].append(scores)
       





individual_score_list = get_student_score_in_each_subject(grade_list)



total_scores = get_subject_total_for_each_student(individual_score_list)

average_scores = get_subject_average_for_each_student(individual_score_list)



record = get_student_records(individual_score_list ,name_list, subject_list)

sorted_list = sorted(record, key=lambda inner_list: inner_list[-1], reverse=True)



print("Students" , end = "  ")
for num in range(len(subject_list)):
	print(subject_list[num], end = "     ")
print("SUM" , end = "     ")
print("AVERAGE" , end = "     ")
print("POSITION" , end = "	")
print(" ")

for row in range(len(name_list)):
	
	for column in range(len(subject_list) + 3):
	
		print(sorted_list[row][column], end = "       ")
	print(row + 1, end = "   ")
	print(" ")


summary = input("Enter (1) to see the summary and (0) to exit:  ")

total_subject_scores = get_subject_total_for_each_student(grade_list)
average_subject_scores = get_subject_average_for_each_student(grade_list)
passes = get_number_of_passes(grade_list)
fails = get_number_of_failes(grade_list)
hardest_subject = get_hardest_subject(grade_list)
easiest_subject = get_easiest_subject(grade_list)


match summary:

	case "1":
		print("SUBJECT SUMMARY")
		print(" ")
		for inner_list in grade_list:
        		inner_list.sort(reverse=True)



		for row in range(len(subject_list)):
			highest_list  = sorted(record, key=lambda inner_list: inner_list[row + 1], reverse=True)
			print(f"The highest scoring student in {subject_list[row]} is {highest_list[0][0]}")
			lowest_list = sorted(record, key=lambda inner_list: inner_list[row + 1])
			print(f"The lowest scoring student in {subject_list[row]} is {lowest_list[0][0]}")
			print(f"The total of scores in {subject_list[row]} is {total_subject_scores[row]}")
			print(f"The average of scores in {subject_list[row]} is {average_subject_scores[row]}")
			print(f"The number of passes in {subject_list[row]} is {passes[row]}")
			print(f"The number of fails in {subject_list[row]} is {fails[row]}")
			print(" ")


		print("CLASS SUMMARY")
		print(" ")
		print(f"The hardest subject is subject {subject_list[hardest_subject[1]]}😒")
		print(f"The easiest subject is subject {subject_list[easiest_subject[1]]}😉")
		print(" ")
		best_graduating = sorted(record, key=lambda inner_list: inner_list[-1], reverse=True)
		worst_graduating = sorted(record, key=lambda inner_list: inner_list[-1])
		print(f"The best graduating student is {best_graduating[0][0]} scoring a total of {best_graduating[0][-2]}")
		print(f"The worst graduating student is {worst_graduating[0][0]} scoring a total of {worst_graduating[0][-2]}")
		
		total = 0
		average = 0
		for num in total_subject_scores:
			total += num
			average = f"{total / len(subject_list) :.1f}"
		print(f"Class total : {total}")
	
		print(f"Class avearge : {average}")

	case "0":
		print("Thanks for using our register 😊💕")

	case _:
		print("Wrong Input!")
		summary = input("Enter (1) to see the summary and (0) to exit:  ")
		while summary != "1":
			print("Wrong Input!")
			summary = input("Enter (1) to see the summary and (0) to exit:  ")

	