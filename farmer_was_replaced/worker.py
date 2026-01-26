CURRENT_MAX_X = 7
CURRENT_MAX_Y = 7

# Two 4×4 pumpkin patches (insurance against 20% death rate)
PUMPKIN_COORDS = [
	(0, 0), (1, 0), (2, 0), (3, 0),
	(0, 1), (1, 1), (2, 1), (3, 1),
	(0, 2), (1, 2), (2, 2), (3, 2),
	(0, 3), (1, 3), (2, 3), (3, 3),
	(0, 4), (1, 4), (2, 4), (3, 4),
	(0, 5), (1, 5), (2, 5), (3, 5),
	(0, 6), (1, 6), (2, 6), (3, 6),
	(0, 7), (1, 7), (2, 7), (3, 7),
]

# 10+ sunflowers for 8× power bonus (12 total)
SUNFLOWER_COORDS = [
	(4, 0), (4, 1), (4, 2), (4, 3),
	(4, 4), (4, 5), (4, 6), (4, 7),
	(5, 0), (5, 2), (5, 4), (5, 6),
]

# Trees in gaps (8 total, spaced)
TREE_COORDS = [
	(6, 0), (6, 2), (6, 4), (6, 6),
	(7, 1), (7, 3), (7, 5), (7, 7),
]

# Carrots (8 tiles)
CARROT_COORDS = [
	(5, 1), (5, 3), (5, 5), (5, 7),
	(6, 1), (6, 3), (6, 5), (6, 7),
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
	elif get_ground_type() != Grounds.Soil:
		till()
	elif get_entity_type() == Entities.Carrot:
		if get_water() < 0.5:
			use_item(Items.Water)
		use_item(Items.Fertilizer)
	else:
		plant(Entities.Carrot)

def sunflower_plant():
	curr_coords = get_current_coords()
	
	if can_harvest():
		# Measure and store petal count
		petals = measure()
	elif get_entity_type() == Entities.Sunflower:
		# Measure growing sunflowers
		petals = measure()
		use_item(Items.Fertilizer)
	else:
		plant(Entities.Sunflower)

def pumpkin_plant():
	if can_harvest():
		harvest()
	elif get_entity_type() == Entities.Pumpkin:
		if get_water() < 0.5:
			use_item(Items.Water)
		use_item(Items.Fertilizer)
	elif get_entity_type() != Entities.Pumpkin:
		if num_items(Items.Carrot) > 100:
			plant(Entities.Pumpkin)

def get_current_coords():
	x = get_pos_x()
	y = get_pos_y()
	return x, y

def do_work():
	curr_coords = get_current_coords()
	
	if curr_coords in CARROT_COORDS:
		carrot_plant()
	elif curr_coords in TREE_COORDS:
		tree_plant()
	elif curr_coords in PUMPKIN_COORDS:
		pumpkin_plant()

def traverse_row(direction, target_x):
	while get_pos_x() != target_x:
		move(direction)
		do_work()

while True:
	if get_current_coords() == (0, 0):
		do_a_flip()
		
		# Harvest optimal sunflower for 8× power bonus
		harvest_optimal_sunflower()
	
	traverse_row(East, CURRENT_MAX_X)
	move(North)
	do_work()
	traverse_row(West, 0)
	
	if get_pos_y() < CURRENT_MAX_Y:
		move(North)
		do_work()
		