





'''
import cyte.hygiene.foods_and_supps.inventory.return_emblems as return_emblems
emblems = return_emblems.find (
	db = 'supplements'
)
'''

import cyte.hygiene._system.connect as connect
import cyte.hygiene.__stem.climate as stem_climate

def find (
	db = ''
):
	assert (db in [ 'supplements', 'food' ])

	[ r, c ] = connect.now ()

	table = 'inventory'

	emblems = r.db (db).table (table).order_by ('emblem').pluck ('emblem').map (
		lambda document :
		document ['emblem']
	).run (c)
	
	return list (emblems)
