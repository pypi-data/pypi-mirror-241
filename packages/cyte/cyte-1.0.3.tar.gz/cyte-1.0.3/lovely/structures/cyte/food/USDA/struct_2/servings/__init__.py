

'''
	"servingSize": 240,
	"servingSizeUnit": "ml",
'''

'''
	calculates servings per package
'''

import json
from fractions import Fraction

import cyte.volume.swap as VOLUME_swap
import cyte.mass.swap as mass_swap	
	
def calc (usda_food_data, usda_food_data_calculated):
	assert ("servingSize" in usda_food_data)
	assert ("servingSizeUnit" in usda_food_data)
	
	SERVING_SIZE_UNIT = usda_food_data ["servingSizeUnit"]
	SERVING_SIZE = usda_food_data ["servingSize"]
	
	import cyte._interpret.unit_kind as UNIT_kind
	kind = UNIT_kind.calc (SERVING_SIZE_UNIT)
	
	if (kind == "volume"):
		volume = usda_food_data_calculated ["volume"] ["listed"]
	
		if ("per package, in liters" in volume):
			LITERS_PER_SERVING = VOLUME_swap.START ([ SERVING_SIZE, SERVING_SIZE_UNIT ], "LITER")
			
			SERVINGS_PER_PACKAGE = str (
				Fraction (
					Fraction (volume ["per package, in liters"]),
					Fraction (LITERS_PER_SERVING)
				)
			)
		
		else:
			raise Exception ('serving size is in volume, but package volume is not known.')
		
		
	elif (kind == "mass"):
		mass = usda_food_data_calculated ["mass"] ["listed"];
	
		if ("per package, in grams" in mass):
			grams_per_serving = mass_swap.START ([ 
				SERVING_SIZE, 
				SERVING_SIZE_UNIT 
			], "GRAMS")
			
			SERVINGS_PER_PACKAGE = str (
				Fraction (
					Fraction (mass ["per package, in grams"]),
					Fraction (grams_per_serving)
				)
			)
		
		else:	
			raise Exception ('serving size is in "mass", but package "mass" is not known.')
	
		pass;
		
	else:
		print ({
			"serving size": [ SERVING_SIZE, SERVING_SIZE_UNIT ]
		})
		raise Exception (f'Kind, received "{ kind }", of serving size unit needs to be "volume" or "mass".')
	
	

	return SERVINGS_PER_PACKAGE