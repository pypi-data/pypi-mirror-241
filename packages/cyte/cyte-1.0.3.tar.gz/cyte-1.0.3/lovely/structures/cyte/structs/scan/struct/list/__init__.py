

'''
	import cyte.structs.DB.access as access
	import cyte.structs.scan.struct.list as structs_list
	list = structs_list.find (access.DB ())
'''


def find (structs_DB, SORT = "region"):
	LIST = structs_DB.all ()
	
	if (SORT == "region"):
		LIST.sort (key = lambda struct : struct [SORT])
	
	return LIST