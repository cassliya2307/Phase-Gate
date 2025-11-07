from student_grade_function import*

student = int(input("Enter number of students: "))


subjects = int(input("Enter number of subjects: "))

final_grades = get_number_of_students(student)

student_count = 0
grade_count = 0
for num in range(student):
	grade_list = []
	print("Enter subject grade for student ",student_count + 1)
	grade_count = 0
	
	
	for grades in range(subjects):
		print("Enter grade of subject " , grade_count + 1)
		grade = int(input("Enter grade of student: "))
		while grade < 0 or grade > 100:
			print("Grade cannot be outside range (1 - 100)")
			grade = int(input("Enter grade of student: "))
		grade_list.append(grade)
		grade_count += 1
		
	final_grades[student_count] = grade_list
	student_count += 1
	                                                        
add = calculate_the_sum_of_grades(final_grades)
sum = calculate_the_sum_of_grades(final_grades)
new_sum = calculate_the_sum_of_grades(final_grades)
average = calculate_average_of_grades(calculate_the_sum_of_grades(final_grades), subjects)

	
add.sort(reverse = True)
for count in range(len(sum)):
	sum[count] = add.index(sum[count]) + 1
	


print("Students" , end = "   ")
for num in range(1, subjects + 4):
	if num <= subjects:
		print(f"sub{num}" ,end = "     ")
	elif num == subjects + 1:
		print(f"Total" , end = "     ")
	elif num == subjects + 2:
		print(f"Average" , end = "	     ")
	elif num == subjects + 3:
		print(f"Position" , end = "	")

for row in range(student):
	print(" ")
	print(row + 1 , end = "	   ")
	for column in range(subjects):	
		print(final_grades[row][column],end = "         ")
	print(new_sum[row] , end = "          ")
	print(average[row] , end = " 	    ")
	print(sum[row] , end = "        ")
	print(" ")		

print(" 				")
same_subjects = get_subject_list(final_grades , subjects)
same2 = get_subject_list(final_grades , subjects)
highest = get_highest_in_each_subject(same_subjects)
lowest = get_lowest_in_each_subjects(same_subjects)
total = total_of_each_subject_score(same_subjects, subjects)
average = get_average_of_each_subject(same_subjects, subjects)
passed = get_total_pass(same_subjects, average)
failed = get_total_fails(same_subjects,average)

#print(passed)

print("SUBJECT SUMMARY")
sub = []
for num in range(subjects):
	sub = same_subjects[num]
	print(f"Subject{num + 1}" , end = " ")
	print(f"Highest scoring student is: Student {sub.index(highest[num]) + 1 } scoring {highest[num]}")
	print(f"Lowest scoring student is: Student {sub.index(lowest[num]) + 1 } scoring {lowest[num]}")
	print(f"Total: ", total[num])
	print(f"Average: " , average[num])
	print(f"Fails: " , failed[num])
	print(f"Passes: " , passed[num])
	print(" 				")
	
	#sub.clear()



hardest = get_hardest_subject(failed)
easiest = get_easiest_subject(passed)
overall_total = get_highest_sum_of_subjects(highest)
highest_total = calculate_the_highest_total(final_grades)
lowest_total = calculate_the_lowest_total(final_grades)
class_total_score = calculate_overall_class_total(new_sum)
class_average_total = calculate_overall_class_total(average)


print("The hardest subject is Subject " , hardest[1] , " with " , hardest[0], "failures")

print("The easiest subject is Subject ", easiest[1], "with" ,easiest[0], "passes")
print(" 				")


sub2 = []
for num in range(subjects):
	sub2 = same2[num]
	print(f"The overall Highest score is Student {sub2.index(highest[num]) + 1 } in Subject {num + 1} scoring {highest[num]}")
	print(f"The overall Lowest  score is Student {sub2.index(lowest[num]) + 1 } in Subject {num + 1} scoring {lowest[num]}")
	print(" 				")

print("=====================================================================================================================================")
print("CLASS SUMMARY")
print("=====================================================================================================================================")

print(" 				")


print("=====================================================================================================================================")
print(f"The Best Graduating student is Student {highest_total[1]} scoring a total of {highest_total[0]}")
print("=====================================================================================================================================")
print(" 				")



print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(f"The Worst Graduating student is Student {lowest_total[1]} scoring a total of {lowest_total[0]}")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(" 				")



print("=====================================================================================================================================")
print(f"Class Total {class_total_score}")
print(f"Class Total Average {class_average_total}")
print("=====================================================================================================================================")


