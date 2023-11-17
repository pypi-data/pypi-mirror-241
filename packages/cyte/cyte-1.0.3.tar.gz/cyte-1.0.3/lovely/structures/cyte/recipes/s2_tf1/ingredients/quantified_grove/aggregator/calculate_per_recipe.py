

import json
from fractions import Fraction

def start (
	product_struct,
	packets_count
):
	print ("$ procedure: calculate per package")

	print ("product struct:", json.dumps (product_struct, indent = 4))
	
	try:
		mass_per_package = Fraction (
			product_struct [
				"ingredient"
			] [ "mass" ] [ "per package" ] ["fraction string grams"]
		)
	except Exception as E:
		mass_per_package = 0

	product_struct [ "ingredient" ] [ "mass" ] [ "per recipe" ] = {
		"fraction string grams": str (mass_per_package * packets_count),
		"float string grams": str (float (mass_per_package * packets_count))
	}

	return;