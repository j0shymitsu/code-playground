CURRENT_MAX_X = 5
CURRENT_MAX_Y = 5

PUMPKIN_COORDS = [
	(0, 0),
	(0, 1),
	(0, 2),
	(1, 0),
	(1, 1),
	(1, 2),
	(2, 0),
	(2, 1),
	(2, 2),
	(3, 5),
	(4, 5),
	(3, 4),
	(4, 4), 
	(5, 4),
	(3, 3),
	(4, 3), 
	(5, 3),
	(5, 5)
]

TREE_COORDS = [
	(3, 0),
	(3, 2),
	(5, 0),
	(5, 2),
	(0, 5),
]

HAY_COORDS = [
	(4, 0),
	(3, 1),
	(4, 1),
	(5, 1),
	(4, 2)
]

CARROT_COORDS = [
	(0, 3),
	(1, 3),
	(2, 3),
	(0, 4),
	(1, 4),
	(2, 4),
	(1, 5),
	(2, 5),
]

def hay_plant():
	if can_harvest():
		harvest()
	elif get_ground_type() == Grounds.Soil:
		till()
	elif get_entity_type() == Entities.Grass:
		use_item(Items.Fertilizer)
	else:
		plant(Entities.Grass) 

def tree_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Tree:
		use_item(Items.Fertilizer)
	else:
		plant(Entities.Tree)  

def carrot_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Carrot:
		use_item(Items.Fertilizer)
	else:
		plant(Entities.Carrot)   

def pumpkin_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Pumpkin:
		use_item(Items.Fertilizer)
	else:
		plant(Entities.Pumpkin)

def get_current_coords():
	x = get_pos_x()
	y = get_pos_y()
	return x, y

def do_work():
	for item in PUMPKIN_COORDS:
		if get_current_coords() == item:
			pumpkin_plant()
	for item in TREE_COORDS:
		if get_current_coords() == item:
			tree_plant()
	for item in HAY_COORDS:
		if get_current_coords() == item:
			hay_plant()
	for item in CARROT_COORDS:
		if get_current_coords() == item:
			carrot_plant()

def traverse_row(direction, target_x):		# Move til boundary
	while get_pos_x() != target_x:
		move(direction)
		do_work()

while(True):
	if get_current_coords() == (0, 0):
		do_a_flip()
	traverse_row(East, CURRENT_MAX_X)
	move(North)
	do_work()
	traverse_row(West, 0)
	move(North)
	do_work()


	
		
		
	

