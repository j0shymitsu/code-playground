CURRENT_MAX_X = 7
CURRENT_MAX_Y = 7

def traverse_and_till():
	for y in range(CURRENT_MAX_Y + 1):
		if y % 2 == 0:
			for x in range(CURRENT_MAX_X + 1):
				if get_ground_type() != Grounds.Soil:
					till()
				if x < CURRENT_MAX_X:
					move(East)
		else:
			for x in range(CURRENT_MAX_X + 1):
				if get_ground_type() != Grounds.Soil:
					till()
				if x < CURRENT_MAX_X:
					move(West)
		if y < CURRENT_MAX_Y:
			move(North)

traverse_and_till()