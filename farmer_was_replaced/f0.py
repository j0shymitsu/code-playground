CURRENT_MAX_X = 5

def tree_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Tree:
		use_item(Items.Water)
	else:
		plant(Entities.Tree)  

def carrot_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Carrot:
		use_item(Items.Water)
	else:
		plant(Entities.Carrot)   

while(True):
	moving_east = True
	
	while (get_pos_x() < CURRENT_MAX_X) and moving_east:
		move(East)
		if get_ground_type() != Grounds.Soil:
			till()
		elif get_pos_x() % 2 == 0:
			tree_plant()
		else:
			carrot_plant()
	move(North)
	if get_ground_type() != Grounds.Soil:
		till()
	elif get_pos_x() % 2 == 0:
		tree_plant()
	else:
		carrot_plant()
	moving_east = False
	while (get_pos_x() > 0) and not moving_east:
		move(West)
		if get_ground_type() != Grounds.Soil:
			till()
		elif get_pos_x() % 2 == 0:
			tree_plant()
		else:
			carrot_plant()
	move(North)
	if get_ground_type() != Grounds.Soil:
		till()
	elif get_pos_x() % 2 == 0:
		tree_plant()
	else:
		carrot_plant()

	
		
		
	

