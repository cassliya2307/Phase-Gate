from parking_lot_function import*

parking_lot_slot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
available_spots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


main = """
~~Welcome To Bailey's Parking Lot~~
Please Drive With Sanity(Thank You /(^ 3 ^)/)
1.Get Parking Space
2.Leave Parking Space
3.Display Slots
0.Leave parking lot
"""
isLoop = True
while isLoop:
	print(main)

	choice = int(input("Enter your choice: "))

	match choice:
		case 1:			
			slot = int(input("Enter a slot number from (1 - 20): "))
			
			if slot <= 20:
				print(get_available_spaces(choice , slot , parking_lot_slot))

				print(compute_taken_space(choice , slot , available_spots ))

			else:
				print("No such slot")
		case 2:
			slot2 = int(input("Enter a taken slot number from (1 - 20): "))
			if slot2 <= 20:
					#print(get_available_spaces(choice , slot2 , parking_lot_slot))
					print(compute_taken_space(choice ,slot2 , available_spots ))
					
										
			else:
				print("No such slot")

		case 3:
			print(available_spots)

		case 0: isLoop = False


		case _:
			print("Invalid Input")
