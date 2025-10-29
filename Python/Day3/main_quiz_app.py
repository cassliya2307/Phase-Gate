from quiz_functions import*
main = """
1.Get Quiz Questions
0.End Game
"""
my_list = []
print(main)
choice = input("Enter choice: ")
is_loop = True
while is_loop:
	match choice:
		case "1":
			print("Here are some quiz questions to keep your brain sharp")
			print()
			questions = display_questions()
			answer = get_answer_choices()
			right_answer = get_right_answer()
			count = 0
			index = 0
			for items in range(0 ,10 , 1):
				print(questions[index])
				print()
				print(answer[index])
				print()
				right_answer[index]
				quiz_answer = input("Enter your choice: ")
				print()
				if quiz_answer == right_answer[index]:			
					my_list.append(quiz_answer)
					print("You are correct /(^-^)/!!!")
				else:
					if quiz_answer != "1" and quiz_answer != "2" and quiz_answer != "3" and  quiz_answer != "4":
						print("Option not available , You're Wrong")
					else:
						print("You are wrong (T-T)")
				index += 1
			for scores in my_list:
				count += 1
			print("You got " ,count, " out of 10 correctly")	
			choice = input("Enter (1) to play again (0) to leave: ")

		case "0":is_loop = False	
		case _:
			print("Invalid Input")
			choice = input("Enter (1) to play again (0) to leave: ")
