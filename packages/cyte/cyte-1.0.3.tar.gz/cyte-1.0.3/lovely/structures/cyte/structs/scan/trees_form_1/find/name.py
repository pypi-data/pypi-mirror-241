

'''
import cyte.structs.scan.trees_form_1.find.name as find_name
struct = find_name.start ("vitamin d", trees_form_1_grove)
'''

import tinydb

def traverse (search_name, grove):
	for struct in grove:
		names = struct ['names']
	
		for name in names:
			if (name == search_name):
				return struct;

		if (len (struct ["includes structs"]) >= 1):
			returns = traverse (search_name, struct ["includes structs"])
			print ("	returns:", type (returns))
			
			if (type (returns) == tinydb.table.Document):
				return returns;
				
	return False


def start (search_name, grove):
	returns = traverse (search_name, grove)
	if (returns == False):
		raise Exception (f"Name '{ search_name }' was not found.")
	
	return returns
	