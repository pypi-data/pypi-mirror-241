

'''
	augment food struct 2 with the newer version
'''

'''
import cyte.hygiene.foods.inventory.doc.augment_every_food_struct_2 as augment_every_food_struct_2
augment_every_food_struct_2.now ()
'''
import cyte.hygiene._system.connect as connect
import cyte.food.USDA.struct_2 as USDA_struct_2
import cyte.hygiene.foods.inventory.doc.augment_food_struct_2 as augment_food_struct_2

import json

def now ():
	[ r, c ] = connect.now ()

	db = "foods"
	table = "inventory"
	emblems = r.db (db).table (table).pluck ('emblem').run (c)

	proceeds = []

	stats = {
		"deleted": 0,
		"errors": 0,
		"inserted": 0,
		"replaced": 0,
		"skipped": 0,
		"unchanged": 0
	}

	for emblem in emblems:
		emblem = emblem ["emblem"]
	
		proceed = augment_food_struct_2.now (emblem)
		
		proceeds.append (proceed)
		for stat in proceed ['update']:
			stats [stat] += proceed ['update'] [stat]  
	
	print (json.dumps (proceeds, indent = 4))
	print (json.dumps (stats, indent = 4))
	
	