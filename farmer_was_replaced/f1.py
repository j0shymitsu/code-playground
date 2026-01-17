CURRENT_MAX_X = 5

def tree_plant():
	if can_harvest():
		harvest()
	else:
		plant(Entities.Carrot)  

def carrot_plant():
	if can_harvest():
		harvest()
	else:
		plant(Entities.Carrot)   

while(True):
	move(North)
	# moving_east = True
	
	# while (get_pos_x() < CURRENT_MAX_X) and moving_east:
	# 	move(East)
	# 	till()
	# move(North)
	# till()
	# moving_east = False
	# while (get_pos_x() > 0) and not moving_east:
	# 	move(West)
	# 	till()
	# move(North)
	# till()
		
		
	

	