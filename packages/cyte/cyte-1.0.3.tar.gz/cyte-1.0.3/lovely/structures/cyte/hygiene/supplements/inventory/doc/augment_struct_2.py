

'''
	augment struct 2 with the newer version
'''

'''
import cyte.hygiene.supplements.inventory.doc.augment_struct_2 as augment_supplement_struct_2
augment_supplement_struct_2.now (1)
'''
import cyte.hygiene._system.connect as connect
import cyte.supplements.NIH.struct_2 as struct_2

def now (
	emblem,
	
	records = 1
):
	[ r, c ] = connect.now ()

	db = "supplements"
	table = "inventory"
	product = r.db (db).table (table).get (emblem).run (c)

	NIH_supplement_data = product ["NIH supplement data"]
	struct_2_data = struct_2.calc (NIH_supplement_data)

	update = r.db (db).table (table).get (emblem).update ({
		"struct_2": struct_2_data
	}).run (c)
	
	if (records >= 1):
		print (update)
	
	return {
		"update": update,
		"emblem": emblem
	}
