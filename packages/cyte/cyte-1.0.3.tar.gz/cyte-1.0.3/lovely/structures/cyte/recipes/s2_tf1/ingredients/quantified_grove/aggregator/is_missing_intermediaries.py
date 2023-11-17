
'''

'''


#
#	make sure all ascendants were found, if there's a product
#	attached to the grove struct.
#
#	An exception would imply that something like:
#		Carbs - found
#			Sugars - not found
#				Added Sugars - found
#
#		where "Sugars" is not in the quantified ingredients
#		of the product, but it is in the structs tree.
#
def calc (
	structs, 
	level = 0, 
	ascendents_line = []
):
	indent = " " * (level * 4)
	structs.sort (key = lambda struct : struct ["names"][0])

	for struct in structs:
		if ("found" in struct):
			found = struct ['found']
			ascendents_line.append ({
				"struct": struct,
				"found": True
			})
		else:
			found = "no "
			ascendents_line.append ({
				"struct": struct,
				"found": False
			})
		
		#
		#	make sure all ascendants were found, if there's a product
		#	attached to the grove
		#
		#	An exception would imply that something like:
		#		Carbs - found
		#			Sugars - not found
		#				Added Sugars - found
		#
		#		where "Sugars" is not in the quantified ingredients
		#		of the product, but it is in the structs tree.
		#
		if (found == True):
			for ascendent in ascendents_line:
				assert (ascendent ["found"] == True), ascendents_line
			
		print (f"{ indent }[{ found }] { struct['names'] } { struct['region'] }")

		if ("includes structs" in struct):
			calc (
				struct ["includes structs"], 
				level = (level + 1),
				ascendents_line = ascendents_line
			)