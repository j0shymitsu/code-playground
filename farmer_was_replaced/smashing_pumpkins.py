CURRENT_MAX_X = 7
CURRENT_MAX_Y = 7

PUMPKIN_COORDS = [
	(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
	(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
	(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
	(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
	(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
	(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
]

SUNFLOWER_COORDS = [
	(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
	(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
]

def pumpkin_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Pumpkin:
		use_item(Items.Fertilizer)
	else:
		plant(Entities.Pumpkin)

def carrot_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Carrot:
		use_item(Items.Fertilizer)
	else:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
		
def sunflower_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Sunflower:
		pass
	elif get_entity_type() != None:
		# Harvest any other crop first
		if can_harvest():
			harvest()
	else:
		plant(Entities.Sunflower)

def do_work():
	x = get_pos_x()
	y = get_pos_y()
	curr_coords = (x, y)
	
	if get_ground_type() != Grounds.Soil:
		till()
	
	if curr_coords in SUNFLOWER_COORDS:
		sunflower_plant()
	elif curr_coords in PUMPKIN_COORDS:
		pumpkin_plant()
	else:
		carrot_plant()

def traverse_row(direction, target_x):
	while get_pos_x() != target_x:
		move(direction)
		do_work()

while True:
	if get_pos_x() == 0 and get_pos_y() == 0:
		do_a_flip()
	
	do_work()
	traverse_row(East, CURRENT_MAX_X)
	move(North)
	do_work()
	traverse_row(West, 0)
	
	if get_pos_y() < CURRENT_MAX_Y:
		move(North)