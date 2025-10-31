
def get_available_spaces(number , slot , parking_list = []):
	if type(number) and type(slot) == int:
		if number == 1: 
			
			parking_list.remove(slot)
			print("slot taken")
			return parking_list

		else:
			
			parking_list.insert(slot - 1, slot)
			print("slot is now vacant")
			return parking_list
	else:
		raiseTypeError("Invalid Input!!")
		

def compute_taken_space(number , slot , available_spots = []):
	if type(number) and type(slot) == int:
		if number == 1:
				available_spots.pop(slot-1)	
				available_spots.insert(slot-1, 1)
				return available_spots

		else:
			available_spots.pop(slot-1)
			available_spots.insert(slot-1, 0)
			return available_spots

	else: 
		raiseTypeError("Invalid Input!!")
















