

'''
	augment food struct 2 with the newer version
'''

'''
import cyte.hygiene.foods.inventory.doc.augment_food_struct_2 as augment_food_struct_2
augment_food_struct_2.now (1)
'''
import cyte.hygiene._system.connect as connect
import cyte.food.USDA.struct_2 as USDA_struct_2

def now (emblem):
	[ r, c ] = connect.now ()

	db = "foods"
	table = "inventory"
	food = r.db (db).table (table).get (emblem).run (c)

	print ('food', food)

	USDA_food_data = food ["USDA food data"]
	food_struct_2 = USDA_struct_2.calc (USDA_food_data)

	update = r.db (db).table (table).get (emblem).update ({
		"struct_2": food_struct_2
	}).run (c)
	
	
	
	
	print ('updated:', emblem, update)
	
	return {
		"update": update,
		"emblem": emblem
	}
