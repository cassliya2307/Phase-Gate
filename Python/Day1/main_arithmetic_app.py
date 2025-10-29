from arithmetic_app_function import*
main = """
1. Display Equations
2.Total mark
0. Exit
"""
score_list = []
loop = True

while loop:
	print(main)
	operation = int(input("Enter operation: "))

	match operation:
		
		case 1:
			first = get_random_equations()
			equation = f"{first[0]} - {first[1]}"
			solution_1 = first[0] - first[1]
			print("1. What is ",equation) 
			answer = int(input("Enter solution: "))
			if answer == solution_1:
				score_list.append(answer)

			while answer != solution_1:
				equation = f"{first[0]} - {first[1]}"
				print("1. What is ",equation) 
				answer = int(input("Enter solution: "))
				solution_two = first[0] - first[1]
				if answer == solution_two:
					score_list.append(answer)

				break
			next = input("Get next question(yes): ").lower()
			match next:
				case "yes":
					second = get_random_equations()
					second_solution = f"{second[0]} - {second[1]}"
					print("2. What is",second_solution) 
					answer = int(input("Enter solution: "))
					solution_2 = second[0] - second[1]
					if answer == solution_2:
						score_list.append(answer)

				
				
					while answer != solution_2:
						second_solution = f"{second[0]} - {second[1]}"
						print("2. What is ",second_solution) 
						answer = int(input("Enter solution: "))
						solution_2 = second[0] - second[1]
						break
						if answer == solution_2:
							score_list.append(answer)
				
					next_2 = input("Get next question(yes): ").lower()
					match next_2:
						case "yes":
							third = get_random_equations()
							third_solution = f"{third[0]} - {third[1]}"
							print("3. What is",third_solution) 
							answer = int(input("Enter solution: "))
							solution_3 = third[0] - third[1]
							if answer == solution_3:
								score_list.append(answer)

						

							while answer != solution_3:
								third_solution = f"{third[0]} - {third[1]}"
								print("3. What is ",third_solution) 
								answer = int(input("Enter solution: "))
								solution_3 = third[0] - third[1]
								break
								if answer == solution_3:
									score_list.append(answer)
				
							next_3 = input("Get next question(yes): ").lower()
							match next_3:
								case "yes":
									fourth = get_random_equations()
									fourth_solution = f"{fourth[0]} - {fourth[1]}"
									print("4. What is",fourth_solution) 
									answer = int(input("Enter solution: "))
									solution_4 = fourth[0] - fourth[1]
									if answer == solution_4:
										score_list.append(answer)
								
									while answer != solution_4:
										fourth_solution = f"{fourth[0]} - {fourth[1]}"
										print("4. What is ",fourth_solution) 
										answer = int(input("Enter solution: "))
										solution_4 = fourth[0] - fourth[1]
										break
										if answer == solution_4:
											score_list.append(answer)
				
									next_4 = input("Get next question(yes): ").lower()
									match next_4:
										case "yes":
											fifth = get_random_equations()
											fifth_solution = f"{fifth[0]} - {fifth[1]}"
											print("5. What is",fifth_solution) 
											answer = int(input("Enter solution: "))
											solution_5 = fifth[0] - fifth[1]
											if answer == solution_5:
												score_list.append(answer)

								
											while answer != solution_5:
												fourth_solution = f"{fifth[0]} - {fifth[1]}"
												print("5. What is ",fifth_solution) 
												answer = int(input("Enter solution: "))
												solution_5 = fifth[0] - fifth[1]
												break
												if answer == solution_5:
													score_list.append(answer)


											next_5 = input("Get next question(yes): ").lower()
											match next_5:
												case "yes":
													sixth = get_random_equations()
													sixth_solution = f"{sixth[0]} - {sixth[1]}"
													print("6. What is",sixth_solution) 
													answer = int(input("Enter solution: "))
													solution_6 = sixth[0] - sixth[1]
													if answer == solution_6	:
														score_list.append(answer)
												
													while answer != solution_6:
														sixth_solution = f"{sixth[0]} - {sixth[1]}"
														print("6. What is ",sixth_solution) 
														answer = int(input("Enter solution: "))
														solution_6 = sixth[0] - sixth[1]
														break
														if answer == solution_6:
															score_list.append(answer)


													next_6 = input("Get next question(yes): ").lower()
													match next_6:
														case "yes":
															seventh = get_random_equations()
															seventh_solution = f"{seventh[0]} - {seventh[1]}"
															print("7. What is",seventh_solution) 
															answer = int(input("Enter solution: "))
															solution_7 = seventh[0] - seventh[1]
															if answer == solution_7:
																score_list.append(answer)
														#case _:print("Questions not answered completely, start all over")

															while answer != solution_7:
																seventh_solution = f"{seventh[0]} - {seventh[1]}"
																print("7. What is ",seventh_solution) 
																answer = int(input("Enter solution: "))
																solution_7 = seventh[0] - seventh[1]
																break
																if answer == solution_7:
																	score_list.append(answer)
																
															next_7 = input("Get next question(yes): ").lower()
															match next_7:
																case "yes":
																	eight = get_random_equations()
																	eight_solution = f"{eight[0]} - {eight[1]}"
																	print("8. What is",eight_solution) 
																	answer = int(input("Enter solution: "))	
																	solution_8 = eight[0] - eight[1]
																	if answer == solution_8:
																		score_list.append(answer)

																	while answer != solution_8:
																		eight_solution = f"{eight[0]} - {eight[1]}"
																		print("8. What is ",eight_solution) 
																		answer = int(input("Enter solution: "))
																		solution_8 = eight[0] - eight[1]
																		break
																		if answer == solution_8:
																			score_list.append(answer)																		
																case _:print("Questions not answered completely, start all over")													

		case 2:
			print("Your total score is:", total_mark(score_list), "out of 8")
		case 0: loop = False


																			
