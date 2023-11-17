




'''
	python3 status/statuses/vitals/__init__.py "structs/scan/trees_form_1/find/STATUS_name_1.py"
'''


import cyte.structs.DB.access as access
import cyte.structs.scan.trees_form_1 as trees_form_1
import cyte.structs.scan.trees_form_1.find.name as find_name


def check_1 ():
	struct_db = access.DB ()
	trees_form_1_grove = trees_form_1.start (struct_db)

	struct = find_name.start ("vitamin d", trees_form_1_grove)
	assert ('vitamin d' in struct ['names']), struct

	struct = find_name.start ("dietary fiber", trees_form_1_grove)
	assert ('dietary fiber' in struct ['names']), struct
	
	print (struct)


	return;
	
	
checks = {
	"trees form 1, find region": check_1
}