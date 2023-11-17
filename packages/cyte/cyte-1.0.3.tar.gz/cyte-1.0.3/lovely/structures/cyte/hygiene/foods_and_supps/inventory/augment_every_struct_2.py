




'''
	augment food struct 2 with the newer version
'''

'''
import cyte.hygiene.foods_and_supps.inventory.augment_every_struct_2 as augment_every_struct_2
augment_every_struct_2.now (db = "supplements")
'''
import cyte.hygiene._system.connect as connect

import cyte.hygiene.foods.inventory.doc.augment_food_struct_2 as augment_food_struct_2
import cyte.hygiene.supplements.inventory.doc.augment_struct_2 as augment_supp_struct_2

import json

def now (
	db = ""
):
	assert (db in [ 'supplements', 'foods' ])

	[ r, c ] = connect.now ()

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
	
		if (db == "foods"):
			proceed = augment_food_struct_2.now (emblem)
		elif (db == "supplements"):
			proceed = augment_supp_struct_2.now (emblem)
		else:
			raise Exception (f"")
		
		proceeds.append (proceed)
		for stat in proceed ['update']:
			stats [stat] += proceed ['update'] [stat]  
	
	print (json.dumps (proceeds, indent = 4))
	print (json.dumps (stats, indent = 4))
	
	